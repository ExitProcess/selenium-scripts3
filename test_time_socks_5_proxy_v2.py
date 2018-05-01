# парсилка SOCKS5 для телеграма -- версия с замерами времени
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом
# оптимизированная версия -- скрипт работает с исходным кодом страницы
# анализ 500 элементов и их вывод происходят за 0,004 секунды (в первой версии -- за 28-33 секунды)
# таким образом, эта часть кода ускорена в 7000-8000 раз
# общее время выполнения скрипта сократилось с 47-50 секунд до 11-13 секунд

import time
from selenium import webdriver
from selenium.webdriver.support import select
from lxml import html

all_time = time.time()

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

# SOCKS5
sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

# 500 элементов
sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

source = driver.page_source
tree = html.fromstring(source)

percents = tree.xpath("//tr/td[8]")
del percents[0]
del percents[0]
del percents[-1]

ip_ports = tree.xpath("//td/table/tbody/tr/td[1]")
del ip_ports[0]
del ip_ports[0]
del ip_ports[-1]

countries = tree.xpath("//tr/td[5]")
del countries[0]
del countries[0]
del countries[-1]

i = -1
analize_print_time = time.time()
for percent in percents:
    i += 1
    percent = percent.text_content()
    if percent[0:3] == "100":
        country = countries[i].text_content()
        ip_port = ip_ports[i].text_content()

        # 7 117.57.245.249document.write("&lt;font class=spy2&gt;:&lt;\/font&gt;"+(r8a1z6^x4i9)+(t0q7h8^o5e5)+
        # (y5w3o5^y5p6)+(t0q7h8^o5e5)):1080

        index1 = ip_port.find(" ")
        index2 = ip_port.find("document.write")
        ip = ip_port[index1 + 1:index2]

        index3 = ip_port.rfind(":")
        host = ip_port[index3:]

        print(ip + host, country, percent)

print("Анализ и печать -- %s seconds" % (time.time() - analize_print_time))
print("Работа скрипта -- %s seconds" % (time.time() - all_time))
driver.close()
driver.quit()

# Анализ и печать -- 0.004000186920166016 seconds
# Работа скрипта -- 11.883679628372192 seconds
#
# Анализ и печать -- 0.003999948501586914 seconds
# Работа скрипта -- 11.345648765563965 seconds
#
# Анализ и печать -- 0.004000186920166016 seconds
# Работа скрипта -- 13.487771272659302 seconds