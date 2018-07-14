# прототип линк-чекера -- скрипта, который ищет ссылки на сайте (в данном случае -- python.org) и переходит по ним
#
# алгоритм:
# 0. зайти на главную страницу сайта
# 1. получить со страницы все ссылки (в список urls_list_from_page), которые удовлетворяют заданным условиям
# 2. из списка urls_list_from_page создать список с уникальными ссылками (unique_urls_list_from_page)
# 3. проверить, есть ли уникальная ссылка в базе ссылок
#    3.1 если ссылки нет, добавить ее в базу и проставить ей статус 0
#     статусы для ссылок --   0 - не проверено;
#                             1 - успех, получены другие ссылки;
#                             2 - успех, других ссылок нет;
#                             3 - неудача, т.е. битая
#                             4 - прямая ссылка на скачивание с ftp
# 4. перейти по следующей ссылке из базы
# 5. повторить шаг 1
# 6. если получены другие ссылки, то:
#    6.1 проставить значение 1 ссылке, по которой был произведен переход (1 - успех, со страницы получены ссылки)
#    6.2 повторить шаги 2, 3, 3.1, 4
# 7. если страница открылась, но ссылок на ней не обнаружено, то:
#    7.1 проставить значение 2 ссылке, по которой был произведен переход (2 - успех, на странице нет ссылок)
#    7.2 повторить шаги 2, 3, 3.1, 4
# 8. если страница не открылась, то:
#    8.1 проставить значение 3 ссылке, по которой был произведен переход (3 - неудача, битая ссылка)
#    8.2 повторить шаги 2, 3, 3.1, 4
# 9. выполнять шаги 1-8 до тех пор, пока есть ссылки со статусом 0

from selenium import webdriver

driver = webdriver.Chrome('C:\SeleniumDrivers\Chrome\chromedriver.exe')

# база ссылок, стартовая страница находится в списке изначально
# https://www.python.org/11111/ добавлена для тестирования
url_base = ["https://python.org/", "https://www.python.org/11111/", ]
# список для результатов (0, 1, 2 или 3, подробности в описании алгоритма)
url_base_result = [0, 0, ]
index = 0
# список битых ссылок
base_404 = []

while 0 in url_base_result:  # выполнять, пока есть ссылки, по которым не было перехода
    # обработка ссылок с "ftp" в адресе -- перехода по ним не происходит, такая ссылка отмечается значением "4" в базе
    if "ftp" in url_base[index]:
        url_base_result[index] = 4
        index += 1
        continue

    driver.get(url_base[index])

    try:
        driver.find_element_by_css_selector(".giga") # локатор "Error 404"
        base_404.append(url_base[index])
        print(url_base[index])
        url_base_result[index] = 3
        index += 1
        continue
    except Exception:
        pass

    urls_list_from_page = []  # временный список для всех ссылок с текущей страницы (url_base[index])

    elements_list_from_page = driver.find_elements_by_tag_name("a")  # список для элементов с тегом "а"
    for elem in elements_list_from_page:
        try:  # если не удалось получить атрибут, то просто перейти к следующему элементу
            url = elem.get_attribute('href')
        except Exception:
            pass

        # фильтрация ссылок: не проверяются внешние сайты, подсайты -- docs.python.org и прочие
        # игнорируются ссылки внутри страницы (https://www.python.org/about/success/#software-development)
        if "www.python.org" in str(url) and "#" not in str(url) and "web.archive.org" not in str(url):
            urls_list_from_page.append(url)

    unique_urls_list_from_page = list(set(urls_list_from_page))  # временный список для уникальных ссылок

    for unique_url in unique_urls_list_from_page:  # наполнение базы
        if unique_url not in url_base:
            url_base.append(unique_url)  # добавить в базу уникальную ссылку
            url_base_result.append(0)  # по уникальной ссылке не было перехода, значит статус 0

    # вывод отладочной информации
    print(len(url_base), "всего ссылок в базе")
    print(len(url_base_result), "всего результатов в базе")

    print(url_base_result.count(3), "битых ссылок в базе")
    print(base_404)

    #print(url_base)
    #print(url_base_result)

    # статус ссылки -- пока заглушка, потом будут проверки для выставления точного статуса
    url_base_result[index] = 1
    # переход к следующей ссылке в базе
    index += 1

driver.close()
driver.quit()

# скрипт нашел 352 битых ссылок, в основном это ссылки на цифровые подписи старых дистрибутивов python, например:
# https://www.python.org/download/releases/2.5.1/python-2.5.1.ia64.msi.asc
# https://www.python.org/download/releases/2.7.2/Python-2.7.2.tar.bz2.asc
# и т.д.
# также есть такие ссылки
# http://www.python.org/2006/cfp
# http://www.python.org/workshops/oscon2002
# https://www.python.org/community/index.html
# 
# все результаты:
# https://github.com/ExitProcess/other_scripts/blob/master/broken_links.py
# https://github.com/ExitProcess/other_scripts/blob/master/base_404.txt
# 
# в link_test_v2.py будет использоваться SQLite, а также requests и lxml
# в бд будет сохраняться информация о родительской ссылке
