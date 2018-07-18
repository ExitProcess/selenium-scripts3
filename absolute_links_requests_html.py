# различные способы получения ссылок с веб-страниц + сравнение скорости
# 3. Requests-HTML (Only Python 3.6 is supported.)
# Requests-HTML - http://html.python-requests.org/

# учитывается время, затраченное на импорт
import time
start = time.time()

from requests_html import HTMLSession

URL = "https://www.python.org/about/success/"

session = HTMLSession()
response3 = session.get(URL)
links_set = response3.html.absolute_links

# фильтр -- ссылки только на www.python.org, не добавлять в список:
# подсайты и сторонние сайты ('https://docs.python.org/3/', 'http://twitter.com/ThePSF')
# ссылки с якорями ('https://www.python.org/about/success/#government')
# обрабатываются дубли и одинаковые ссылки со слешем и без ('https://www.python.org/', 'https://www.python.org')
clear_list = []
for link in links_set:
    if "www.python.org" in link and "#" not in link:
        if link not in clear_list and (link + '/') not in clear_list and link[:-1] not in clear_list:
            clear_list.append(link)

finish = time.time() - start

print(clear_list)
print(len(clear_list))  # 83
print(finish)  # 0.9390535354614258 - 1.0250585079193115
