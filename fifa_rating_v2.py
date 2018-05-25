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

# вывод сразу всех стран
button_211 = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="201-211"] span')))
ActionChains(driver).move_to_element(button_211).perform()
time.sleep(2)
ActionChains(driver).click(button_211).perform()

for i in range(2, 211):
    xpath = "//tbody/tr[" + str(i) + "]/td[3]/a"

    country_button = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    time.sleep(1)
    ActionChains(driver).move_to_element(country_button).perform()
    time.sleep(1)
    ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(country_button).key_up(Keys.LEFT_CONTROL).perform()

    window_handles = driver.window_handles
    if len(window_handles) < 2:
        continue

    countries_page = window_handles[0]
    country_personal_page = window_handles[1]
    driver.switch_to.window(country_personal_page)

    country_name = driver.find_element_by_css_selector(".fdh-text")
    current = driver.find_element_by_css_selector("li:nth-of-type(1) .data")
    average = driver.find_element_by_css_selector("li:nth-of-type(2) .data")

    print(country_name.text)
    print("CURRENT FIFA WORLD RANKING == ", current.text)
    print("AVERAGE POSITION SINCE FIFA WORLD RANKING CREATION == ", average.text)

    driver.close()
    driver.switch_to.window(countries_page)

driver.close()
driver.quit()
