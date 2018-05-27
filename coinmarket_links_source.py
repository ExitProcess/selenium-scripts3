# скрипт парсит веб-страницы криптовалют
# работает аналогично fifa_rating_3_source.py

from lxml import html
from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://coinmarketcap.com")
cookie_close = driver.find_element_by_css_selector(".banner-alert-close [aria-hidden]")
cookie_close.click()

source = driver.page_source
tree = html.fromstring(source)
cryptocurrencies_list = tree.xpath("//tr/td[2]/a")

for cryptocurrency in cryptocurrencies_list:
    url = cryptocurrency.get("href")  # /currencies/bitcoin/
    url = ("https://coinmarketcap.com" + url)
    driver.get(url)

    cryptocurrency_name = driver.find_element_by_css_selector(".text-large")
    site_elem = driver.find_element_by_link_text("Website")
    cryptocurrency_url = site_elem.get_attribute("href")
    print(cryptocurrency_name.text, cryptocurrency_url)

driver.close()
driver.quit()

# Bitcoin (BTC) https://bitcoin.org/
# Ethereum (ETH) https://www.ethereum.org/
# Ripple (XRP) https://ripple.com/
# ...
