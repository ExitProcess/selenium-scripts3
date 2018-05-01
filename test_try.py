# работа с исключениями
#
#

from selenium import webdriver
from selenium.webdriver.support import select

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

spy1x = 'body .spy1x:nth-of-type('
spy1xx = 'body .spy1xx:nth-of-type('
percent_pos = ') [colspan="1"]:nth-of-type(8)'
ip_host_pos = ') [colspan="1"]:nth-of-type(1)'
country_pos = ') [colspan="2"]'

for i in range(4, 502):
    try:
        percent = driver.find_element_by_css_selector(spy1x + str(i) + percent_pos)
    except Exception:
        percent = driver.find_element_by_css_selector(spy1xx + str(i) + percent_pos)

    if percent.text[0:3] == "100":
        try:
            ip_host = driver.find_element_by_css_selector(spy1x + str(i) + ip_host_pos)
            country = driver.find_element_by_css_selector(spy1x + str(i) + country_pos)
        except Exception:
            ip_host = driver.find_element_by_css_selector(spy1xx + str(i) + ip_host_pos)
            country = driver.find_element_by_css_selector(spy1xx + str(i) + country_pos)
        ip_host = ip_host.text
        index = ip_host.find(' ')
        print(ip_host[index+1:], country.text, percent.text)
pass
