from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv

def sroll_to(driver):
    """Фунция скроллинга до конца"""
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(3)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Настройка веб-драйвера (например, Chrome)
user_agent = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
)
chrome_option = Options()
chrome_option.add_argument("--disable-blink-features=AutomationControlled") ## скрыть использование webdriver
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)


try:
    # Открываем ozon.ru
    driver.get("https://ozon.ru")
    time.sleep(3)  # Ожидание загрузки страницы

    #всплывающее окно для уточнений адреса жмем "не сейчас"
    no_adrers = driver.find_element(By.XPATH,"//div/button[2]/div[2]")
    if no_adrers:
        no_adrers.click()
    time.sleep(1)  # Ожидание загрузки страницы

    #всплывающее окно cookies
    try:
        ok_cook = driver.find_element(By.XPATH,'//div[@data-widget="cookieBubble"]//button')
        if ok_cook:
            ok_cook.click()
        time.sleep(1)  # Ожидание загрузки страницы
    except Exception as e:
        print(f"окна не было {e}")

    # выбираем категорю где искать
    cat_down = driver.find_element(By.XPATH,"//form/div/div[1]/span[1]")
    cat_down.click()
    time.sleep(3)  # Ожидание загрузки страницы

    # в меню выбираем "электороника"
    cat_enter = driver.find_element(By.XPATH,'//div[@class="ae0a_32"]/div[1]')
    cat_enter.click()
    time.sleep(3)  # Ожидание загрузки страницы

    # Находим строку поиска
    search_field = driver.find_element(By.NAME, "text")

    # Вводим в строку поиска "что ищем"
    search_field.send_keys("винтелятор для Nvidia RTX 3060")

    # Нажимаем Enter для поиска
    search_field.send_keys(Keys.RETURN)
    time.sleep(3)  # Ожидание загрузки результатов поиска

    # ищем меню сортировки и открываем
    sort = driver.find_element(By.XPATH,'//div/input[@title="Популярные"]')
    sort.click()
    time.sleep(1)  # Ожидание загрузки 
    # сортируем по "дешевле"
    price_low = driver.find_element(By.XPATH,'//div[4]/div/div/div[3]/div[1]')
    price_low.click()

    time.sleep(10)  # Ожидание загрузки результатов поиска
    # скролл вниз 
    sroll_to(driver)
    time.sleep(5)  # Ожидание загрузки результатов поиска

    
    # получаем список элементов
    results = driver.find_elements(By.XPATH, '//*[@id="paginatorContent"]/div/div/div')
    time.sleep(5)  # Ожидание загрузки результатов поиска
    data = []

    for result in results:
        try:
            title = result.find_element(By.XPATH, './/a/div/span').text
        except Exception as e:
            print(f"ОШИБКА!!! {e}")
            title = "Not Found 404"
        try:
            price = result.find_element(By.XPATH, './/div[3]/div[1]/div/span[1]').text
        except Exception as e:
            print(f"ОШИБКА!!! {e}")
            price = "Not Found 404" 
        try:       
            stock = result.find_element(By.XPATH, './/div[3]/div[2]/span').text
        except Exception as e:
            print(f"ОШИБКА!!! {e}")
            stock = "Not Found 404" 
        data.append({
            'title': title,
            'price': price.replace('\u2009', '')[:-1],
            'stock': stock
        })
        print(str(data)) 


    with open('./home_work_7/results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'price', 'stock']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
                writer.writerow(row)
    print(data)

    # Показываем результаты поиска 
    print("Результаты поиска загружены. Браузер будет закрыт через 10 секунд.")
    time.sleep(10)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()