import time
import urllib.request

# список прокси -- http://spys.one/proxies/
proxies = ['195.9.112.102:35756',
           '188.168.58.130:40917',
           '95.165.228.74:47315',
           '176.192.124.98:60787',
           '176.117.216.120:44049',
           '176.196.238.210:60449',
           '145.255.30.91:59679',
           '46.147.192.133:39692'
           ]
proxy_response = []

for proxy in proxies:
    try:
        proxy_support = urllib.request.ProxyHandler({'https': proxy})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

        start = time.time()
        response = urllib.request.urlopen('https://www.google.com')
        finish = time.time() - start
        proxy_response.append(finish)

        print(proxy, finish)
    except Exception:
        proxy_response.append(99.99)
        print("{} fail".format(proxy))

fast_index = proxy_response.index(min(proxy_response))
print("самый быстрый прокси")
print(proxies[fast_index], proxy_response[fast_index])
