#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '7760078560:AAHTic43wy13C-e-fvdJi-jgvJVEA10oebI'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['ajuda', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Menssagem de teste, apenas para testar o bot\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
