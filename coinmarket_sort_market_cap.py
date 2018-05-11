# скрипт проверяет работу сортировки рыночной стоимости криптовалют на сайте
# https://coinmarketcap.com/all/views/all/

from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/all/views/all/")
sort_button = driver.find_element_by_css_selector("#th-marketcap")
sort_button.click()

#

list_mc = driver.find_elements_by_css_selector(".market-cap")
del list_mc[-1]


for i in range(0, len(list_mc)-1):
    if list_mc[i].text > list_mc[i + 1].text:
        print(list_mc[i].text, "больше", list_mc[i + 1].text)
    if list_mc[i].text == "$?" and len(list_mc[i-1].text) > 2:
        print(list_mc[i-1].text, "последний элемент с известной стоимостью")
    if list_mc[i].text == "$?":
        print(list_mc[i].text, "стоимость неизвестна")
