# линк-чекер python.org, третья версия
# в отличие от прошлой версии, третья версия использует БД (sqlite)

import time
import sqlite3
import urllib.error
import urllib.request

from lxml import html

# подключение к базе данных
con = sqlite3.connect("links.db")

# начало работы с базой данных
with con:
    cur = con.cursor()
    # удаление старой таблицы Links, если она существует
    cur.execute("DROP TABLE IF EXISTS Links")
    # создание таблицы Links
    cur.execute("CREATE TABLE Links(Id INTEGER PRIMARY KEY, Link TEXT, HTTP_status_code INT, Parent TEXT)")
    # добавление 1 записи
    cur.execute("INSERT INTO Links(Link, HTTP_status_code, Parent) VALUES ('https://www.python.org/', 0, 'https://www.python.org/')")
    #  отладочные записи
    #  cur.execute("INSERT INTO Links(Link, HTTP_status_code) VALUES ('https://www.python.org/111', 0)")
    #  cur.execute("INSERT INTO Links(Link, HTTP_status_code) VALUES ('https://www.python.org/444', 0)")

# переменные
# список прокси
proxies = ['94.130.203.204:51746',
           '194.135.246.178:42010',
           '91.205.146.25:37501',
           '195.218.173.242:48181',
           ]
# счетчик
count = 0


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


while count < cur.lastrowid:
    try:
        # выбор первой записи, где HTTP status code = 0 (т.е. получение первой ссылки, по которой не было перехода)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Links WHERE HTTP_status_code=0 LIMIT 1")
            rows = cur.fetchall()  # <class 'list'>: [(1, 'https://www.python.org', 0)]
            rows_list = list(rows[0])  # <class 'list'>: [1, 'https://www.python.org', 0]

        # ссылка, id и http-статус из первой записи в Links, где HTTP status code = 0
        first_not_tested_link = rows_list[1]  # 'https://www.python.org'
        first_not_tested_link_id = rows_list[0]  # 1
        first_not_tested_link_http_status = rows_list[2]  # 0

        # HTTP-запрос к выбранной странице
        # отладка
        print("переход по ссылке: %s" % first_not_tested_link)
        response = urllib.request.urlopen(first_not_tested_link)

        # print(response.geturl())
        # print(response.getcode())

    # обработчик ошибок HTTP
    except urllib.error.HTTPError as error:
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Links SET HTTP_status_code = ? WHERE Id = ?",
                        (error.code, first_not_tested_link_id))

    except urllib.error.URLError as error:  # обычно [WinError 10060]
        # [WinError 10054] Удаленный хост принудительно разорвал существующее подключение
        print(error.reason)
        print("выбор самого быстрого прокси-сервера")
        fast_proxy_index = select_fast_proxy()
        proxy_handler(proxies[fast_proxy_index])
        count -= 1

    except UnicodeEncodeError:  # обработка unicode-ссылок (заглушка)
        # https://www.python.org/events/python-events/553/“https:/pydata.org/delhi2017“
        # ссылка находится на странице https://www.python.org/events/python-events/553/
        # + https://www.python.org/events/python-user-group/192/
        # unicode-ссылкам проставляется http-status 999, позже будет нормальный обработчик (на urllib.parse)
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Links SET HTTP_status_code = ? WHERE Id = ?",
                        (999, first_not_tested_link_id))

    else:
        # обновление записи, когда http-статус = 200
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Links SET HTTP_status_code = ? WHERE Id = ?",
                        (response.getcode(), first_not_tested_link_id))

        # парсинг ссылок с текущей страницы
        tree = html.fromstring(response.read())
        tree.make_links_absolute(response.geturl(), resolve_base_href=False)
        links_list = tree.xpath('//a/@href')

        # создание списка ссылок из таблицы Links
        with con:
            cur = con.cursor()
            cur.execute("SELECT Link FROM Links")
            db_links = cur.fetchall()  # [('https://www.python.org',)]
            # print(db_links)
            db_links_list = [i[0] for i in db_links]  # ['https://www.python.org']
            # print(db_links_list)

        # обработка результатов -- ссылки только на www.python.org, не добавлять в список:
        # подсайты и сторонние сайты ('https://docs.python.org/3/', 'http://twitter.com/ThePSF')
        # ссылки с якорями ('https://www.python.org/about/success/#government')
        for new_link in links_list:
            if "ftp" not in new_link and "#" not in new_link:
                if "www.python.org" in new_link and "web.archive.org" not in new_link and "www.python.org.ar" not in new_link:
                    if new_link not in db_links_list:
                        #  если ссылка удовлетворяет условиям, то происходит добавление ее в БД и в список db_links_list
                        #  (т.о., список из БД создается при парсинге страницы, а не при проверке каждой ссылки на наличие ее в БД)
                        # добавление ссылки в db_links_list
                        db_links_list.append(new_link)
                        # добавление ссылки в БД
                        with con:
                            cur = con.cursor()
                            cur.execute("INSERT INTO Links (Link, HTTP_status_code, Parent) VALUES (?, ?, ?)",
                                        (new_link, 0, first_not_tested_link))
    finally:
        count += 1
        print("обработано ссылок: %s" % count)
        print("ссылок в БД: %s" % cur.lastrowid)

#
# вывод в консоль в конце работы:
#
# ссылок в БД: 4545
# переход по ссылке: https://www.python.org/events/python-user-group/locations/110/
# обработано ссылок: 4543
# ссылок в БД: 4545
# переход по ссылке: https://www.python.org/events/python-events/locations/61/
# обработано ссылок: 4544
# ссылок в БД: 4545
# переход по ссылке: https://www.python.org/events/python-events/locations/70/
# обработано ссылок: 4545
# ссылок в БД: 4545
#
# Process finished with exit code 0
#
