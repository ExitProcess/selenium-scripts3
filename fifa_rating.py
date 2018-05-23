# вывод информации с главной страницы, потом история рейтинга со страниц для каждой страны
# будут использоваться actionchains, хэндлы и т.д.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.fifa.com/fifa-world-ranking/ranking-table/men/index.html")

button_211 = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '[title="201-211"] span')))
ActionChains(driver).move_to_element(button_211).perform()
time.sleep(2)
ActionChains(driver).click(button_211).perform()

# countries_list = driver.find_elements_by_xpath("//tbody/tr/td[3]/a") # css -- '.tbl-teamname [href]'
# link = country.get_attribute("href")

countries_list = driver.find_elements_by_css_selector(".tbl-teamname [href]")
for country in countries_list:
    time.sleep(2)
    ActionChains(driver).move_to_element(country).perform()
    ActionChains(driver).key_down(Keys.LEFT_CONTROL).click().perform()
    ActionChains(driver).key_up(Keys.LEFT_CONTROL).perform()