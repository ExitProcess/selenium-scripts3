# отладочный скрипт для coinmarket_all_marketcap.py -- сравнение списков в нем выдает AssertionError
# причина в том, что в списках различаются id элементов для элементов "$?", см. вывод внизу

from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/all/views/all/")
# закрыть cookie-уведомление
cookie_close = driver.find_element_by_css_selector(".banner-alert-close [aria-hidden]")
cookie_close.click()

# сортировка по убыванию
sort_button = driver.find_element_by_css_selector("#th-marketcap")
sort_button.click()
# список элементов по убыванию
list_mcap_elements_dec = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements_dec[-1]

# сортировка по возрастанию
sort_button.click()
# список элементов по возрастанию
list_mcap_elements_inc = driver.find_elements_by_css_selector(".market-cap")
del list_mcap_elements_inc[-1]

list_mcap_elements_inc.reverse()

for i in range(len(list_mcap_elements_dec)):
    market_dec = list_mcap_elements_dec[i].text
    market_inc = list_mcap_elements_inc[i].text
    id_dec = list_mcap_elements_dec[i].id
    id_inc = list_mcap_elements_inc[i].id

    if market_dec == market_inc:
        print(i, market_dec, market_inc, id_dec, id_inc)
        continue
    print("+++ +++ +++", i, market_dec, market_inc)

driver.close()
driver.quit()

# 1352 $565 $565 0.797192536799955-1355 0.797192536799955-1355
# 1353 $554 $554 0.797192536799955-1356 0.797192536799955-1356
# 1354 $481 $481 0.797192536799955-1357 0.797192536799955-1357
# 1355 $18 $18 0.797192536799955-1358 0.797192536799955-1358
# 1356 $? $? 0.797192536799955-1359 0.797192536799955-1642
# 1357 $? $? 0.797192536799955-1360 0.797192536799955-1641
# 1358 $? $? 0.797192536799955-1361 0.797192536799955-1640
# 1359 $? $? 0.797192536799955-1362 0.797192536799955-1639
# ...
# 1635 $? $? 0.797192536799955-1638 0.797192536799955-1363
# 1636 $? $? 0.797192536799955-1639 0.797192536799955-1362
# 1637 $? $? 0.797192536799955-1640 0.797192536799955-1361
# 1638 $? $? 0.797192536799955-1641 0.797192536799955-1360
# 1639 $? $? 0.797192536799955-1642 0.797192536799955-1359
