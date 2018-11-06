# линк-чекер python.org, v3.1
# в отличие от v2, третья версия использует БД (sqlite)
# по сравнению с v3, немного изменен алгоритм проверки наличия ссылки в БД -- v3 использовала для этого промежуточный
# список, v3.1 работает напрямую с таблицей БД
# v3.2 -- две таблицы: для нормальных и для битых ссылок

import sys
import time
import sqlite3
import urllib.error
import urllib.request

from lxml import html
from lxml import etree


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
con = sqlite3.connect("links_v3_2.db")
# начало работы с базой данных
with con:
    cur = con.cursor()
    # удаление старых таблиц, если они существуют
    cur.execute("DROP TABLE IF EXISTS Links_200")
    cur.execute("DROP TABLE IF EXISTS Links_404")
    # создание таблиц Links_200, Links_404
    cur.execute("CREATE TABLE Links_200(Id INTEGER PRIMARY KEY, Link_200 TEXT, HTTP_status_code INT, Check_status INT)")
    cur.execute("CREATE TABLE Links_404(Id INTEGER PRIMARY KEY, Link_404 TEXT, HTTP_status_code INT)")
    # добавление стартовой записи
    cur.execute("INSERT INTO Links_200(Link_200, HTTP_status_code, Check_status) VALUES ('https://www.python.org/', 0, NULL)")

while count < last_id:
    try:
        # выбор первой записи, где HTTP status code = 0 (т.е. получение первой ссылки, по которой не было перехода)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Links_200 WHERE HTTP_status_code=0 LIMIT 1")
            rows = cur.fetchall()  # <class 'list'>: [(1, 'https://www.python.org', 0, 0)]
            rows_list = list(rows[0])  # <class 'list'>: [1, 'https://www.python.org', 0, 0]

        # столбцы Link_200 и Id первой строки, где HTTP status code = 0
        first_not_parsed_link = rows_list[1]  # 'https://www.python.org'
        first_not_parsed_link_id = rows_list[0]  # 1

        # HTTP-запрос к выбранной странице
        print("переход по ссылке: %s" % first_not_parsed_link)  # выводится для отладки
        response = urllib.request.urlopen(first_not_parsed_link)

    # обработчик ошибок HTTP
    except urllib.error.HTTPError as error:
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Links_404 (Link_404, HTTP_status_code) VALUES (?, ?)",  (first_not_parsed_link, error.code))
            cur.execute("DELETE FROM Links_200 WHERE Id = ?", (first_not_parsed_link_id,))

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
            cur.execute("INSERT INTO Links_404 (Link_404, HTTP_status_code) VALUES (?, ?)",  (first_not_parsed_link, 999))
            cur.execute("DELETE FROM Links_200 WHERE Id = ?", (first_not_parsed_link_id,))

    else:
        # обновление записи, когда http-статус = 200
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Links_200 SET HTTP_status_code = ? WHERE Id = ?",
                        (response.getcode(), first_not_parsed_link_id))

        # парсинг ссылок с текущей страницы
        tree = html.fromstring(response.read())
        tree.make_links_absolute(response.geturl(), resolve_base_href=False)
        links_list = tree.xpath('//a/@href')

        # обработка результатов -- ссылки только на www.python.org, не добавлять в таблицу:
        # подсайты и сторонние сайты ('https://docs.python.org/3/', 'http://twitter.com/ThePSF')
        # ссылки с якорями ('https://www.python.org/about/success/#government')
        for new_link in links_list:
            if "ftp" not in new_link and "#" not in new_link:
                if "www.python.org" in new_link and "web.archive.org" not in new_link and "www.python.org.ar" not in new_link:
                    with con:
                        cur = con.cursor()
                        cur.execute("SELECT Link_200 FROM Links_200 WHERE Link_200 = ? \
                                    UNION \
                                    SELECT Link_404 FROM Links_404 WHERE Link_404 = ?", (new_link, new_link))
                        link_exist = cur.fetchall()
                    if len(link_exist) == 0:
                        with con:
                            cur = con.cursor()
                            cur.execute("INSERT INTO Links_200 (Link_200, HTTP_status_code) VALUES (?, ?)",
                                        (new_link, 0))
                            last_id = cur.lastrowid

    finally:
        count += 1
        print("обработано ссылок: %s" % count)
        print("ссылок в БД: %s" % last_id)
