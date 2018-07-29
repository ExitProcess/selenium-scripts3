# еще один линк-чекер, в отличие от первой версии, которая была реализована на библиотеке selenium webdriver,
# во второй версии используются библиотеки urllib и lxml

import time
import urllib.error
import urllib.request
from lxml import html
from lxml import etree

# список прокси
proxies = ['46.50.136.4:53281',
           '46.45.19.138:53281',
           '89.189.130.205:8080',
           ]

links_base = ["https://www.python.org/", ]
referer_link = ["https://www.python.org/", ]
index = 0
count_404 = 0

doc = open("404.txt", "w+")
doc.close()


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


while index != len(links_base):
    try:
        # каждые 50 итераций показывать ip
        if (index % 50) == 0:
            response = urllib.request.urlopen('https://api.ipify.org')
            ip = response.read()
            print('My public IP address is: {}'.format(ip))

        response = urllib.request.urlopen(links_base[index])

        # инфо для отладки
        print(links_base[index])
        print(response.geturl())

        # обработка переадресации на подсайт
        # https://www.python.org/psf/license ->> https://docs.python.org/3/license.html
        # подсайты не проверяются
        if "www.python.org" not in response.geturl():
            continue
    except UnicodeEncodeError:  # обработка unicode-ссылок, пока заглушка, позже будет нормальный обработчик
        # https://www.python.org/events/python-events/553/“https:/pydata.org/delhi2017“
        # ссылка находится на странице https://www.python.org/events/python-events/553/
        doc = open("404.txt", "a+")
        doc.write(referer_link[index] + "\n")
        doc.write((" " * 8) + links_base[index] + "\n")
        doc.close()
        count_404 += 1
    except urllib.error.HTTPError as error:
        if error.code == 404:
            doc = open("404.txt", "a+")
            doc.write(referer_link[index] + "\n")
            doc.write((" " * 8) + links_base[index] + "\n")
            doc.close()
            count_404 += 1
    except urllib.error.URLError as error:  # обычно [WinError 10060]
        # [WinError 10054] Удаленный хост принудительно разорвал существующее подключение
        print(error.reason)
        print("выбор самого быстрого прокси-сервера")
        fast_proxy_index = select_fast_proxy()
        proxy_handler(proxies[fast_proxy_index])
        index -= 1
    else:
        try:
            tree = html.fromstring(response.read())
            tree.make_links_absolute(response.geturl(), resolve_base_href=False)

            links_list = tree.xpath('//a/@href')

            # обработка результатов -- ссылки только на www.python.org, не добавлять в список:
            # подсайты и сторонние сайты ('https://docs.python.org/3/', 'http://twitter.com/ThePSF')
            # ссылки с якорями ('https://www.python.org/about/success/#government')
            for link in links_list:
                if "ftp" not in link and "#" not in link:
                    if "www.python.org" in link and "web.archive.org" not in link and "www.python.org.ar" not in link:
                        if link not in links_base:
                            links_base.append(link)
                            referer_link.append(links_base[index])
        except etree.ParserError as error:
            # обработка пустых страниц, например https://www.python.org.ar/wiki/PyCamp/2018/raw
            print(error)  # Document is empty
    finally:
        index += 1
        # инфо для отладки
        print(index)
        print(len(links_base))
        print(len(referer_link))
        print(count_404)
