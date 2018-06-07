# скрипт проверяет работу сортировки рыночной стоимости криптовалют на сайте
# https://coinmarketcap.com/all/views/all/
# AssertionError срабатывает из-за причины, найденной в coinmarket_allmc_debug.py
# AssertionError исправлен, теперь сравнение списков проходит успешно

from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/all/views/all/")
# закрыть cookie-уведомление
cookie_close = driver.find_element_by_css_selector(".banner-alert-close [aria-hidden]")
cookie_close.click()

# сортировка по убыванию
sort_button = driver.find_element_by_css_selector("#th-marketcap")
sort_button.click()
# список элементов по убыванию
list_mcap_elements_dec = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements_dec[-1]

# сортировка по возрастанию
sort_button.click()
# список элементов по возрастанию
list_mcap_elements_inc = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements_inc[-1]

# работа с list_mcap_elements_dec
# цикл проверяет, чтобы следующий элемент списка был меньше предыдущего
count = 0
na_count = 0
for i in range(0, len(list_mcap_elements_dec)):  # последний элемент списка _не_ надо проверять вне цикла; обработка Try
    elem_current = list_mcap_elements_dec[i].text
    try:
        elem_next = list_mcap_elements_dec[i + 1].text
    except Exception:  # сработает, когда elem_current == list[-1], т.е. ссылается на последний элемент списка ($?)
        if list_mcap_elements_dec[-1].text == "$?":
            count += 1
            na_count += 1  # последний элемент "$?"
            print(count, elem_current)
            break
    # условия для сравнения строк разной и одинаковой длины
    # len($146 109 484 586) > len($67 635 761 404) or "$67 635 761 404" > "$27 646 445 524"
    if len(elem_current) > len(elem_next) or elem_current > elem_next:
        count += 1
        print(count, elem_current)
    elif len(elem_current) < 3:
        count += 1
        na_count += 1  # подсчет элементов "$?"
        print(count, elem_current)

print(count)

assert count == len(list_mcap_elements_dec)
print("сортировка market cap по убыванию работает")

# подготовка списка list_mcap_elements_inc для сравнения его с list_mcap_elements_dec
new_list_inc = []
for i in range(0, na_count):
    new_list_inc.append(list_mcap_elements_inc.pop(0))

new_list_inc.reverse()

new_list_inc.extend(list_mcap_elements_inc)
new_list_inc.reverse()

assert new_list_inc == list_mcap_elements_dec
print("сортировка market cap по возрастанию работает")

driver.close()
driver.quit()

# вывод:
# 1 $128 053 785 023
# 2 $59 693 845 610
# 3 $23 980 302 376
# ...
# 1621 $?
# 1622 $?
# 1623 $?
# 1624 $?
# 1624
# сортировка market cap по убыванию работает
# Traceback (most recent call last):
#  File "C:/Users/alexey/PycharmProjects/selenium-scripts3/coinmarket_all_marketcap.py", line 49, in <module>
#    assert list_mcap_elements_inc == list_mcap_elements_dec
# AssertionError
# +
# см. coinmarket_allmc_debug.py
#
# 03.06.2018, сравнение списков поправлено
# 1638 $?
# 1639 $?
# 1639
# сортировка market cap по убыванию работает
# сортировка market cap по возрастанию работает
#
# Process finished with exit code 0
