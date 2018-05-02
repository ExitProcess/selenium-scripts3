# парсилка SOCKS5
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом
# сравнение скорости работы xpath и сss (загрузка элементов в список и анализ списков)
# используется find_elements_by, а не find_element_by

import time
from selenium import webdriver
from selenium.webdriver.support import select

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

css = time.time()

driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

css_loop = time.time()
count_css = 0
i = 0

percent_list = driver.find_elements_by_css_selector('[colspan="1"]:nth-of-type(8)')  # 501; 1 не нужен
del percent_list[0]
ip_port_list = driver.find_elements_by_css_selector('[colspan="1"]:nth-of-type(1)')  # 501; 1 не нужен
del ip_port_list[0]
country_list = driver.find_elements_by_css_selector('[colspan="2"]')  # 502; 1 и 2 не нужны
del country_list[0]
del country_list[0]

for percent in percent_list:
    if percent.text[0:3] == "100":
        ip_port = ip_port_list[i].text
        index = ip_port.find(" ")
        print(ip_port[index+1:], country_list[i].text, percent.text)
        count_css += 1
    i += 1

css_loop = time.time() - css_loop
css = time.time() - css

print("#"*60)

xpath = time.time()

driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

xpath_loop = time.time()
count_xpath = 0
i = 0

percent_list = driver.find_elements_by_xpath('//tr/td[8]')  # 503; 1, 2 и 503 не нужны
del percent_list[0]
del ip_port_list[0]
del ip_port_list[-1]
ip_port_list = driver.find_elements_by_xpath('//td/table/tbody/tr/td[1]')  # 503, 1, 2 и 503 не нужны
del percent_list[0]
del ip_port_list[0]
del ip_port_list[-1]
country_list = driver.find_elements_by_xpath('//tr/td[5]')  # 503; 1, 2 и 503 не нужны
del percent_list[0]
del ip_port_list[0]
del ip_port_list[-1]

for percent in percent_list:
    if percent.text[0:3] == "100":
        ip_port = ip_port_list[i].text
        index = ip_port.find(" ")
        print(ip_port[index+1:], country_list[i].text, percent.text)
        count_xpath += 1
    i += 1

xpath_loop = time.time() - xpath_loop
xpath = time.time() - xpath

print("#"*60)

print("найдено серверов по CSS: %s" % count_css)
print("найдено серверов по XPATH: %s" % count_xpath)

print("CSS: поиск элементов, создание списков, анализ и вывод -- %s sec" % css_loop)
print("CSS: время выполнения -- %s sec" % css)

print("XPATH: поиск элементов, создание списков, анализ и вывод -- %s sec" % xpath_loop)
print("XPATH: время выполнения -- %s sec" % xpath)

if css_loop < xpath_loop:
    print("поиск элементов по CSS, создание списков, анализ и вывод быстрее XPATH на %s sec" % (xpath_loop - css_loop))
else:
    print("поиск элементов по XPATH, создание списков, анализ и вывод быстрее CSS на %s sec" % (css_loop - xpath_loop))

driver.close()
driver.quit()

# найдено серверов по CSS: 63
# найдено серверов по XPATH: 63
# CSS: поиск элементов, создание списков, анализ и вывод -- 14.020801782608032 sec
# CSS: время выполнения -- 31.150781631469727 sec
# XPATH: поиск элементов, создание списков, анализ и вывод -- 13.977799892425537 sec
# XPATH: время выполнения -- 21.514230966567993 sec
# поиск элементов по XPATH, создание списков, анализ и вывод быстрее CSS на 0.04300189018249512 sec
#
# поиск элементов по XPATH, создание списков, анализ и вывод быстрее CSS на 0.2110121250152588 sec
#
# поиск элементов по XPATH, создание списков, анализ и вывод быстрее CSS на 0.010000228881835938 sec
