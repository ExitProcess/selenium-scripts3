# парсилка https серверов
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом

from selenium import webdriver
from selenium.webdriver.support import select
from lxml import html

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

# http, https
sort_http = driver.find_element_by_id("xf5")
sort_http.click()
select.Select(sort_http).select_by_value("1")

# 500 элементов
sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

source = driver.page_source
tree = html.fromstring(source)

percents = tree.xpath("//tr/td[8]")  # 503
ip_ports = tree.xpath("//td/table/tbody/tr/td[1]")  # 503
countries = tree.xpath("//tr/td[5]")  # 503
http_types = tree.xpath("//tr/td[2]")  # 506

i = 1
for percent in percents:
    percent = percent.text_content()
    http_type = http_types[i + 1].text_content()

    if "100" in percent and "HTTPS" in http_type:
        country = countries[i-1].text_content()
        ip_port = ip_ports[i-1].text_content()

        # 7 117.57.245.249document.write("&lt;font class=spy2&gt;:&lt;\/font&gt;"+(r8a1z6^x4i9)+(t0q7h8^o5e5)+
        # (y5w3o5^y5p6)+(t0q7h8^o5e5)):1080

        index1 = ip_port.find(" ")
        index2 = ip_port.find("document.write")
        ip = ip_port[index1 + 1:index2]

        index3 = ip_port.rfind(":")
        host = ip_port[index3:]

        print(ip + host, country, percent, http_type)
    i += 1

driver.close()
driver.quit()
