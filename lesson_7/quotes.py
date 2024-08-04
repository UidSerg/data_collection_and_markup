from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv



# Запуск нового экземпляра браузера Chrome
user_agent = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
)
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
browser = webdriver.Chrome(options=chrome_option)
# Переход на первую страницу веб-сайта
browser.get("http://quotes.toscrape.com/page/1/")
# Инициализация пустого списка для хранения цитат
quotes = []
while True:
    # Поиск всех цитат на странице с помощью xpath
    quote_elements = browser.find_elements(By.XPATH,
    '//div[@class="quote"]')
    # Извлечение текста каждой цитаты
    for quote_element in quote_elements:
        quote = quote_element.find_element(By.XPATH,
        './/span[@class="text"]').text
        author = quote_element.find_element(By.XPATH,
        './/span/small[@class="author"]').text
        quotes.append({"quote": quote, "author": author})
    # Проверка наличия следующей кнопки
    next_button = browser.find_elements(By.XPATH,'//li[@class="next"]/a')
    if not next_button:
        break
    # Нажатие следующей кнопки
    next_button[0].click()
    # Ожидание загрузки страницы
    time.sleep(1)
# Запись данных в файл CSV
with open("./lesson_7/quotes.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(quotes)
# Закрытие браузера
browser.close()
# Вывод цитат
# for quote in quotes:
#    print(quote["quote"], "by", quote["author"])