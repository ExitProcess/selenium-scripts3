# парсилка SOCKS5 для телеграма
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом
# сравнение скорости работы xpath и сss
# алгоритм тот же что и в socks_5_proxy.py -- используется find_element_by, а не find_elements_by
# сравнение find_elements_by_xpath и css_selector будет потом

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

spy1x = ':nth-of-type('
percent_pos = ') [colspan="1"]:nth-of-type(8)'
ip_host_pos = ') [colspan="1"]:nth-of-type(1)'
country_pos = ') [colspan="2"]'

count_css = 0
css_loop = time.time()

for i in range(4, 502):
    percent = driver.find_element_by_css_selector(spy1x + str(i) + percent_pos)
    if percent.text[0:3] == "100":
        ip_host = driver.find_element_by_css_selector(spy1x + str(i) + ip_host_pos)
        country = driver.find_element_by_css_selector(spy1x + str(i) + country_pos)
        ip_host = ip_host.text
        index = ip_host.find(' ')
        print(ip_host[index + 1:], country.text, percent.text)
        count_css += 1

css_loop = time.time() - css_loop
print("CSS анализ и вывод -- %s seconds" % css_loop)
css = time.time() - css
print("CSS общее время -- %s seconds" % css)

xpath = time.time()

driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

count_xpath = 0
xpath_loop = time.time()

for str_count in range(4, 502):
    percents_xpath = "//tr[" + str(str_count) + "]/td[8]"
    percent_elem = driver.find_element_by_xpath(percents_xpath)

    if percent_elem.text[0:3] == "100":
        ip_port_xpath = "// tr[" + str(str_count) + "] / td[1]"
        ip_port_elem = driver.find_element_by_xpath(ip_port_xpath)
        ip_port_clear = ip_port_elem.text
        index = ip_port_clear.rfind(" ")

        country_xpath = "// tr[" + str(str_count) + "] / td[5]"
        country_elem = driver.find_element_by_xpath(country_xpath)

        print(ip_port_clear[index + 1:], country_elem.text, percent_elem.text)
        count_xpath += 1

print("найдено серверов перебором CSS: %s" % count_css)
print("найдено серверов перебором XPATH: %s" % count_xpath)

xpath_loop = time.time() - xpath_loop
print("XPATH анализ и вывод -- %s seconds" % xpath_loop)
xpath = time.time() - xpath
print("XPATH общее время -- %s seconds" % xpath)

driver.close()
driver.quit()
