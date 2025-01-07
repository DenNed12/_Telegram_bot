import telebot
from main import *
import questions

points = 0

bot.message_handler(content_types=['text'])
def quiz(message: telebot.types.Message):
    global points
    start_mk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = telebot.types.InlineKeyboardButton('Начать викторину')
    start_mk.add(start)
    bot.send_message(message.chat.id, text= "Начать викторину?",reply_markup =start_mk)
    print(message.text)

    # вот этот if  не срабатывает
    if message.text == 'Начать викторину':
        question = questions[0]
        print(question)
            # points = 0
            # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            # button1 = telebot.types.InlineKeyboardButton('Начать викторину')
            # button2 = telebot.types.InlineKeyboardButton('Начать викторину')
            # button3 = telebot.types.InlineKeyboardButton('Начать викторину')
            # markup.add(button1,button2,button3)
            # bot.send_message(message.chat.id, text="Начать викторину?", reply_markup=start_mk)
