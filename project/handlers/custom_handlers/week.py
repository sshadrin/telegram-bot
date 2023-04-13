from loader import bot, url_yandex, headers
import requests
import json
import math
from matplotlib import pyplot
import matplotlib

@bot.message_handler(commands=['week'])
def weather(message):
    """В данной функции, реализуем команду для бота, которая будет выводить график изменения температуры на неделю
    вперед"""
    request = requests.get(url=url_yandex, headers=headers, timeout=10)
    if request.status_code == 200:
        data = json.loads(request.text)
        yesday_tmp = data['yesterday']['temp']
        today = data['now_dt']
        today_tmp = data['fact']['temp']
        forecasts = data['forecasts']
        nextday_1 = forecasts[1]['date']
        nextday_tmp_1 = math.ceil((forecasts[1]['parts']['night_short']['temp'] +
                                 forecasts[1]['parts']['day_short']['temp']) / 2)
        nextday_2 = forecasts[2]['date']
        nextday_tmp_2 = math.ceil((forecasts[2]['parts']['night_short']['temp'] +
                                 forecasts[2]['parts']['day_short']['temp']) / 2)
        nextday_3 = forecasts[3]['date']
        nextday_tmp_3 = math.ceil((forecasts[3]['parts']['night_short']['temp'] +
                                 forecasts[3]['parts']['day_short']['temp']) / 2)
        nextday_4 = forecasts[4]['date']
        nextday_tmp_4 = math.ceil((forecasts[4]['parts']['night_short']['temp'] +
                                 forecasts[4]['parts']['day_short']['temp']) / 2)
        nextday_5 = forecasts[5]['date']
        nextday_tmp_5 = math.ceil((forecasts[5]['parts']['night_short']['temp'] +
                                   forecasts[5]['parts']['day_short']['temp']) / 2)

        gradus = [yesday_tmp, today_tmp, nextday_tmp_1, nextday_tmp_2, nextday_tmp_3, nextday_tmp_4, nextday_tmp_5]
        days = ['yesterday', today[0:10], nextday_1, nextday_2, nextday_3, nextday_4, nextday_5]
        matplotlib.use('agg')
        pyplot.style.use('seaborn-v0_8')
        figura, axes = pyplot.subplots()
        axes.plot(days, gradus, linewidth=3)
        axes.set_title("Недельный график изменения погоды", fontsize=24)
        axes.set_xlabel("Дата", fontsize=14)
        axes.set_ylabel("Температура в \N{DEGREE SIGN}C", fontsize=14)
        axes.scatter(days, gradus, color=(0, 0.8, 0), s=100)
        axes.tick_params(axis='both', labelsize=10)
        pyplot.savefig('figure.png')
        figure = open('figure.png', 'rb')
        bot.send_photo(message.chat.id, figure)
    else:
        bot.send_message(message.chat.id, "API problems")