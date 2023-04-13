import os
from dotenv import load_dotenv, find_dotenv  # подключаем модуль dotenv для использования токенов

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

load_dotenv(find_dotenv())  # если в файле .env существует объект, получаем его
api_token = os.getenv("api_token")
load_dotenv(find_dotenv())
token_yandex = os.getenv("token_yandex")

DEFAULT_COMMANDS = (  # команды для нашего бота
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("helps", "Справочное меню"),
    ("weather", "Показать погоду"),
    ("wind", "Данные о ветре"),
    ("other", "Данные о давлении и влажности"),
    ("full", "Полные данные о погоде от Яндекс"),
    ("week", "Вывести график изменения температуры на неделю")
    )