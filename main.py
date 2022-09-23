import telebot
from telebot import types

bot = telebot.TeleBot('5793963547:AAGFSj-kGOqrYxaVq20afvbhyYc15RzRPac')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🖥 Веб сайт!')
    item2 = types.KeyboardButton('🖊 Записаться!')

    markup.add(item1,item2)

    photo = open('5.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, выбери один из пунктов ниже⬇️', reply_markup=markup )

    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        if message.chat.type == 'private':
            if message.text == '🖥 Веб сайт!':
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='http://127.0.0.1:8000'))
                bot.send_message(message.chat.id, '⬇️', reply_markup=markup)

            elif message.text == '🖊 Записаться!':
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('Записаться на стригу!', url='https://t.me/pavelap'))
                bot.send_message(message.chat.id, '⬇️', reply_markup=markup)



bot.polling(none_stop=True)
