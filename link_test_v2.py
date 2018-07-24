# еще один линк-чекер, в отличие от первой версии, которая была реализована на библиотеке selenium webdriver,
# во второй версии используются библиотеки urllib и lxml

import time
import urllib.error
import urllib.request
from lxml import html

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
    except urllib.error.HTTPError as error:
        if error.code == 404:
            doc = open("404.txt", "a+")
            doc.write(referer_link[index] + "\n")
            doc.write((" " * 8) + links_base[index] + "\n")
            doc.close()
            count_404 += 1
    except urllib.error.URLError as error:
        print(error.reason)
        print("pause")
        time.sleep(30)
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
