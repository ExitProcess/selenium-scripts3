from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://coinmarketcap.com")
# элемент сортировки рыночной стоимости
sort_button = driver.find_element_by_id("th-marketcap")

# 1 клик -- сортировка по убыванию
sort_button.click()
# список элементов, отсортированных по убыванию
list_mcap_elements_dec = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements_dec[-1]

# 2-ой клик -- сортировка по возрастанию
sort_button.click()
# список с элементами по возрастанию
list_mcap_elements_inc = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements_inc[-1]


# работа с list_mcap_elements_dec
# цикл проверяет, чтобы следующий элемент списка был меньше предыдущего
count = 0
for i in range(0, len(list_mcap_elements_dec) - 1):  # последний элемент списка надо выводить отдельно
    elem_current = list_mcap_elements_dec[i].text
    elem_next = list_mcap_elements_dec[i + 1].text
    # условие для сравнения строк разной длины ("$146 109 484 586 больше $67 635 761 404")
    if len(elem_current) > len(elem_next):
        count += 1
        print(elem_current)
    # условие для сравнения строк одинаковой длины ("$67 635 761 404 больше $27 646 445 524")
    if elem_current > elem_next:
        count += 1
        print(elem_current)
elem_last = list_mcap_elements_dec[-1].text
if elem_last < elem_current or len(elem_last) < len(elem_current):
    print(elem_last)
    count += 1

print(count)

# если 100 элементов расположены в списке по убыванию, то сортировка по убыванию работает
if count == 100:
    print("сортировка market cap по убыванию работает")


# работа с list_mcap_elements_inc
# вместо того чтобы проверять каждый элемент списка на возрастание,
# проще и быстрее перевернуть список и сравнить его со списком list_mcap_elements_dec
list_mcap_elements_inc.reverse()
if list_mcap_elements_inc == list_mcap_elements_dec:
    print("сортировка market cap по возрастанию работает")

driver.close()
driver.quit()
