# вывод рейтинга fifa сборных
# пока только первые 50 команд, будут все 211 команд

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.fifa.com/")
ranking = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,
                                                                     "WORLD RANKING")))
ranking.click()

n = 211
rnk = "rnk_1"
rnk_inc = 1
while n > 0:
    position = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,
                                                                          rnk)))
    results = position.text
    i = results.rfind(")")
    print(results[0:i+1])

    rnk_inc += 1
    rnk = rnk[0:4]+str(rnk_inc)
pass
