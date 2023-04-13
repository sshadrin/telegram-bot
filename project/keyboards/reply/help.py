from loader import bot
from telebot import types

@bot.message_handler(commands=['helps'])
def help(message):
    """В данной функции, реализуем команду для бота, которая будет создавать навигационное меню в виде
    кнопок и команд"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    weather = types.KeyboardButton('Основные характеристики погоды\n/weather')
    wind = types.KeyboardButton('Основные характеристики ветра\n/wind')
    other = types.KeyboardButton('Основные характеристики атмосферного давления и влажности\n/other')
    full = types.KeyboardButton('Полный прогноз погоды от Яндекс\n/full')
    week = types.KeyboardButton('График изменения температуры на неделю\n/week')
    markup.add(weather, wind, other, full, week)
    bot.send_message(message.chat.id, "Для данного бота доступны следующие команды:",
                     reply_markup=markup)