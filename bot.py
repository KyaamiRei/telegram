import telebot
import config
import random
import os

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "офай нахуй, {0.first_name}!!! \nБез нигатива :) ♥ ".format(message.from_user),
    parse_mode='html') 

# @bot.message_handler(commands=['givePicture'])
# def answer(message):
#     bot.send_message(message.chat.id, "Можешь подождать {0.first_name}?. \nПлииииз♥".format(message.from_user), 
#     parse_mode='html')

    # rnd = random.randint(0,3)

    # pic = open(f'static/qq ({rnd}).jpg', 'rb')
    # bot.send_message(message.chat.id, "Но для тебя у меня есть вот это!, -> " + str(rnd))
    # bot.send_photo(message.chat.id, pic)

@bot.message_handler(commands=['giveList'])
def fileCount(message):
    fileList = os.listdir(path="static")

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Хочешь чтобы я их сбросила?", callback_data='send') 

    markup.add(item1)

    bot.send_message(message.chat.id, "Вот столько картинок я тебе загружу -> " + str(len(fileList)-1), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Привет':
            bot.send_message(message.chat.id, "Привет, меня зовут {0.first_name}".format(bot.get_me()),
            parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Я не знаю что ответить (")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'send':
                rnd = random.randint(0,3)

                pic = open(f'static/qq ({rnd}).jpg', 'rb')
                bot.send_message(call.message.chat.id, "Вот что у меня есть для тебя!, -> " + str(rnd))
                bot.send_photo(call.message.chat.id, pic)
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)