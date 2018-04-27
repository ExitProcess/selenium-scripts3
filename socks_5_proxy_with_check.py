# дополненная версия скрипта socks_5_proxy.py
# на первой стадии работает точно также: собирает socks5 с лучшим аптаймом с сайта spys.one
# после формирования списка прокси, скрипт идет на hidemy.name/ru/proxy-checker/
# список загружается в чекер, после чего начинается проверка
# таким образом, пользователь может выбрать прокси, доступный в данный момент

from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.common.keys import Keys

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

# вначале отсортируем по SOCKS5, а только потом отобразим все
sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

# отобразим на странице 500 элементов
sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

# теперь парсим строки, выбираем сервера со 100% аптаймом
# если аптайм сервака == 100%, то выводим на печать ip:port, страну, аптайм сервака + (количество проверок)
# "//tbody/tr[4]" - "//tbody/tr[503]" -- столько всего строк
proxy_list = []
for str_count in range(4, 503):
    # локатор аптайма
    percents_xpath = "//tr[" + str(str_count) + "]/td[8]"
    percent_elem = driver.find_element_by_xpath(percents_xpath)

    if percent_elem.text[0:3] == "100":
        # локатор ip:port + получение индекса начала текста ip:port
        ip_port_xpath = "// tr[" + str(str_count) + "] / td[1]"
        ip_port_elem = driver.find_element_by_xpath(ip_port_xpath)
        ip_port_clear = ip_port_elem.text
        index = ip_port_clear.rfind(" ")

        country_xpath = "// tr[" + str(str_count) + "] / td[5]"
        country_elem = driver.find_element_by_xpath(country_xpath)

        print(ip_port_clear[index + 1:], country_elem.text, percent_elem.text)

        # формируем список, который потом будет загружен на чекер hidemy.name/ru/proxy-checker/
        proxy_list.append(ip_port_clear[index + 1:])

# открываем чекер hidemy.name/ru/proxy-checker/
driver.get("https://hidemy.name/ru/proxy-checker/")
form = driver.find_element_by_id("f_in")

for i in proxy_list:
    form.send_keys(i)
    form.send_keys(Keys.RETURN)

check = driver.find_element_by_id("chkb1")
check.click()