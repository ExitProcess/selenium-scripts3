# скрипт парсит веб-страницы криптовалют
# работает аналогично fifa_rating_3_source.py
# страницы долго грузятся из-за рекламы, поэтому для оптимизации скрипт одновременно парсит данные с 5 вкладок

from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://coinmarketcap.com")
cookie_close = driver.find_element_by_css_selector(".banner-alert-close [aria-hidden]")
cookie_close.click()

source = driver.page_source
tree = html.fromstring(source)
cryptocurrencies_list = tree.xpath("//tr/td[2]/a")


def new_page(n):
    while n > 0:
        page_button = driver.find_element_by_css_selector(".navbar-brand .default")
        ActionChains(driver).move_to_element(page_button).perform()
        ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(page_button).key_up(Keys.LEFT_CONTROL).perform()
        n -= 1


new_page(4)

# tab1 = tabs_handles[0], tab2 = tabs_handles[1], tab3 = tabs_handles[2], tab4 = tabs_handles[3], tab5 = tabs_handles[4]
tabs_handles = driver.window_handles

tab = 0
for cryptocurrency in cryptocurrencies_list:
    url = cryptocurrency.get("href")  # /currencies/bitcoin/
    url = ("https://coinmarketcap.com" + url)

    if tab == 5:
        tab = 0

    driver.switch_to.window(tabs_handles[tab])

    if "$" in driver.title:
        cryptocurrency_name = driver.find_element_by_css_selector(".text-large")
        site_elem = driver.find_element_by_link_text("Website")
        cryptocurrency_url = site_elem.get_attribute("href")
        print(cryptocurrency_name.text, cryptocurrency_url)

        driver.get(url)
        tab += 1
    else:
        driver.get(url)
        tab += 1


driver.close()
driver.quit()

# Bitcoin (BTC) https://bitcoin.org/
# Ethereum (ETH) https://www.ethereum.org/
# Ripple (XRP) https://ripple.com/
# ...
