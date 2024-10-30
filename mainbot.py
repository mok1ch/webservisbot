import telebot
from telebot import TeleBot
from handlers import register_handlers

TOKEN = '7654102260:AAGftG_qr2WK75VcGZDfAzDj0M6j4I8KjuI'
bot = telebot.TeleBot(TOKEN)

register_handlers(bot)

if __name__ == '__main__':
    bot.infinity_polling()
