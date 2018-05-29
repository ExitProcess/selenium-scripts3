"""Скрипт управляет скроллбаром на soundcloud через данные, которые получает от пользователя

формат -- -0:30 -- через actionchains перематывает назад на 0:30 секунд
       --  0:30 -- через actionchains перематывает вперед на 0:30 секунд

*** данные от пользователя не обрабатываются.
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://soundcloud.com/luna_official/jukebox")
# закрывает сообщение о кукисах
cookie_close = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                          ".announcement__dismiss")))
cookie_close.click()


def manager():
    # наводит на скроллбар, чтобы появился хендл перемотки
    progressbar = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                             '.playbackTimeline__progressBar')))
    ActionChains(driver).move_to_element(progressbar).perform()

    # захват хендла перемотки
    global handle
    handle = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        '.playbackTimeline__progressHandle')))
    ActionChains(driver).click_and_hold(handle).perform()

    # получение текущего времени воспроизведения
    current_time = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                              '.playbackTimeline__timePassed [aria-hidden]')))
    current_time_sec = int(current_time.text[0]) * 60 + int(current_time.text[2:4])
    print(current_time_sec)

    if str.isdigit(user[0]):
        # полученные от пользователя данные
        user_seconds = int(user[0]) * 60 + int(user[2:4])
        print(user_seconds)

        # текущее время + время от пользователя
        all_time_sec = current_time_sec + user_seconds
        print(all_time_sec)

        while all_time_sec > current_time_sec:
            ActionChains(driver).move_by_offset(1, 0).perform()
            current_time = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                      '.playbackTimeline__timePassed [aria-hidden]')))
            current_time_sec = int(current_time.text[0]) * 60 + int(current_time.text[2:4])
    else:
        user_seconds = int(user[1]) * 60 + int(user[3:5])
        print("-", user_seconds)
        all_time_sec = current_time_sec - user_seconds
        if all_time_sec < 0:
            driver.find_element_by_css_selector(".skipControl__previous").click()
        else:
            while current_time_sec > all_time_sec:
                ActionChains(driver).move_by_offset(-1, 0).perform()
                current_time = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                          '.playbackTimeline__timePassed [aria-hidden]')))
                current_time_sec = int(current_time.text[0]) * 60 + int(current_time.text[2:4])


user = ""
while user != "close":
    user = input("-x:xx - перемотать назад, x:xx -- перемотать вперед: ")
    manager()
    ActionChains(driver).release(handle).perform()

driver.close()
driver.quit()
