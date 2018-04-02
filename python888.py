from selenium import webdriver
from selenium.webdriver.common.keys import Keys

languages = {"C programming language": 0,
             "C++": 0,
             "Python programming language": 0,
             "Assembly language": 0
             }

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

for language in languages:
    driver.get("https://www.google.ru/")
    elem = driver.find_element_by_name("q")
    elem.send_keys(language)
    elem.send_keys(Keys.RETURN)
    elem2 = driver.find_element_by_id("resultStats")
    elem2 = elem2.text
    languages[language] = elem2

print(languages)
driver.close()
driver.quit()
