# скрипт парсит веб-страницы криптовалют
# работает аналогично fifa_rating.py

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://coinmarketcap.com/")

cookie_close = driver.find_element_by_css_selector(".banner-alert-close [aria-hidden]")
cookie_close.click()

cryptocurrencies_list = driver.find_elements_by_css_selector(".currency-name-container")
for cryptocurrency in cryptocurrencies_list:
    time.sleep(0.5)
    ActionChains(driver).move_to_element(cryptocurrency).perform()
    time.sleep(0.5)
    ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(cryptocurrency).key_up(Keys.LEFT_CONTROL).perform()

    window_handles = driver.window_handles
    cryptocurrencies_page = window_handles[0]
    cryptocurrency_page = window_handles[1]
    driver.switch_to.window(cryptocurrency_page)

    cryptocurrency_name = driver.find_element_by_css_selector(".text-large")
    site_elem = driver.find_element_by_link_text("Website")
    cryptocurrency_url = site_elem.get_attribute("href")
    print(cryptocurrency_name.text, cryptocurrency_url)

    driver.close()
    driver.switch_to.window(cryptocurrencies_page)

driver.close()
driver.quit()

# Bitcoin (BTC) https://bitcoin.org/
# Ethereum (ETH) https://www.ethereum.org/
# Ripple (XRP) https://ripple.com/
# Bitcoin Cash (BCH) https://www.bitcoincash.org/
# EOS (EOS) https://eos.io/
# Litecoin (LTC) https://litecoin.com/
# Stellar (XLM) https://www.stellar.org/
# Cardano (ADA) https://www.cardano.org/
# TRON (TRX) https://tron.network/
# IOTA (MIOTA) https://www.iota.org/
# NEO (NEO) https://neo.org/
# Dash (DASH) https://www.dash.org/
