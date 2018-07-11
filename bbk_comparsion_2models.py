# скрипт заходит на сайт bbk, выбирает категорию "тв-ресиверы"
# затем парсит страницу с моделями, создает список всех элементов tag a, то есть cписок ссылок
# потом создается второй список, куда входят только ссылки на страницы моделей ресиверов
# из второго списка выбираются нужные нам модели, а именно 'SMP145HDT2' и 'SMP240HDT2'
# затем поочередно открываются страницы моделей, каждая добавляется в сравнение,
# после чего открывается страница сравнения
# cкрипт неоптимизирован!!! в скрипте используется метод получения всех ссылок на странице

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.bbk.ru/")

prod_button = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH,
                                                                         "//a[@href='/production/']")))
ActionChains(driver).move_to_element(prod_button).perform()

recievers_button = WebDriverWait(driver, 4).until(ec.element_to_be_clickable((By.XPATH,
                                                                              "//a[@href='/production/tv_video"
                                                                              "/tv_receivers/']")))
ActionChains(driver).click(recievers_button).perform()

model_list = []  # список элементов моделей
# получаем все ссылки на странице
link_list = driver.find_elements_by_tag_name("a")  # список всех элементов со ссылками
# отбираем только ссылки, ведущие на модели ресиверов
for i in link_list:  # выбираем только элементы моделей, добавляем в model_list
    if len(i.text) == 10:
        model_list.append(i)
print(model_list)

a = "145"
b = "240"
a_link = ""
b_link = ""
# 145, 240
# 'SMP145HDT2', 'SMP240HDT2'

for i in model_list:
    if i.text[3:6] == a:
        print("найдена ссылка на модель ", a)
        a_link = i.get_attribute('href')
        print(a_link)
    if i.text[3:6] == b:
        print("найдена ссылка на модель ", b)
        b_link = i.get_attribute('href')
        print(b_link)

driver.get(a_link)
add_to_comp = WebDriverWait(driver, 4).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         ".add_to_comparsion")))
add_to_comp.click()
driver.get(b_link)
add_to_comp = WebDriverWait(driver, 4).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         ".add_to_comparsion")))
add_to_comp.click()

comparsion = WebDriverWait(driver, 4).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        ".compare")))
comparsion.click()

comparsion2 = WebDriverWait(driver, 4).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         ".compare_link")))
comparsion2.click()
