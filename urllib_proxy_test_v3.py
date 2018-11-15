import time
import urllib.request

# список прокси -- http://spys.one/proxies/
proxies = ['217.197.240.87:30411',
           '91.107.38.48:33801',
           '78.109.129.46:45943',
           '31.13.22.142:40100',
           '178.161.150.46:31765',
           '109.106.139.225:45689',
           '84.52.124.217:3100',
           '128.68.47.241:53577'
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
