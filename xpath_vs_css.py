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

all_css_time = time.time()

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

css_analize_time = time.time()
count_css = 0

for i in range(4, 502):
        percent = driver.find_element_by_css_selector(spy1x + str(i) + percent_pos) # :nth-of-type(4) :nth-of-type(8)
        if percent.text[0:3] == "100":
            ip_host = driver.find_element_by_css_selector(spy1x + str(i) + ip_host_pos)
            country = driver.find_element_by_css_selector(spy1x + str(i) + country_pos)
            ip_host = ip_host.text
            index = ip_host.find(' ')
            print(ip_host[index+1:], country.text, percent.text)
            count_css += 1

print("CSS анализ и вывод -- %s seconds" % (time.time() - css_analize_time))
print("CSS общее время -- %s seconds" % (time.time() - all_css_time))

all_xpath_time = time.time()

driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

count_xpath = 0
xpath_analize_time = time.time()

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

print("найдено серверов перебором CSS: ", count_css)
print("найдено серверов перебором XPATH: ", count_xpath)

print("XPATH анализ и вывод -- %s seconds" % (time.time() - xpath_analize_time))
print("XPATH общее время -- %s seconds" % (time.time() - all_xpath_time))

driver.close()
driver.quit()