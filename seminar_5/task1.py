"""
 Создайте проект Scrapy и паука для скрейпинга только названий стран из таблицы.
- Добавьте User Agent.
- Реализуйте метод извлечения данных с помощью селекторов CSS или XPath и получения элементов Scrapy.
- Сохраните данные в JSON-файл.

Паук должен записывать извлеченные данные в словарь.
- Модифицируйте предыдущий сценарий, чтобы получить дополнительные данные из столбцов таблицы:  Membership within the UN, Sovereignty dispute information, Country status.
- В методе parse выполните итерации по строкам стран в таблице (wikitable).
- Извлеките из таблицы требуемые данные.
- Сохраните данные в JSON-файл. Запустите паука с помощью команды scrapy crawl countries_spider -o output.json, чтобы сохранить собранные данные в JSON-файл.


Если какая-либо извлеченная информация отсутствует, установите для соответствующего словаря значение None.

Задание 3
Скрейпинг информацию о каждой стране: название столицы (Capital), официальные языки (Official languages) и данные о площади (Area: Total, Water).

Задание:

- В методе parse выполните итерации по строкам стран в таблице (wikitable).
- Извлеките URL для каждой страницы Википедии, соответствующей стране, соединив базовый URL с относительным URL.
- Создайте метод parse_country_page в котором для каждой страны из таблицы infobox с помощью выражений XPath извлеките столицу, официальные языки, общую площадь и процент воды.
- Используйте библиотеку re для извлечения числовых данных о площади и проценте воды.
- Добавьте извлеченную информацию в словарь.
en.wikipedia.org/wiki/List_of_sovereign_states
"""


