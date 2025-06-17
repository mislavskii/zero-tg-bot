import telebot.version
import telebot

from auth import *

print('Hello, zerocoders!')
print('telebot version:', telebot.version.__version__)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=[ 'start' ])
def send_welcome(message):
	bot.reply_to(message, """\
Привет! Я эхо-бот!
Умею повторять за тобой!!! \
""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if "привет" in message.text.lower():
        bot.send_message(message.chat.id, "Ты со мной noздоровался?")
    else:
        bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
