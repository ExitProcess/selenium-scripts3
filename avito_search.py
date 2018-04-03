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

"""label[1] - ленинский, [2] - октябрьский, [3] - пролетарский"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "tab")]//following::label[1]')))
driver.find_element_by_xpath('//div[contains(@class, "tab")]//following::label[1]').click()

"""цена до 2 000 000 рублей"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="до, руб."]')))
driver.find_element_by_xpath('//input[@placeholder="до, руб."]').send_keys("2000000")

def search(keys):
    query = driver.find_element_by_id("search")
    query.clear()
    query.send_keys(keys)
    query.send_keys(Keys.RETURN)

search("1-к квартира")

"""тип объявления == Продам"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog"]/div[4]/div/div/div/div/div[1]/div/select')))
elem5 = driver.find_element_by_xpath('//*[@id="catalog"]/div[4]/div/div/div/div/div[1]/div/select')
elem5.click()
#select.Select(elem5).select_by_visible_text("Продам")
select.Select(elem5).select_by_value("1059")

"""раскрывает список количество комнат"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog"]/div[4]/div/div/div/div/div[2]/div/div/div/span')))
elem6 = driver.find_element_by_xpath('//*[@id="catalog"]/div[4]/div/div/div/div/div[2]/div/div/div/span')
elem6.click()
"""отмечает 1 комнатную квартиру"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog"]/div[4]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li[2]/label/span')))
driver.find_element_by_xpath('//*[@id="catalog"]/div[4]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li[2]/label/span').click()

"""раскрывает список вид объекта"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div')))
elem7 = driver.find_element_by_xpath('//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div')
elem7.click()
"""отмечает чек-бокс вторичка"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div[2]/div/div/div/ul/li[1]/label')))
driver.find_element_by_xpath('//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div[2]/div/div/div/ul/li[1]/label').click()
"""отмечает чек-бокс новостройка"""
WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div[2]/div/div/div/ul/li[2]/label')))
driver.find_element_by_xpath('//*[@id="catalog"]/div[4]/div/div/div/div/div[3]/div/div/div[2]/div/div/div/ul/li[2]/label').click()

search("квартира")

pass