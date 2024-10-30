import telebot

from weather_api import OpenWeatherApi

def register_handlers(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def start(message: telebot.types.Message):
        msg = bot.send_message(message.chat.id, 'Введи город: ')
        bot.register_next_step_handler(msg, get_weather)

    def get_weather(message: telebot.types.Message):
        city = message.text
        weather = OpenWeatherApi(city)
        bot.send_message(message.chat.id, weather.get_answer())

    @bot.message_handler(commands=['info'])
    def info(message: telebot.types.Message):
        bot.send_message(message.chat.id, 'Author: Danil')




