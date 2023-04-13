from loader import bot, url_yandex, headers
import requests
import json


@bot.message_handler(commands=['other'])
def other(message):
    """В данной функции, реализуем команду для бота, которая будет выводить характеристики давления и влажности"""
    request = requests.get(url=url_yandex, headers=headers, timeout=10)
    if request.status_code == 200:
        data = json.loads(request.text)
        date_time = data['now_dt']
        pressure = data['fact']['pressure_mm']
        humidity = data['fact']['humidity']
        season = data['fact']['season']
        season_dir = {"summer": "лето", "autumn": "осень", "winter": "зима", "spring": " весна"}
        if season in season_dir.keys():
            season_ru = season_dir[season]
        bot.send_message(message.chat.id, "Характеристики давления и влажности в Новодвинске на {d}:\n"
        "Атмосферное давление: {pressure} мм рт. ст.\nВлажность воздуха: {humidity} %;\nВ данном регионе сейчас "
        "{season}!".format(d=date_time[0:10], pressure=pressure, humidity=humidity, season=season_ru))
    else:
        bot.send_message(message.chat.id, "API problems")
