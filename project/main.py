from loader import bot
import handlers
import keyboards
from utils.set_bot_commands import set_default_commands

# Запускатор
if __name__ == "__main__":
    set_default_commands(bot)
    bot.polling(none_stop=True)
