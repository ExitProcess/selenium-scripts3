import urllib.request
import urllib.parse

url = "https://en.wikipedia.org/wiki/Thomas_Müller"

try:
    response = urllib.request.urlopen(url)
except UnicodeEncodeError as e:
    print(e)
    print(url)

    url = urllib.parse.urlsplit(url)
    url = list(url)
    print(url)

    url[2] = urllib.parse.quote(url[2])
    print(url[2])

    url = urllib.parse.urlunsplit(url)
    print(url)

    response = urllib.request.urlopen(url)
