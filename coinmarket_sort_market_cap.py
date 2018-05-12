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
list_mcap_elements = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements[-1]

for i in range(0, len(list_mcap_elements) - 1):
    elem_current = list_mcap_elements[i].text
    elem_next = list_mcap_elements[i+1].text
    elem_prev = list_mcap_elements[i-1].text
    # условие для сравнения строк разной длины ("$146 109 484 586 больше $67 635 761 404")
    if len(elem_current) > len(elem_next) and len(elem_next) != 2:
        print(elem_current, "больше", elem_next)
    # условие для сравнения строк одинаковой длины ("$67 635 761 404 больше $27 646 445 524")
    if elem_current > elem_next:
        print(elem_current, "больше", elem_next)
    # граница между элементами с известной и неизвестной рыночной стоимостью
    if elem_current == "$?" and len(elem_prev) > 2:
        print("#"*22)
    if elem_current == "$?":
        print(elem_current, "стоимость неизвестна")

driver.close()
driver.quit()
