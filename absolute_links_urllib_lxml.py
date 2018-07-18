# различные способы получения ссылок с веб-страниц + сравнение скорости
# 1. urllib + lxml
# urllib - https://docs.python.org/3.6/library/urllib.request.html
# lxml - https://lxml.de

# учитывается время, затраченное на импорт
import time

start = time.time()

from urllib.request import urlopen
from lxml import html

URL = "https://www.python.org/about/success/"

response = urlopen(URL)
tree = html.fromstring(response.read())
tree.make_links_absolute("https://www.python.org", resolve_base_href=True)

links_list = tree.xpath('//a/@href')

# фильтр -- ссылки только на www.python.org, не добавлять в список:
# подсайты и сторонние сайты ('https://docs.python.org/3/', 'http://twitter.com/ThePSF')
# ссылки с якорями ('https://www.python.org/about/success/#government')
# обрабатываются дубли и одинаковые ссылки со слешем и без ('https://www.python.org/', 'https://www.python.org')
clear_list = []
for link in links_list:
    if "www.python.org" in link and "#" not in link:
        if link not in clear_list and (link + '/') not in clear_list and link[:-1] not in clear_list:
            clear_list.append(link)

finish = time.time() - start

print(clear_list)
print(len(clear_list))  # 83
print(finish)  # 0.5500311851501465 - 0.6010341644287109
