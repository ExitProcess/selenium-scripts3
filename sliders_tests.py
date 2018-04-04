from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://soundcloud.com/user-95923847/5-1")

#play = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
#                                        '//*[@id="content"]/div/div[4]/div/div[2]/div[2]/div/div/div[1]/a')))
#play.click()

cookie_close = WebDriverWait (driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                              ".announcement__dismiss")))
cookie_close.click()

repeat = driver.find_element_by_xpath("//button[@title='Repeat']")
repeat.click()