# вывод информации с главной страницы, потом история рейтинга со страниц для каждой страны
# будут использоваться actionchains, хэндлы и т.д.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.fifa.com/fifa-world-ranking/ranking-table/men/index.html")

# вывод сразу всех стран для дальнейшего создания списка
button_211 = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[title="201-211"] span')))
ActionChains(driver).move_to_element(button_211).perform()
time.sleep(2)
ActionChains(driver).click(button_211).perform()

# countries_list = driver.find_elements_by_xpath("//tbody/tr/td[3]/a") # css -- '.tbl-teamname [href]'
# link = country.get_attribute("href")

countries_list = driver.find_elements_by_css_selector(".tbl-teamname [href]")
for country in countries_list:
    time.sleep(0.5)
    ActionChains(driver).move_to_element(country).perform()
    time.sleep(0.5)
    # в цикле в новой вкладке открывается персональная страница страны;
    # теперь открывается с 1-ой команды, т.е. с Германии
    ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(country).key_up(Keys.LEFT_CONTROL).perform()

    window_handles = driver.window_handles
    # в связи с тем, что цикл начинает работать со 2-го элемента, проверяется, открыто ли 2 вкладки
    if len(window_handles) < 2:  # если открыта 1 вкладка, то пропустить оставшееся тело цикла и начать новую итерацию
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

