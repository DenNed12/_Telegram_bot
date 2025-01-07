import telebot
from conf import TOKEN
from quiz import *
from questions import questions

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = ('Добро пожаловать в Telegram бот Московского зоопарка!'
            ' Здесь вы можете узнать больше о нас и пройти увлекательную викторину! 🐘')
    help = ('Чтобы узнать что я могу отправте команду /help')
    bot.send_message(message.chat.id, text=text)
    bot.send_message(message.chat.id, text=help)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start = telebot.types.KeyboardButton('Начать')
    markup.add(start)
    bot.send_message(message.chat.id,text = "Давайте начнем работу!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message: telebot.types.Message):
    if message.text == 'Начать':
        telebot.types.ReplyKeyboardRemove()
        markup = telebot.types.InlineKeyboardMarkup()
        support = telebot.types.InlineKeyboardButton('Поддержка🛠', callback_data='sup')
        quiz = telebot.types.InlineKeyboardButton('Викторина❓',callback_data='quiz')
        contacts = telebot.types.InlineKeyboardButton('Наши контакты📱', callback_data='cont')
        question = telebot.types.InlineKeyboardButton("Есть вопрос?", callback_data='question')
        print(support.callback_data)
        markup.add(support,quiz)
        markup.add(contacts,question)

        bot.send_message(message.chat.id,text ='Чем вам помочь?', reply_markup=markup)
    elif message.text == '/help':
            bot.send_message(message.chat.id,text ='Это help')



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
     message = call.message
     if call.data == 'quiz':
         quiz(message)



if __name__ ==  "__main__":
    bot.skip_pending = True
    bot.polling(non_stop=True)