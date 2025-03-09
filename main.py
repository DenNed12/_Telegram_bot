import random

import telebot
import random
from telebot import types
from conf import TOKEN
from questions import questions
from stickers import *
bot = telebot.TeleBot(TOKEN)


user_points = {}


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    text = ('Добро пожаловать в Telegram бот Московского зоопарка!'
            ' Здесь вы можете узнать больше о нас и пройти увлекательную викторину! 🐘')
    help_text = 'Чтобы узнать, что я могу, отправьте команду /help'
    sticker_index = random.randint(0,3)
    bot.send_sticker(message.chat.id, sticker= greet[sticker_index])
    bot.send_message(message.chat.id, text=text)
    bot.send_message(message.chat.id, text=help_text)


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start_button = types.KeyboardButton('Начать')
    markup.add(start_button)
    bot.send_message(message.chat.id, text="Давайте начнем работу!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main(message: types.Message):
    if message.text == 'Начать':
        markup = types.InlineKeyboardMarkup()
        support = types.InlineKeyboardButton('Поддержка🛠', callback_data='sup')
        quiz = types.InlineKeyboardButton('Викторина❓', callback_data='quiz')
        contacts = types.InlineKeyboardButton('Наши контакты📱', callback_data='cont')
        question = types.InlineKeyboardButton("Есть вопрос?", callback_data='question')
        markup.add(support, quiz)
        markup.add(contacts, question)

        bot.send_message(message.chat.id, text='Чем вам помочь?', reply_markup=markup)
    elif message.text == '/help':
        bot.send_message(message.chat.id, text='Это help')

    elif message.text == 'Да':
        start_quiz(message)

    elif message.text == 'Нет':
        markup = types.InlineKeyboardMarkup()
        support = types.InlineKeyboardButton('Поддержка🛠', callback_data='sup')
        quiz = types.InlineKeyboardButton('Викторина❓', callback_data='quiz')
        contacts = types.InlineKeyboardButton('Наши контакты📱', callback_data='cont')
        question = types.InlineKeyboardButton("Есть вопрос?", callback_data='question')
        markup.add(support, quiz)
        markup.add(contacts, question)

        bot.send_message(message.chat.id, text='Чем вам помочь?', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: types.CallbackQuery):
    if call.data == 'quiz':
        start_quiz(call.message)
    elif call.data == 'sup':
        bot.send_message(call.message.chat.id, "Обратитесь в поддержку по email: support@example.com")
    elif call.data == 'cont':
        bot.send_message(call.message.chat.id, """
            Наши контакты: vk.com/moscow_zoo
            +7 (499) 252-29-51 - телефон для справок
            +7 (499) 255-53-75- заказ экскурсий
            +7 (499) 255-57-63 - по вопросам организации мероприятий  """)
    elif call.data == 'question':
        bot.send_message(call.message.chat.id, "Задайте ваш вопрос, и мы ответим в ближайшее время.")


def start_quiz(message: types.Message):
    user_points[message.chat.id] = 0
    send_question(message.chat.id, 0)


def send_question(chat_id, question_index):
    if question_index < len(questions):
        question_data = questions[question_index]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for option in question_data["answers"]:
            markup.add(types.KeyboardButton(option))
        bot.send_message(chat_id, question_data["question"], reply_markup=markup)
        bot.register_next_step_handler_by_chat_id(chat_id, lambda message: check_answer(message, question_index))
    else:
        bot.send_message(chat_id, f"Викторина завершена! Ваш счет: {user_points[chat_id]}")


        if user_points[chat_id] == 1:
            bot.send_message(chat_id, 'Мы подобрали для вас животное! Ваше животное в подарок от зоопарка')
            bot.send_sticker(chat_id,mouse)
            bot.send_message(chat_id,'Чтобы узнать подробнее про нашу программу опеки '
                                     'животных пройдите в нашу группу вконтаке')
        elif user_points[chat_id] == 2:
            bot.send_message(chat_id, 'Мы подобрали для вас животное! Ваше животное в подарок от зоопарка')
            bot.send_sticker(chat_id,cat)
            bot.send_message(chat_id,'Чтобы узнать подробнее про нашу программу опеки '
                                     'животных пройдите в нашу группу вконтаке')

        elif user_points[chat_id] == 3:
            bot.send_message(chat_id, 'Мы подобрали для вас животное! Ваще животное в подарок от зоопарка')
            bot.send_sticker(chat_id,dog)
            bot.send_message(chat_id,'Чтобы узнать подробнее про нашу программу опеки '
                                     'животных пройдите в нашу группу вконтаке')

        elif user_points[chat_id] == 4:
            bot.send_message(chat_id, 'Мы подобрали для вас животное! Ваше животное в подарок от зоопарка')
            bot.send_sticker(chat_id,jag)
            bot.send_message(chat_id,'Чтобы узнать подробнее про нашу программу опеки '
                                     'животных пройдите в нашу группу вконтаке')


        elif user_points[chat_id] == 5 or user_points[chat_id] == 6:
            bot.send_message(chat_id, 'Мы подобрали для вас животное! Ваiе животное в подарок от зоопарка')
            bot.send_sticker(chat_id,bear)
            bot.send_message(chat_id,'Чтобы узнать подробнее про нашу программу опеки '
                                     'животных пройдите в нашу группу вконтаке')

        elif user_points[chat_id] == 7 or user_points[chat_id] == 8:
            bot.send_message(chat_id, 'Мы подобрали для вас животное! Ваше животное в подарок от зоопарка')
            bot.send_sticker(chat_id,seal)
            bot.send_message(chat_id,'Чтобы узнать подробнее про нашу программу опеки '
                                     'животных пройдите в нашу группу вконтаке')
        else:
            bot.send_message(chat_id, 'Ошибка')

        del user_points[chat_id]
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        agree = types.KeyboardButton("Да")
        disagree = types.KeyboardButton("Нет")
        mark.add(agree,disagree)
        bot.send_message(chat_id, f"Хотите пройти викторину еще раз?", reply_markup=mark)



def check_answer(message: types.Message, question_index):
    chat_id = message.chat.id
    correct_answer = questions[question_index]["right_answer"]
    if message.text == correct_answer:
        user_points[chat_id] += 1
        bot.send_message(chat_id, "Правильно! 🎉")
    else:
        bot.send_message(chat_id, f"Неправильно. Правильный ответ: {correct_answer}")

    send_question(chat_id, question_index + 1)


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message: types.Message):
    # Получаем file_id стикера
    sticker_file_id = message.sticker.file_id
    print(f"Sticker file_id: {sticker_file_id}")

    # Отправляем file_id обратно пользователю
    bot.reply_to(message, f"File_id этого стикера: {sticker_file_id}")




if __name__ == "__main__":
    bot.skip_pending = True
    bot.polling(non_stop=True)