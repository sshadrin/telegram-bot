from loader import bot


@bot.message_handler(commands=["start"])
def start(message):
    """В данной функции, реализуем команду для бота, которая будет приветствовать пользователя"""
    bot.send_message(message.chat.id, "Здравствуйте уважаемый {name} {surname}, используйте команду /help для "
    "получения справки по использованию бота.".format(
        name=message.from_user.first_name, surname=message.from_user.last_name), parse_mode='html')
