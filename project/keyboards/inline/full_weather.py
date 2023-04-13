from loader import bot, url_yandex, headers
from telebot import types
import requests
import json

@bot.message_handler(commands=['full'])
def weather(message):
    """В данной функции, реализуем команду для бота, которая будет создавать кнопку-ссылку на url яндекса с полным
    прогнозом погоды"""
    request = requests.get(url=url_yandex, headers=headers, timeout=10)
    if request.status_code == 200:
        data = json.loads(request.text)
        inf = data['info']['url']
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Яндекс Погода", url=inf))
        bot.send_message(message.chat.id,"Если хотите более подробный анализ погоды, перейдите на сайт",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "API problems")