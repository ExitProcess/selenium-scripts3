# парсилка SOCKS5 для телеграма
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import select

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
# если аптайм сервака == 100%, то выводим на печать ip:port и страну
# "//tbody/tr[4]" - "//tbody/tr[503]" -- столько всего строк
for str_count in range(4, 503):

    str_xpath = "//tbody/tr[" + str(str_count) + "]"
    str_elem = driver.find_element_by_xpath(str_xpath)

    percents_xpath = "//tr[" + str(str_count) + "]/td[8]"
    percent_elem = driver.find_element_by_xpath(percents_xpath)

    if percent_elem.text[0:3] == "100":

        ip_port_xpath = "// tr[" + str(str_count) + "] / td[1]"
        ip_port_elem = driver.find_element_by_xpath(ip_port_xpath)

        country_xpath = "// tr[" + str(str_count) + "] / td[5]"
        country_elem = driver.find_element_by_xpath(country_xpath)

        print(ip_port_elem.text, country_elem.text, percent_elem.text)

pass
