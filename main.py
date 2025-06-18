import random
import telebot.version
import telebot

import router as rt

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
- Команда /coinflip подбрасывает монетку.
- Команда /roll6 бросает шестигранный кубик.
- Команда /roll10 бросает десятигранный кубик.
- Команда /roll20 бросает двадцатигранный кубик.
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
- /coinflip: Подбросить монетку (орёл или решка).
- /roll6: Бросить шестигранный кубик (от 1 до 6).
- /roll10: Бросить десятигранный кубик (от 1 до 10).
- /roll20: Бросить двадцатигранный кубик (от 1 до 20).
- Напиши любое сообщение, и я его повторю!\
"""
    )

# Команда /joke и /анекдот
@bot.message_handler(commands=['joke', 'анекдот'])
def send_joke(message):
    joke = random.choice(jokes)  # Выбираем случайный анекдот
    bot.reply_to(message, joke)

# Команда /coinflip
@bot.message_handler(commands=['coinflip'])
def coinflip(message):
    result = random.choice(['Орёл', 'Решка'])
    bot.reply_to(message, f"Монетка подброшена: {result}! 🪙")

# Команда /roll6
@bot.message_handler(commands=['roll6'])
def roll6(message):
    result = random.randint(1, 6)
    bot.reply_to(message, f"Шестигранный кубик: {result}! 🎲")

# Команда /roll10
@bot.message_handler(commands=['roll10'])
def roll10(message):
    result = random.randint(1, 10)
    bot.reply_to(message, f"Десятигранный кубик: {result}! 🎲")

# Команда /roll20
@bot.message_handler(commands=['roll20'])
def roll20(message):
    result = random.randint(1, 20)
    bot.reply_to(message, f"Двадцатигранный кубик: {result}! 🎲")

# Любое другое сообщение (Эхо-функция)
@bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     if "привет" in message.text.lower():
#         bot.send_message(message.chat.id, "Ты со мной поздоровался? Привет! 👋")
#     else:
#         bot.send_message(message.chat.id, message.text)
def reply(message):
    reply = rt.extract_content(rt.query_ai(message.text))
    bot.send_message(message.chat.id, reply)

print('starting up!')

bot.infinity_polling()
