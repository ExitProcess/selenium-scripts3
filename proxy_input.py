# интерактивный скрипт
# input -- страна и тип прокси
# на сайте http://free-proxy.cz/ru/ скрипт выбирает страну и тип прокси, после чего применяет фильтр
# результат выводится в консоль

from selenium import webdriver
from selenium.webdriver.support import select

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://free-proxy.cz/ru/")

# текст элементов такой -- "Австралия (28)" и т.д., в скобках указано количество прокси для страны
# select будет работать по visible_text, а не по value ("AU" для Австралии)
# скрипт будет сравнивать пользовательский input страны с visible_text элемента, и в случае полного или частичного
#     совпадения, методу select будет передаваться "родной" visible_text
# создание списка всех элементов с селектором "value"

elements_list = driver.find_elements_by_css_selector("[value]")

# создание списка строк всех стран -- с этими строками будет сравниваться пользовательская строка
country_list = []
for i in elements_list:
    # элементы стран имеют тег "option" (в первом списке также есть элементы с тегом "input" (radio))
    # if i.tag_name == "option":
    # у radio строка text пустая, поэтому условие такое:
    if i.text:
        country_list.append(i.text)
print(country_list)

country = ""

while country != "close":
    country = input("страна:")
    # австралия ->> Австралия
    country = country.capitalize()

    for i in country_list:
        if i.startswith(country):
            country_filter = driver.find_element_by_id("frmsearchFilter-country")
            submit_button = driver.find_element_by_id("frmsearchFilter-send")
            select.Select(country_filter).select_by_visible_text(i)
            submit_button.click()
            break
