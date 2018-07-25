import urllib.request

# список прокси -- http://spys.one/proxies/
proxies = ['95.143.135.149:41258',
           '186.121.249.220:8080',
           '41.160.96.250:8080',
           '80.233.185.116:8080',
           '50.250.144.26:8080',
           '50.250.144.26:8080',
           '185.14.149.53:8080',
           '212.69.18.132:36029',
           '37.235.67.3:8080']

for proxy in proxies:
    proxy_support = urllib.request.ProxyHandler({'https': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    # для получения ip используется сайт https://www.ipify.org
    response = urllib.request.urlopen('https://api.ipify.org')

    ip = response.read()
    print('My public IP address is: {}'.format(ip))
