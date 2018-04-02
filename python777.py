from selenium import webdriver
from selenium.webdriver.common.keys import Keys

queries = []
print("введите запрос и нажмите enter")
print("после добавления всех слов нажмите enter")
while True:
    query = input("запрос: ")
    if not query:  # если пустая строка то заканчиваем цикл
        break
    queries.append(query)

path='C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver=webdriver.Chrome(path)
results = dict()

for query in queries:
    driver.get("https://www.google.ru/")
    elem = driver.find_element_by_name("q")
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)
    elem2 = driver.find_element_by_id("resultStats")
    elem2 = elem2.text
    results[query]=elem2

print(results)
driver.close()
driver.quit()