from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://coinmarketcap.com")
# закрыть cookie-уведомление
cookie_close = driver.find_element_by_css_selector(".banner-alert-close [aria-hidden]")
cookie_close.click()

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
# цикл проверяет, чтобы текущий элемент был больше следующего
count = 0
for i in range(0, len(list_mcap_elements_dec)):
    elem_current = list_mcap_elements_dec[i].text

    try:
        elem_next = list_mcap_elements_dec[i + 1].text
    except Exception:  # elem_current указывает на последний элемент [-1], соот-но next выйдет за границу
        elem_penultimate = list_mcap_elements_dec[-2].text  # предпоследний элемент в списке
        if elem_penultimate > elem_current or len(elem_penultimate) > len(elem_current):
            print(elem_current)
            count += 1

    # условия для сравнения строк разной и одинаковой длины
    # len($146 109 484 586) > len($67 635 761 404) or "$67 635 761 404" > "$27 646 445 524"
    if len(elem_current) > len(elem_next) or elem_current > elem_next:
        count += 1
        print(elem_current)

print(count)

# если 100 элементов расположены в списке по убыванию, то сортировка по убыванию работает
assert count == 100
print("сортировка market cap по убыванию работает")

# работа с list_mcap_elements_inc
# вместо того чтобы проверять каждый элемент списка на возрастание,
# проще и быстрее перевернуть список и сравнить его со списком list_mcap_elements_dec
list_mcap_elements_inc.reverse()
assert list_mcap_elements_inc == list_mcap_elements_dec
print("сортировка market cap по возрастанию работает")

driver.close()
driver.quit()


