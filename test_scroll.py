from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://soundcloud.com/luna_official/jukebox")
# закрывает сообщение о кукисах
cookie_close = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                          ".announcement__dismiss")))
cookie_close.click()


progressBar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                             '.playbackTimeline__progressBar')))
ActionChains(driver).move_to_element(progressBar).perform()


handle = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        '.playbackTimeline__progressHandle')))
ActionChains(driver).click_and_hold(handle).perform()

current_time = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                          '.playbackTimeline__timePassed [aria-hidden]')))
current = current_time.text
print(current_time.text)

a = "59"
while  a > current_time.text[2:4]:
    ActionChains(driver).move_by_offset(1, 0).perform()
    current_time = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                               '.playbackTimeline__timePassed [aria-hidden]')))
ActionChains(driver).release(handle).perform()