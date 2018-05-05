# скрипт для сравнения скорости find_elements_by_xpath, т.е. через запросы к браузеру,
# против работы с исходным кодом страницы, загруженным в оперативную память (coinmarket_source.py)

import time
from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/all/views/all/")

execute_time = time.time()

num_list = driver.find_elements_by_xpath("//tr/td[1]")
name_list = driver.find_elements_by_xpath("//tr/td[2]")
symbol_list = driver.find_elements_by_xpath("//tr/td[3]")
mcap_list = driver.find_elements_by_xpath("//tr/td[4]")

index = 0
for num in num_list:
    print(num.text, name_list[index].text, symbol_list[index].text, mcap_list[index].text)
    index += 1

execute_time = time.time() - execute_time
print(execute_time)

driver.close()
driver.quit()

# 272.20756936073303
