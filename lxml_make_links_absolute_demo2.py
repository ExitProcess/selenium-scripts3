import urllib.request
from lxml import html

# по адресу https://www.python.org/doc/ есть ссылка https://www.python.org/doc/av
# (в подвале, Documentation ->> Audio/Visual Talks)
# если в метод make_links_absolute передать эту ссылку без слеша в конце, то
# метод вернет неправильную (неполную) абсолютную ссылку -- https://www.python.org/doc/5minutes
# правильная ссылка -- https://www.python.org/doc/av/5minutes -- получится, если передать в метод
# ссылку со слешем в конце -- https://www.python.org/doc/av/

urls = ["https://www.python.org/doc/av/", "https://www.python.org/doc/av"]
for url in urls:
    response = urllib.request.urlopen(url)

    tree = html.fromstring(response.read())
    tree.make_links_absolute(response.geturl(), resolve_base_href=True)

    links = tree.xpath("//a/@href")
    # print(links)
    # print(len(links))

    for link in links:
        if "5minutes" in link:
            print(link)

# https://www.python.org/doc/av/5minutes
# https://www.python.org/doc/av/5minutes
# https://www.python.org/doc/av/5minutes
# https://www.python.org/doc/av/5minutes
