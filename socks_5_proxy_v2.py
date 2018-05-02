# парсилка SOCKS5 для телеграма
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом
# оптимизированная версия -- скрипт работает с исходным кодом страницы
# анализ 500 элементов и их вывод происходят за 0,004 секунды (в первой версии -- за 28-33 секунды)
# таким образом, эта часть кода ускорена в 7000-8000 раз
# общее время выполнения скрипта сократилось с 47-50 секунд до 11-13 секунд

from selenium import webdriver
from selenium.webdriver.support import select
from lxml import html

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

ip_ports = tree.xpath("//td/table/tbody/tr/td[1]")

countries = tree.xpath("//tr/td[5]")

i = 1
for percent in percents[2:-1]:
    i += 1
    percent = percent.text_content()
    if "100" in percent:
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

driver.close()
driver.quit()
