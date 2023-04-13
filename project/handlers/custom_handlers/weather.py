from loader import bot, url_yandex, headers
import requests
import json


@bot.message_handler(commands=['weather'])
def weather(message):
    """В данной функции, реализуем команду для бота, которая будет выводить основные характеристики погоды"""
    request = requests.get(url=url_yandex, headers=headers, timeout=10)
    if request.status_code == 200:
        data = json.loads(request.text)
        temp = data['fact']['temp']
        feels = data['fact']['feels_like']
        date_time = data['now_dt']
        condition = data['fact']['condition']
        condition_dict = {"clear": "ясно", "partly-cloudy": "малооблачно", "cloudy": "облачно с прояснениями",
        "overcast": "пасмурно", "drizzle": "морось", "light-rain": "небольшой дождь", "rain": "дождь","moderate-rain":
        "умеренно сильный дождь","heavy-rain": "сильный дождь","continuous-heavy-rain": "длительный сильный дождь",
        "showers": "ливень","wet-snow": "дождь со снегом","light-snow": "небольшой снег","snow": "снег",
        "snow-showers": "снегопад", "hail": "град", "thunderstorm": "гроза", "thunderstorm-with-rain": "дождь с грозой",
                          "thunderstorm-with-hail": "гроза с градом"}
        if condition in condition_dict.keys():
            condition_ru = condition_dict[condition]
        bot.send_message(message.chat.id, "Температура в Новодвинске: на {d}:\n Сейчас: {temp} \N{DEGREE SIGN}C; \n "
        "Ощущается, как: {feels}  \N{DEGREE SIGN}C;\n На улице {condition}!".format(
            d=date_time[0:10], temp=temp, feels=feels, condition=condition_ru))
    else:
        bot.send_message(message.chat.id, "API problems")