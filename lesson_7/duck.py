# Импорт необходимых библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv


user_agent = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
)
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)
# Переход на веб-сайт DuckDuckGo
driver.get("https://duckduckgo.com/")
# Поиск строки поиска и ввод поискового запроса
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("Selenium books")
# Поиск кнопки поиска и нажатие на нее
search_button = driver.find_element(By.XPATH,"//div/button")
search_button.click()
# Поиск выпадающего меню "Время" и щелчок по нему
time_dropdown = driver.find_element(By.XPATH,"//*[@id='links_wrapper']/div[1]/div[1]/div/div[3]/a")
time_dropdown.click()
# Поиск опции "За последний месяц" в выпадающем меню времени ищелчок по ней
time_last_month = driver.find_element(By.XPATH,"*//a[@data-value='m']")
time_last_month.click()
more_btn = driver.find_element(By.XPATH,"//a[@class='result--more__btn btn btn--full']")
more_btn.click()
# Поиск всех результатов на странице
results = driver.find_elements(By.XPATH,"//div[@class='nrn-react-div']")
result_data = []
# Извлечение заголовка и URL каждого результата
for result in results:
    result_title = result.find_element(By.XPATH,".//a[@class='eVNpHGjtxRBq_gLOfGDr LQNqh2U1kzYxREs65IJu']").text
    result_url = result.find_element(By.XPATH,".//a[@class='eVNpHGjtxRBq_gLOfGDr LQNqh2U1kzYxREs65IJu']").get_attribute("href")
    result_data.append([result_title, result_url])
driver.quit()
# Запись данных в файл CSV
with open("./lesson_7/quotes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Result Title", "URL"])
    writer.writerows(result_data)