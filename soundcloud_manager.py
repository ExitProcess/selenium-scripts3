"""Скрипт управляет воспроизведением на soundcloud через данные, которые получает от пользователя

Команды:
previous -- переключает на предыдущий трек
play -- вопроизведение текущего трека (не срабатывает, если трек уже воспроизводится)
pause -- пауза текущего трека (не срабатывает, если трек уже на паузе)
next -- переключает на следующий трек
shuffle -- перемешивание
repeat (track, all, none) -- повтор (трека, всех треков, без рипита)
volume (-30, 40) -- громкость (убавить на 30%, прибавить на 40%)
** можно вводить любые значения, например 55, -37 и т.д.: нижний разряд не затрагивается
*** скрипт научился обрабатывать любые значения, теперь не падает при play0, -, ---, -abcdef и подобных данных
**** теперь громкость прибавляется в диапазоне -100 <= x <= 100, т.о. нет долгих бесполезных циклов

"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://soundcloud.com/luna_official/jukebox")
# закрывает сообщение о кукисах
cookie_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                           ".announcement__dismiss")))
cookie_close.click()

# Циклы управления рипитом
# Состояния: 0 - нет повтора, 1 - повтор трека, 2 - повтор всех
repeat_counter = 0


def repeat_track():
    global repeat_counter
    if repeat_counter == 0:
        driver.find_element_by_css_selector(".playControls__repeat").click()
        repeat_counter = 1
    elif repeat_counter == 2:
        driver.find_element_by_css_selector(".playControls__repeat").click()
        time.sleep(1)
        driver.find_element_by_css_selector(".playControls__repeat").click()
        repeat_counter = 1


def repeat_all():
    global repeat_counter
    if repeat_counter == 1:
        driver.find_element_by_css_selector(".playControls__repeat").click()
        repeat_counter = 2
    elif repeat_counter == 0:
        driver.find_element_by_css_selector(".playControls__repeat").click()
        time.sleep(1)
        driver.find_element_by_css_selector(".playControls__repeat").click()
        repeat_counter = 2


def repeat_none():
    global repeat_counter
    if repeat_counter == 2:
        driver.find_element_by_css_selector(".playControls__repeat").click()
        repeat_counter = 0
    elif repeat_counter == 1:
        driver.find_element_by_css_selector(".playControls__repeat").click()
        time.sleep(1)
        driver.find_element_by_css_selector(".playControls__repeat").click()
        repeat_counter = 0


def manager():
    if user == "previous":
        driver.find_element_by_css_selector(".skipControl__previous").click()
    elif user == "play":
        play_button = driver.find_element_by_css_selector(".playControls__elements > [type]")
        if play_button.text == "Play current":
            play_button.click()
    elif user == "pause":
        play_button = driver.find_element_by_css_selector(".playControls__elements > [type]")
        if play_button.text == "Pause current":
            play_button.click()
    elif user == "next":
        driver.find_element_by_css_selector(".playControls__next").click()
    elif user == "shuffle":
        driver.find_element_by_css_selector(".playControls__shuffle").click()
    elif user == "repeat track":  # 1
        repeat_track()
    elif user == "repeat all":  # 2
        repeat_all()
    elif user == "repeat none":  # 0
        repeat_none()
    # если строка-в-число == True or начало строки == "-" (user[0]== "-")
    elif str.isdigit(user) or str.find(user, "-") == 0:
        # если строка в число без знака "-" == True (user[1:]==int) and диапазон -100 <= int(user) <= 100:
        if str.isdigit(user[1:]) and -100 <= int(user) <= 100:
            volume = int(user)  # строку в целое число
            if volume < 0:
                volume = -volume
                volume_down(volume)
            else:
                volume_up(volume)


def volume_up(y):
    while y >= 9:
        ActionChains(driver).key_down(Keys.LEFT_SHIFT).perform()
        ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
        ActionChains(driver).key_up(Keys.LEFT_SHIFT).perform()
        y -= 10


def volume_down(y):
    while y >= 9:
        ActionChains(driver).key_down(Keys.LEFT_SHIFT).perform()
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(driver).key_up(Keys.LEFT_SHIFT).perform()
        y -= 10


user = ""
while user != "close":
    user = input("запрос: ")
    manager()

driver.close()
driver.quit()
