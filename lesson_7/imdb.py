from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


user_agent = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
)
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.imdb.com/chart/top")
movie_title_elements = driver.find_elements(By.XPATH,"//div/ul/li/div[2]/div/div/div[1]/a/h3")
rating_elements = driver.find_elements(By.XPATH,"//div/ul/li/div[2]/div/div/span/div/span/span[1]")
titles = [element.text for element in movie_title_elements]
ratings = [element.text for element in rating_elements]
for i in range(10):
    print("Rank {}: {} ({} stars)".format(i + 1, titles[i], ratings[i]))
driver.quit()
