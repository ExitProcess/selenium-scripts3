from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.avito.ru/saransk")
elem = driver.find_element_by_name("category_id")
elem.click()
elem2 = select.Select(elem).select_by_visible_text("Квартиры")
elem3 = driver.find_element_by_id("directions")
elem3.click()


def search(keys):
    query = driver.find_element_by_id("search")
    query.clear()
    query.send_keys(keys)
    query.send_keys(Keys.RETURN)


def open_dropdowns(xpath):
    global dropdown, dropdown2
    WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    dropdown = dropdown2 = driver.find_element_by_xpath(xpath)
    dropdown.click()


# label[1] - ленинский, [2] - октябрьский, [3] - пролетарский
open_dropdowns('//div[contains(@class, "tab")]//following::label[1]')

# цена до 2 000 000 рублей
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="до, руб."]')))
driver.find_element_by_xpath('//input[@placeholder="до, руб."]').send_keys("2000000")

search("1-к квартира")

# тип объявления -- раскрыть список
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div/div[1]/div/select')

# тип объявления == Продам
select.Select(dropdown2).select_by_value("1059")  # select.Select(dropdown).select_by_visible_text("Продам")

# раскрывает список количество комнат
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div/div[2]/div/div/div/span')

# отмечает 1 комнатную квартиру
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li[2]/label/span')

# раскрывает список вид объекта
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div')

# отмечает чек-бокс вторичка
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div[2]/div/div/div/ul/li[1]/label')

# отмечает чек-бокс новостройка
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div[2]/div/div/div/ul/li[2]/label')

search("квартира")

pass
