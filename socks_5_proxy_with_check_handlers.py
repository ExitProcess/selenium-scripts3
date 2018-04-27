# написано в учебных целях -- получение некоего значения на одном сайте(вкладке) и передача значения в форму
#   на другом сайте(открытым во второй вкладке) -- хендлы и т.д.
#
# скрипт собирает socks5 с лучшим аптаймом с сайта spys.one
# после каждого найденного прокси со 100% аптаймом, скрипт переходит на hidemy.name/ru/proxy-checker/
#     и загружает в чекер ip:host по одному
#

from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

# подготовка второй вкладки
# ctrl + лкм по любому элементу
# (ctrl + T не работает, проблема описана в test_ctrl_t.py)
temp_elem = driver.find_element_by_link_text("SPYS.ONE © 2008-2018")
ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(temp_elem).key_up(Keys.LEFT_CONTROL).perform()

# получение списка хендлов
handles_list = driver.window_handles
spys_tab = handles_list[0]
hide_tab = handles_list[1]

# переключение на вторую вкладку, переход на hidemy, возврат на spys.one
driver.switch_to.window(hide_tab)
driver.get("https://hidemy.name/ru/proxy-checker/")
form = driver.find_element_by_id("f_in")
driver.switch_to.window(spys_tab)

# сортировка по SOCKS5
sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

# отображение всех прокси на странице
sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

# теперь парсим строки, выбираем сервера со 100% аптаймом
# если аптайм сервака == 100%, то выводим на печать ip:port, страну, аптайм сервака + (количество проверок)
# "//tbody/tr[4]" - "//tbody/tr[503]" -- столько всего строк

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

        # переключение на hidemy и передача ip:host туда

        driver.switch_to.window(hide_tab)
        form.send_keys(ip_port_clear[index + 1:])
        form.send_keys(Keys.RETURN)
        driver.switch_to.window(spys_tab)


driver.switch_to.window(hide_tab)
check = driver.find_element_by_id("chkb1")
check.click()
