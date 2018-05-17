from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

# driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL + "T")
#
# оказывается chrome driver с 58 версии не открывает новую вкладку по ctrl + t
# https://github.com/SeleniumHQ/selenium/issues/5462
# https://bugs.chromium.org/p/chromedriver/issues/detail?id=2265
#
# реализация будет такой -- 1) будет ctrl + LMBC по любому элементу;
#                           2) затем переключение по хендлу;
#                           3) нужный урл в новой вкладке.
#

new = driver.find_element_by_link_text("SPYS.ONE © 2008-2018")
ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(new).key_up(Keys.LEFT_CONTROL).perform()

handles_list = driver.window_handles
tab1 = handles_list[0]
tab2 = handles_list[1]

driver.switch_to.window(tab2)

driver.get("https://hidemy.name/ru/proxy-checker/")
pass