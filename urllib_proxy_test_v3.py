import time
import urllib.request

# список прокси -- http://spys.one/proxies/
proxies = ['91.234.183.112:41258',
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
