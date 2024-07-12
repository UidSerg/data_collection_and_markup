"""
- Установите пакет PyMongo и импортируйте MongoClient и json.
- Установите Compass MongoDB
- Подключитесь к серверу MongoDB по адресу 'mongodb://localhost:27017/'.
- Создайте базу данных 'town_cary' и коллекцию 'crashes'.
- Выполните чтение файла JSON 'crash-data.json'.
- Напишите функцию chunk_data, которая принимает два аргумента: список данных и размер фрагмента. Функция должна разделить данные на более мелкие фрагменты указанного размера и вернуть генератор.
- Разделите данные JSON на фрагменты по 5000 записей в каждом. 
- Переберите все фрагменты и вставьте каждый фрагмент в коллекцию MongoDB с помощью функции insert_many(). 
- Выведите финальное сообщение, указывающее на то, что данные были успешно вставлены.
"""

import json
from pymongo import MongoClient

client = MongoClient()
db = client['town_cary']
collection = db['crashes']


all_docs = collection.find()
first_doc = all_docs[0]

pretty_json = json.dumps(first_doc, indent=4, default=str)
print(pretty_json)