from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://news.rambler.ru/")

# чтобы появился блок категорий, надо перейти в полноэкранный режим
driver.fullscreen_window()

# Рамблер/финансы
finance_button = driver.find_element_by_css_selector("[data-blocks='finance\:\:not_current']")
finance_button.click()
assert "https://finance.rambler.ru/" in driver.current_url
assert "Рамблер/финансы" in driver.title

# Рамблер/женский
women_button = driver.find_element_by_css_selector("[data-blocks='woman\:\:not_current']")
women_button.click()
assert "https://woman.rambler.ru/" in driver.current_url
assert "Рамблер/женский" in driver.title

# Рамблер/кино
kino_button = driver.find_element_by_css_selector("[data-blocks='kino\:\:not_current']")
kino_button.click()
assert "https://kino.rambler.ru/" in driver.current_url
assert "Рамблер/кино" in driver.title

driver.close()
driver.quit()
