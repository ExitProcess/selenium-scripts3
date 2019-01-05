# линк-чекер python.org
# формирует две таблицы: таблицу со ссылками и кодами состояния, и таблицу всех ссылок на каждой странице

import time
import sqlite3
import urllib.error
import urllib.request

from lxml import html

# переменные
# список прокси
proxies = ['178.46.188.202:39864',
           '195.9.33.178:31978',
           '46.146.213.153:45768',
           '95.161.158.178:61833',
           '176.215.170.147:35604',
           '109.75.140.158:59916',
           '194.135.246.178:42010',
           '176.118.132.2:30894'
           ]
# счетчик
count = 0
last_id = 1
time1 = 0
time2 = 0


# переключение прокси
def proxy_handler(x):
    proxy_support = urllib.request.ProxyHandler({'https': x})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)


# выбор самого быстрого прокси
def select_fast_proxy():
    proxy_response = []
    for proxy in proxies:
        try:
            proxy_handler(proxy)
            start = time.time()
            urllib.request.urlopen('https://www.python.org/')
            finish = time.time() - start
            proxy_response.append(finish)
        except Exception:
            proxy_response.append(99.99)

    fast_proxy_index = proxy_response.index(min(proxy_response))
    print(proxies[fast_proxy_index], proxy_response[fast_proxy_index])
    return fast_proxy_index


# подключение к базе данных
con = sqlite3.connect("links_v3.4.db")
# начало работы с базой данных, создание таблиц
with con:
    cur = con.cursor()
    # удаление старых таблиц, если они существуют
    cur.execute("DROP TABLE IF EXISTS Links")
    cur.execute("DROP TABLE IF EXISTS Parent_child")
    # создание таблиц
    cur.execute("CREATE TABLE Links(Id INTEGER PRIMARY KEY, Link TEXT, HTTP_status_code INT)")
    cur.execute("CREATE TABLE Parent_child(Id INTEGER PRIMARY KEY, Parent_link INT, Child_link INT)")
    # добавление стартовой записи
    cur.execute("INSERT INTO Links(Link, HTTP_status_code) VALUES ('https://www.python.org/', 0)")

while count < last_id:
    try:
        # выбор первой записи, где HTTP status code = 0 (т.е. получение первой ссылки, по которой не было перехода)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Links WHERE HTTP_status_code=0 LIMIT 1")
            rows = cur.fetchall()  # <class 'list'>: [(1, 'https://www.python.org', 0, 0)]
            rows_list = list(rows[0])  # <class 'list'>: [1, 'https://www.python.org', 0, 0]

        # столбцы Link и Id первой строки, где HTTP status code = 0
        first_not_parsed_link = rows_list[1]  # 'https://www.python.org'
        first_not_parsed_link_id = rows_list[0]  # 1

        # HTTP-запрос к выбранной странице
        print("переход по ссылке: %s" % first_not_parsed_link)  # выводится для отладки
        response = urllib.request.urlopen(first_not_parsed_link)

    # обработчик ошибок HTTP
    except urllib.error.HTTPError as error:
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Links SET HTTP_status_code = ? WHERE Id = ?", (error.code, first_not_parsed_link_id))

    except urllib.error.URLError as error:  # обычно [WinError 10060]
        # [WinError 10054] Удаленный хост принудительно разорвал существующее подключение
        print(error.reason)
        print("выбор самого быстрого прокси-сервера")
        fast_proxy_index = select_fast_proxy()
        proxy_handler(proxies[fast_proxy_index])
        count -= 1

    except UnicodeEncodeError:  # обработка unicode-ссылок (заглушка), ссылки наподобие
        # https://www.python.org/events/python-events/553/“https:/pydata.org/delhi2017“
        # unicode-ссылкам проставляется http-status 999, позже будет нормальный обработчик (на urllib.parse)
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Links SET HTTP_status_code = ? WHERE Id = ?", (999, first_not_parsed_link_id))

    else:
        # обновление записи, когда http-статус = 200
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Links SET HTTP_status_code = ? WHERE Id = ?",
                        (response.getcode(), first_not_parsed_link_id))

        # парсинг ссылок с текущей страницы
        tree = html.fromstring(response.read())
        tree.make_links_absolute(response.geturl(), resolve_base_href=False)
        links = tree.xpath('//a/@href')

        # формирование списка ссылок, которые будут добавлены в таблицы
        # в таблицу Links добавляются только ссылки на www.python.org. не добавляются:
        # подсайты и сторонние сайты ('https://docs.python.org/', 'http://twitter.com/ThePSF')
        # ссылки с якорями ('https://www.python.org/about/success/#government')
        new_links = []
        for link in links:
            if link not in new_links:
                if "ftp" not in link and "#" not in link:
                    if "www.python.org" in link and "web.archive.org" not in link and "www.python.org.ar" not in link:
                        new_links.append(link)
        new_links = tuple(new_links)

        # наполнение таблицы Links
        time0 = time.time()
        for new_link in new_links:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Links WHERE Link=? OR Link=? OR Link=?", (new_link, new_link+"/", new_link[:-1]))
                link_exist = cur.fetchall()
            if len(link_exist) == 0:
                with con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Links (Link, HTTP_status_code) VALUES (?, ?)", (new_link, 0))
                    last_id = cur.lastrowid
        time0 = time.time() - time0
        time1 += time0

        # наполнение таблицы Parent_child, то есть формирование таблицы связей
        # Parent_link и Child_link -- Id ссылок в таблице Links
        # например, на странице www.python.org находится 58 ссылок, все они добавляются в таблицу связей
        # | Id | Parent_link | Child_link |
        # | 1  |           1 |          1 | Parent_link - https://www.python.org/, Child_link - https://www.python.org/
        # | 2  |           1 |          2 | Parent_link - https://www.python.org/, Child_link - https://www.python.org/psf-landing/
        time0 = time.time()
        for new_link in new_links:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Links WHERE Link=? OR Link=? OR Link=?", (new_link, new_link + "/", new_link[:-1]))
                child_link = cur.fetchall()
                row = list(child_link[0])
                child_link_id = row[0]
                cur.execute("INSERT INTO Parent_child (Parent_link, Child_link) VALUES (?, ?)", (first_not_parsed_link_id, child_link_id))
        time0 = time.time() - time0
        time2 += time0

    finally:
        count += 1
        print("обработано ссылок: %s" % count)
        print("ссылок в БД: %s" % last_id)
        print("первая таблица обработана:", time1)
        print("вторая таблица обработана:", time2)

# v3.1 -- в отличие от v2, третья версия использует БД (sqlite)
# по сравнению с v3, немного изменен алгоритм проверки наличия ссылки в БД -- v3 использовала для этого промежуточный
# список, v3.1 работает напрямую с таблицей БД
# v3.2 -- две таблицы: для нормальных и для битых ссылок
# v3.3 -- 1 таблица для всех ссылок, 1 таблица в формате "страница-все ссылки на этой странице"
# v3.4 -- пофикшен "/" (подробнее см. примечение тут --
# https://github.com/ExitProcess/other_scripts/blob/0c1fbee9f2271f1ac7b2f057c9ec1d8e8a124817/readme.txt)
