# еще один линк-чекер, в отличие от первой версии, которая была реализована на библиотеке selenium webdriver,
# во второй версии используются библиотеки urllib и lxml

import urllib.error
import urllib.request
from lxml import html

# список прокси
proxy_index = -1
proxies = ['91.234.183.112:41258',
           '5.175.75.190:8080',
           '91.224.63.218:8080',
           '168.181.212.101:8080',
           '212.69.18.132:36029',
           '178.63.8.211:3128',
           '46.50.136.4:53281',
           '46.45.19.138:53281',
           '2.94.171.75:8080',
           '178.33.194.169:3128',
           '89.189.130.205:8080',
           '46.227.161.214:53281',
           '188.120.231.22:10009',
           '81.163.61.21:41258',
           '178.176.28.164:8080',
           '109.74.142.138:53281',
           '77.79.146.91:3128',
           '193.105.124.127:8080',
           '91.201.169.243:41258'
           ]

links_base = ["https://www.python.org/", ]
referer_link = ["https://www.python.org/", ]
index = 0
count_404 = 0

doc = open("404.txt", "w+")
doc.close()

while index != len(links_base):
    try:
        response = urllib.request.urlopen(links_base[index])
        # обработка переадресации на подсайт
        if "www.python.org" not in response.geturl():
            index += 1
            continue
    except UnicodeEncodeError:  # обработка unicode-ссылок, пока заглушка, позже будет нормальный обработчик
        print(links_base[index])
    except urllib.error.HTTPError as error:
        if error.code == 404:
            doc = open("404.txt", "a+")
            doc.write(referer_link[index] + "\n")
            doc.write((" " * 8) + links_base[index] + "\n")
            doc.close()
            count_404 += 1
    except urllib.error.URLError as error:  # обычно [WinError 10060]
        print(error.reason)
        proxy_index += 1  # (первый или) следующий прокси из списка
        try:
            proxy_support = urllib.request.ProxyHandler({'https': proxies[proxy_index]})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
            continue
        except Exception:  # если не удалось подключиться к прокси, то повторить запрос с предыдущим подключением
            continue
    else:
        tree = html.fromstring(response.read())
        tree.make_links_absolute(response.geturl(), resolve_base_href=False)

        links_list = tree.xpath('//a/@href')

        # обработка результатов -- ссылки только на www.python.org, не добавлять в список:
        # подсайты и сторонние сайты ('https://docs.python.org/3/', 'http://twitter.com/ThePSF')
        # ссылки с якорями ('https://www.python.org/about/success/#government')
        for link in links_list:
            if "ftp" not in link and "#" not in link and "www.python.org" in link:
                if link not in links_base:
                    links_base.append(link)
                    referer_link.append(links_base[index])
        # инфо для отладки
        print(links_base[index])
        print(response.geturl())

    index += 1

    # инфо для отладки
    print(index)
    print(len(links_base))
    print(len(referer_link))
    print(count_404)
