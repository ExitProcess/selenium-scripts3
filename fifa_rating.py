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

# rnk - локатор
rnk = "rnk_1"
rnk_inc = 1
while rnk_inc < 212:
    position = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,
                                                                          rnk)))
    results = position.text
    i = results.rfind(")")
    print(results[0:i+1])

    rnk_inc += 1
    rnk = rnk[0:4]+str(rnk_inc)
pass
