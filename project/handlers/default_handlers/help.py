from loader import bot
from telebot import types

@bot.message_handler(commands=['help'])
def help(message):
    """В данной функции, реализуем команду для бота, которая будет выводить инфо по командам"""
    bot.send_message(message.chat.id, "Данный бот предназначен для быстрого отслежевания погоды в г.Новодвинск, "
            "Архангельской области.\nВоспользуйтесь командой /helps для вызова навигационного меню.", parse_mode='html')