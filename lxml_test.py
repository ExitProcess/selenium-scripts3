from selenium import webdriver
from selenium.webdriver.support import select
from lxml import html

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

source = driver.page_source
tree = html.fromstring(source)

percent_elems = tree.xpath("//tr/td[8]")

for x in percent_elems:
    x = x.text_content()
    if x[0:3] == "100":
        print(x)
