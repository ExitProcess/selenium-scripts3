# тест слайдера
# пока что включает бабангиду и фиксирует курсор на ползунке громкости

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

cookie_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        ".announcement__dismiss")))
cookie_close.click()

repeat = driver.find_element_by_xpath("//button[@title='Repeat']")
repeat.click()

volume_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                 "//div[@class='volume__iconWrapper']")))
ActionChains(driver).move_to_element(volume_button).perform()

slider = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            "//div[@class='volume__sliderHandle']")))

ActionChains(driver).move_to_element(slider).perform()
ActionChains(driver).click_and_hold(slider).perform()
pass