# тест слайдера
# включает песню и фиксирует курсор на ползунке громкости
# в зависимости от времени воспроизведения, прибавляет громкость

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://soundcloud.com/linya-109923603/ne-tvoe-delo-ya-budu-ryadom")

# закрывает сообщение о кукисах
cookie_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        ".announcement__dismiss")))
cookie_close.click()

# ставит трек на рипит
repeat = driver.find_element_by_xpath("//button[@title='Repeat']")
repeat.click()

# наводит курсор на иконку громкости, чтобы появился ползунок
volume_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                 "//div[@class='volume__iconWrapper']")))
ActionChains(driver).move_to_element(volume_button).perform()

#slider = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
#                                            "//div[@class='volume__sliderHandle']")))
#ActionChains(driver).move_to_element(slider).perform()
#ActionChains(driver).click_and_hold(slider).perform()

def volume_down(x):
    while x > 0:
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        x -= 10

def volume_up(x):
    while x > 0:
        ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
        x -= 10

# с начала воспроизведения громкость устанавливается на 50%
ActionChains(driver).key_down(Keys.LEFT_SHIFT).perform()
volume_down(50)

# цикл проверяет время воспроизведения трека
# громкость на soundcloud регулируется shift+up, shift+down
# громкость установлена на 50%, на отметке 0:10 установится на 90%
seconds = 300
while seconds > 1:
    current_time = driver.find_element_by_css_selector('.playbackTimeline__timePassed [aria-hidden]')
    if current_time.text == "0:10":
        volume_up(40)
        ActionChains(driver).key_up(Keys.LEFT_SHIFT).perform()
        break
    print(current_time.text)
    seconds -= 1
    time.sleep(1)

pass