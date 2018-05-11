# скрипт проверяет работу сортировки рыночной стоимости криптовалют на сайте
# https://coinmarketcap.com/all/views/all/

from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/all/views/all/")
# сортировка по убыванию
sort_button = driver.find_element_by_css_selector("#th-marketcap")
sort_button.click()

#
list_mc = driver.find_elements_by_css_selector(".market-cap")
del list_mc[-1]

for i in range(0, len(list_mc)-1):
    elem_current = list_mc[i].text
    elem_next = list_mc[i+1].text
    elem_prev = list_mc[i-1].text
    if elem_current > elem_next:
        print(elem_current, "больше", elem_next)
    if elem_current == "$?" and len(elem_prev) > 2:
        print(elem_prev, "последний элемент с известной стоимостью")
    if elem_current == "$?":
        print(elem_current, "стоимость неизвестна")

driver.close()
driver.quit()
