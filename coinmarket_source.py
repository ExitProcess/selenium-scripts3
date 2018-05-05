# скрипт для сравнения скорости работы с исходным кодом страницы, загруженным в оперативную память,
# против find_elements_by_xpath, т.е. через запросы к браузеру (coinmarket_xpath_v1.py)

import time
from selenium import webdriver
from lxml import html

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/all/views/all/")

execute_time = time.time()

source = driver.page_source
tree = html.fromstring(source)

num_list = tree.xpath("//tr/td[1]")  # \n1\n
name_list = tree.xpath("//tr/td[2]")
# symbol_list = tree.xpath("//tr/td[3]")  # ADA
mcap_list = tree.xpath("//tr/td[4]")  # '$9 649 627 724'

index = 0
for num in num_list:
    num = num.text[1:-1]  # \n1\n -->> 1

    name_str = name_list[index].text_content()  # \n\nXRP\nRiple\n
    name_str = name_str.strip("\n")  # XRP\nRiple
    str_divide = name_str.find('\n')

    name = name_str[str_divide+1:]
    symbol = name_str[:str_divide]

    mcap = mcap_list[index].text

    print(num, name, symbol, mcap)
    index += 1

execute_time = time.time() - execute_time
print(execute_time)

driver.close()
driver.quit()

# 0.5940341949462891
