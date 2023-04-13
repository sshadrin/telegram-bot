from telebot.types import BotCommand
from project.config_data.config import DEFAULT_COMMANDS

def set_default_commands(bot):
    """В данной функции, реализуем меню, которое будет выводить все доступные команды"""
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )