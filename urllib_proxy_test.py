import urllib.request

# список прокси -- http://spys.one/proxies/
proxies = {'https': '14.207.128.15:8080'}
proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

# для получения ip используется сайт https://www.ipify.org
response = urllib.request.urlopen('https://api.ipify.org')

ip = response.read()
print('My public IP address is: {}'.format(ip))
