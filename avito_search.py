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
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='rf_district_286']//following::label[1]")))
driver.find_element_by_xpath("//input[@id='rf_district_286']//following::label[1]").click()

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="до, руб."]')))
driver.find_element_by_xpath('//input[@placeholder="до, руб."]').send_keys("2000000")

query = driver.find_element_by_id("search")
query.send_keys("1-к квартира")
query.send_keys(Keys.RETURN)

pass