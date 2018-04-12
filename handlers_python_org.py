from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.python.org/")

doc_button = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                             "#documentation")))
ActionChains(driver).move_to_element(doc_button).perform()


button_3_x = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,
                                                                             "Python 3.x Docs")))
ActionChains(driver).click(button_3_x).perform()


lib_ref = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT,
                                                                    "Library Reference")))
ActionChains(driver).move_to_element(lib_ref).perform()
ActionChains(driver).key_down(Keys.LEFT_CONTROL).click().perform()
ActionChains(driver).key_up(Keys.LEFT_CONTROL).perform()


tutorial = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,
                                                                      "Tutorial")))
ActionChains(driver).click(tutorial).perform()
window_handles = driver.window_handles


tutorial_handle = window_handles[0]
library_handle = window_handles[1]

i = 50
while i > 0:
    driver.switch_to_window(library_handle)
    driver.switch_to_window(tutorial_handle)
    i -= 1