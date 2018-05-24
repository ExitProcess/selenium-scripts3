import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.fifa.com/fifa-world-ranking/ranking-table/men/index.html")

# вывод сразу всех стран
# после нажатия на 201-211, страница прокручивается вниз
button_211 = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="201-211"] span')))
ActionChains(driver).move_to_element(button_211).perform()
time.sleep(2)
ActionChains(driver).click(button_211).perform()

# move_to_element - не работает
# elem2 = driver.find_element_by_id("rnk_2")
# elem2 = driver.find_element_by_xpath("//tbody/tr[3]/td[3]/a")
# ActionChains(driver).move_to_element(elem2).perform()

# перемотка с помощью scrollIntoView
elem2 = driver.find_element_by_xpath("//tbody/tr[2]/td[3]/a")
driver.execute_script("arguments[0].scrollIntoView();", elem2)

driver.close()
driver.quit()
