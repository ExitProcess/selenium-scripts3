# скрипт заходит на сайт bbk, выбирает категорию "тв-ресиверы"
# затем парсит страницу с моделями, создает список всех элементов tag a, то есть cписок ссылок
# потом создается второй список, куда входят только ссылки на страницы моделей ресиверов
# из второго списка выбираются нужные нам модели, а именно 'SMP145HDT2' и 'SMP240HDT2'
# затем поочередно открываются страницы моделей, каждая добавляется в сравнение, после чего открывается страницы сравнения
# cкрипт неоптимизирован!!!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.bbk.ru/")

prod_button = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//a[@href='/production/']")))
ActionChains(driver).move_to_element(prod_button).perform()

recievers_button = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                                              "//a[@href='/production/tv_video/tv_receivers/']")))
ActionChains(driver).click(recievers_button).perform()

fffff = driver.find_element_by_xpath('//*[@id="add_fav_smp145hdt2"]')

ggggg = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[1]/div/div[4]')
pass
