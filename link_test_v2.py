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
        tree.make_links_absolute(links_base[index], resolve_base_href=False)

        links_list = tree.xpath('//a/@href')

        # обработка результатов -- ссылки только на www.python.org, не добавлять в список:
        # подсайты и сторонние сайты ('https://docs.python.org/3/', 'http://twitter.com/ThePSF')
        # ссылки с якорями ('https://www.python.org/about/success/#government')
        for link in links_list:
            if "ftp" not in link and "#" not in link and "www.python.org" in link:
                # для того, чтобы работал метод make_links_absolute, ссылка должна заканчиваться слешем
                # "?" not in link - https://www.python.org/jobs/?page=1 -- не добавлять слеш, т.к. запрос
                # не добавлять слеш к расширениям -- .asc, .txt, .png, .psd, .svg, .pdf, .html и т.д.
                if link[-1] != "/":
                    if link[-4] != "." and link[-5] != "." and "?" not in link:
                        link = link + "/"
                if link not in links_base:
                    links_base.append(link)
                    referer_link.append(links_base[index])
    index += 1
    # инфо для отладки
    print(index)
    print(len(links_base))
    print(len(referer_link))
    print(count_404)
