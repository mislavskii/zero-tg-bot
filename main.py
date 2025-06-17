import random
import telebot.version
import telebot

from auth import *

print('Hello, zerocoders!')
print('telebot version:', telebot.version.__version__)

bot = telebot.TeleBot(token)

# Список анекдотов про ботов
jokes = [
    "Встретились два бота. Один говорит: 'Привет!', а другой отвечает: 'Ты уже это говорил.'",
    "Человек спрашивает у бота: 'Ты умный?' Бот отвечает: 'Да, я знаю всё! Спрашивай, пока интернет не отключили.'",
    "Бот: 'Скажи мне что-нибудь интересное.' Человек: 'Ты сам бот, придумай!'",
    "Почему бот не пошел на свидание? Он завис, пытаясь придумать, как начать разговор.",
    "Бот: 'Ты меня любишь?' Человек: 'Конечно, ты же всегда отвечаешь, чего не скажешь про людей.'"
]

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        """\
Привет! Я умный бот! Вот список того, что я умею:
- Команда /help расскажет, что я умею.
- Команда /joke или /анекдот расскажет тебе анекдот про ботов.
- А если просто напишешь сообщение, я его повторю! 😊\
"""
    )

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message,
        """\
Вот что я умею:
- /start: Запустить бота.
- /help: Посмотреть список доступных команд.
- /joke или /анекдот: Услышать смешной анекдот про ботов.
- Напиши любое сообщение, и я его повторю!\
"""
    )

# Команда /joke и /анекдот
@bot.message_handler(commands=['joke', 'анекдот'])
def send_joke(message):
    joke = random.choice(jokes)  # Выбираем случайный анекдот
    bot.reply_to(message, joke)

# Любое другое сообщение (Эхо-функция)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if "привет" in message.text.lower():
        bot.send_message(message.chat.id, "Ты со мной поздоровался? Привет! 👋")
    else:
        bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
