# получение ссылок стран из исходного кода страницы

import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.fifa.com/fifa-world-ranking/ranking-table/men/index.html")

# вывод сразу всех стран
button_211 = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="201-211"] span')))
ActionChains(driver).move_to_element(button_211).perform()
time.sleep(2)
ActionChains(driver).click(button_211).perform()

source = driver.page_source
tree = html.fromstring(source)

countries_list = tree.xpath("//tbody/tr/td[3]/a")

for country in countries_list:
    text = country.text_content()
    url = country.get("href")  # '/fifa-world-ranking/associations/association=ger/men/index.html'
    print(text, url)

    driver.get("http://www.fifa.com" + url)

    country_name = driver.find_element_by_css_selector(".fdh-text")
    current = driver.find_element_by_css_selector("li:nth-of-type(1) .data")
    average = driver.find_element_by_css_selector("li:nth-of-type(2) .data")

    print(country_name.text)
    print("CURRENT FIFA WORLD RANKING == ", current.text)
    print("AVERAGE POSITION SINCE FIFA WORLD RANKING CREATION == ", average.text)

driver.close()
driver.quit()
