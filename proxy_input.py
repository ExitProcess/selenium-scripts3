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
    # if i.tag_name == "option":, или другой вариант:
    # у radio строка text пустая, поэтому условие может быть таким:
    if i.text:
        country_list.append(i.text)
print(country_list)

def proxy_select(proxy_prot):
    proxy_type = driver.find_element_by_id("frmsearchFilter-protocol-" + str(proxy_prot))
    proxy_type.click()

def country_select(i):
    country_filter = driver.find_element_by_id("frmsearchFilter-country")
    select.Select(country_filter).select_by_visible_text(i)

def submit():
    submit_button = driver.find_element_by_id("frmsearchFilter-send")
    submit_button.click()

country = "any"

while country != "close":
    # можно со строчной, можно не полностью, например, "герм", "латв", "папуа" и т.д.
    country = input("страна: ")
    proxy_prot = input("тип прокси: все = 0, http = 1, https = 2, Socks 4/5 = 3, Socks 4 = 4, Socks 5 = 5: ")
    # австралия ->> Австралия
    country = country.capitalize()  # -> Bool
    if country:
        for i in country_list:
            if i.startswith(country) and proxy_prot:
                proxy_select(proxy_prot)
                country_select(i)
                submit()
            elif i.startswith(country):
                country_select(i)
                submit()
    elif not country:
        if proxy_prot:
            proxy_select(proxy_prot)
            submit()


# ограничения/баги:
# 1) не работают ЮАР и США
# 2) тип прокси должны быть от 0 до 6, исключение при любом другом значении
