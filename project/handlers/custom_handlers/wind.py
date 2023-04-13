from loader import bot, url_yandex, headers
import requests
import json


@bot.message_handler(commands=['wind'])
def weather(message):
    """В данной функции, реализуем команду для бота, которая будет выводить характеристики для ветра"""
    request = requests.get(url=url_yandex, headers=headers, timeout=10)
    if request.status_code == 200:
        data = json.loads(request.text)
        date_time = data['now_dt']
        wind = data['fact']['wind_speed']
        wind_gust = data['fact']['wind_gust']
        wind_dir = data['fact']['wind_dir']
        wind_dir_dict = {"nw": "северо-западное", "n": "северное", "ne": "северо-восточное", "e": " восточное",
        "se": "юго-восточное", "s": "южное", "sw": "юго-западное","w": "западное","c": "штиль"}
        if wind_dir in wind_dir_dict.keys():
            wind_ru = wind_dir_dict[wind_dir]
        bot.send_message(message.chat.id, "Характеристики ветра в Новодвинске на {d}:\n Скорость ветра: {wind} м/с;\n "
        "Скорость порывов ветра: {wind_gust} м/с;\n Направление ветра: {wind_ru}!".format(
            d=date_time[0:10], wind=wind, wind_gust=wind_gust, wind_ru=wind_ru.title()))
    else:
        bot.send_message(message.chat.id, "API problems")