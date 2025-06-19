import random
import telebot.version
import telebot
import traceback

import router as rt
import utils as ut

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
- Или просто напиши любое сообщение, и я постараюсь дать подходящий ответ!\
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

# Любое другое сообщение (задействуем сторонний ИИ)
@bot.message_handler(func=lambda message: True)
def reply(message):
    # Отправляем предварительное сообщение пользователю
    preparation_message = bot.send_message(message.chat.id, "Идет подготовка ответа...")
    # Генерируем ответ
    reply_text = rt.generate_ai_response(message.text)
    # Удаляем сообщение "Идет подготовка ответа..."
    bot.delete_message(message.chat.id, preparation_message.message_id)
    reply_chunks = ut.split_message(reply_text)
    # a text not exceeding TG's limit will be sent entirely in the first and only chunk
    for chunk in reply_chunks:   
        try:
            bot.send_message(message.chat.id, chunk)
        except Exception:
            traceback.print_exc()
            bot.send_message(message.chat.id, 'Это слишком сложно для меня! Прости, пожалуйста...')

# @bot.message_handler(func=lambda message: True)
# def reply(message):
#     # Отправляем предварительное сообщение пользователю
#     preparation_message = bot.send_message(message.chat.id, "Идет подготовка ответа...")
    
#     try:
#         # Генерируем ответ
#         reply_text = rt.generate_ai_response(message.text)
#         reply_chunks = ut.split_message(reply_text)
        
#         # Удаляем сообщение "Идет подготовка ответа..."
#         bot.delete_message(message.chat.id, preparation_message.message_id)

#         # Отправляем ответ частями, если необходимо
#         for chunk in reply_chunks:
#             bot.send_message(message.chat.id, chunk)
#     except Exception:
#         # Если произошла ошибка, удаляем сообщение "Идет подготовка ответа..."
#         bot.delete_message(message.chat.id, preparation_message.message_id)
        
#         # Логируем ошибку и отправляем сообщение об ошибке пользователю
#         traceback.print_exc()
#         bot.send_message(message.chat.id, 'Это слишком сложно для меня! Прости, пожалуйста...')

print('starting up!')

bot.infinity_polling()
