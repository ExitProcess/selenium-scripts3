# вывод рейтинга fifa сборных
# выводит все 211 команд

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.fifa.com/")
ranking = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,
                                                                     "WORLD RANKING")))
ranking.click()

more = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                  '[title="201-211"] span')))
ActionChains(driver).move_to_element(more).perform()
time.sleep(2)
ActionChains(driver).click(more).perform()

list = []
for rnk_inc in range(1, 212):
    rnk = "rnk_" + str(rnk_inc)
    list.append(rnk)

# rnk - локатор
for x in range(0, 211):
#    position = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,
#                                                                          rnk)))
    position = driver.find_element_by_id(list[x])
    results = position.text
    i = results.rfind(")")
    print(results[0:i + 1])

pass
