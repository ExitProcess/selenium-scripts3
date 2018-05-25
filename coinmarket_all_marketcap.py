# скрипт проверяет работу сортировки рыночной стоимости криптовалют на сайте
# https://coinmarketcap.com/all/views/all/

from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/all/views/all/")
# сортировка по убыванию
sort_button = driver.find_element_by_css_selector("#th-marketcap")
sort_button.click()

list_mcap_elements = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements[-1]

# работа с list_mcap_elements
# цикл проверяет, чтобы следующий элемент списка был меньше предыдущего
count = 0
for i in range(0, len(list_mcap_elements) - 1):  # последний элемент списка надо выводить отдельно
    elem_current = list_mcap_elements[i].text
    elem_next = list_mcap_elements[i + 1].text
    # условия для сравнения строк разной и одинаковой длины
    # len($146 109 484 586) > len($67 635 761 404) or "$67 635 761 404" > "$27 646 445 524"
    if len(elem_current) > len(elem_next) or elem_current > elem_next:
        count += 1
        print(count, elem_current)
    elif len(elem_current) < 3:
        count += 1
        print(count, elem_current)

print(count)

driver.close()
driver.quit()

# вывод:
# 1 $128 053 785 023
# 2 $59 693 845 610
# 3 $23 980 302 376
# ...
# 1620 $?
# 1621 $?
# 1622 $?
# 1623 $?
# 1623
