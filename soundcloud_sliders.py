# скрипт включает на рипит трек на саундклауде, прибавляет громкость до 75%
# когда трек доходит до 3:00, громкость прибавляется до 95%

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://soundcloud.com/")
WebDriverWait(driver, 5)
search = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH,
                                             '//*[@id="content"]/div/div/div[2]/div/div[1]/span/form/input')))
search.click()
search.send_keys("ласковый май белые розы")
search.send_keys(Keys.RETURN)
kategory = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH,
                                               "//a[@class='resultCounts__link sc-link-light']")))
kategory.click()
results = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        '.resultCounts')))
print(results.text)
assert "tracks" in results.text

play = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                        '//html//li[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]')))
play.click()

cookie_close = WebDriverWait (driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                              ".announcement__dismiss")))
cookie_close.click()

repeat = driver.find_element_by_xpath("//button[@title='Repeat']")
repeat.click()

volume_button = driver.find_element_by_xpath("//div[@class='volume__iconWrapper']")
ActionChains(driver).move_to_element(volume_button).perform()

volume_slider = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div[@class='volume__sliderHandle']")))
ActionChains(driver).click_and_hold(volume_slider)
pass
