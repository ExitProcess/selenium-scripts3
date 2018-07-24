import urllib.request

# список прокси -- http://spys.one/proxies/
proxies = ['14.207.128.15:8080',
           '2.94.171.75:8080',
           '183.88.155.200:8080',
           '177.22.120.69:8080',
           '79.148.66.198:8080']

for proxy in proxies:
    proxy_support = urllib.request.ProxyHandler({'https': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    # для получения ip используется сайт https://www.ipify.org
    response = urllib.request.urlopen('https://api.ipify.org')

    ip = response.read()
    print('My public IP address is: {}'.format(ip))
