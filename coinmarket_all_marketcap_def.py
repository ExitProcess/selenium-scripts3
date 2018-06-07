# скрипт проверяет работу сортировки рыночной стоимости криптовалют на сайте
# https://coinmarketcap.com/all/views/all/
# также см. coinmarket_allmc_debug.py

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

count = 0


# функция для работы с list_mcap_elements_dec и list_mcap_elements_inc
# проверяет, чтобы следующий элемент списка был меньше предыдущего, кроме элементов "$?"
def check_decrement(elem_list):
    global count
    for index in range(0, len(elem_list)):  # последний элемент списка _не_ надо проверять вне цикла
        elem_current = elem_list[index].text
        try:
            elem_next = elem_list[index + 1].text
        except Exception:  # сработает, когда elem_current == list[-1], т.е. ссылается на последний элемент списка ($?)
            if elem_list[-1].text == "$?":
                count += 1
                print(count, elem_current)
                break
        # условия для сравнения строк разной и одинаковой длины
        # len($146 109 484 586) > len($67 635 761 404) or "$67 635 761 404" > "$27 646 445 524"
        if len(elem_current) > len(elem_next) or elem_current > elem_next:
            count += 1
            print(count, elem_current)
        elif len(elem_current) < 3:
            count += 1
            print(count, elem_current)
    return count


check_decrement(list_mcap_elements_dec)
assert count == len(list_mcap_elements_dec)
print("сортировка market cap по убыванию работает")

# перевернуть список с элементами, расположенными по возрастанию
list_mcap_elements_inc.reverse()
count = 0
# проверить получившийся список на убывание
check_decrement(list_mcap_elements_inc)
assert count == len(list_mcap_elements_inc)
print("сортировка market cap по возрастанию работает")

driver.close()
driver.quit()

# 1640 $?
# сортировка market cap по убыванию работает
# 1 $130 769 656 132
# ...
# 1639 $?
# 1640 $?
# сортировка market cap по возрастанию работает
#
# Process finished with exit code 0
