from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.avito.ru/saransk")
elem = driver.find_element_by_name("category_id")
elem.click()
elem2 = select.Select(elem).select_by_visible_text("Автомобили")
elem3 = driver.find_element_by_id("directions")
elem3.click()

# клик и раскрытие выпадающего меню
def open_dropdowns(xpath):
    global dropdown, dropdown2
    WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    dropdown = dropdown2 = driver.find_element_by_xpath(xpath)
    dropdown.click()

# клик и удержание по кнопке слайдера
def slider_hold(slider):
    ActionChains(driver).click_and_hold(slider).perform()

# перемещение слайдера
def slider_move(offsetX, offsetY):
    ActionChains(driver).move_by_offset(offsetX, offsetY).perform()

# перестает удерживать кнопку слайдера
def slider_release(slider):
    ActionChains(driver).release(slider).perform()

# label[1] - ленинский, [2] - октябрьский, [3] - пролетарский
open_dropdowns('//div[contains(@class, "tab")]//following::label[1]')
open_dropdowns('//div[contains(@class, "tab")]//following::label[2]')
open_dropdowns('//div[contains(@class, "tab")]//following::label[3]')

# марка -- раскрыть список
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div[2]/div[1]/div/select')

# выбрать volvo
select.Select(dropdown2).select_by_value("1219")  # select.Select(dropdown).select_by_visible_text("Volvo")

open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div[1]/div[1]/ul/li[1]/label/span')
open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div[1]/div[1]/ul/li[2]/label/span')
open_dropdowns('//*[@id="pre-filters"]/label[2]/span')

open_dropdowns('//*[@id="catalog"]/div[4]/div/div/div/div[2]/div[4]/div/div/div[1]/span')

slider_left = driver.find_element_by_xpath(
    '//*[@id="catalog"]/div[4]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/div/div/div/div/div/i[1]')

slider_hold(slider_left)

while dropdown2.text < "от 2000  г.в.":
    slider_move(1, 0)
slider_release(slider_left)

slider_right = driver.find_element_by_xpath(
    '//*[@id="catalog"]/div[4]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/div/div/div/div/div/i[2]')

slider_hold(slider_right)

# до начала проверки надо дернуть правый слайдер, чтобы значение "от 2000  г.в." сменилось на "2000—2017  г.в."
slider_move(-3, 0)

while dropdown2.text > "2000—2011  г.в.":
    slider_move(-1, 0)
slider_release(slider_right)

search = driver.find_element_by_id('search')
search.send_keys(Keys.RETURN)

# test
# search_button = driver.find_element_by_xpath('//*[@id="search_form"]/div[1]/div[1]/div[2]/input')
# ActionChains(driver).move_to_element(search_button).perform()

driver.close()
driver.quit()