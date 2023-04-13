import telebot
from config_data import config

# основной загрузочный файл
bot = telebot.TeleBot(config.api_token)
url_yandex = "https://api.weather.yandex.ru/v2/forecast?lat=64.25&lon=40.49&lang=ru_RU&limit=7"
headers = {"X-Yandex-API-Key": config.token_yandex}