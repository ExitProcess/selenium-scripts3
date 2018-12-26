from selenium import webdriver

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

css_selectors = ("[data-blocks='finance\:\:not_current']",
                 "[data-blocks='woman\:\:not_current']",
                 "[data-blocks='kino\:\:not_current']")

urls = ("https://finance.rambler.ru/",
        "https://woman.rambler.ru/",
        "https://kino.rambler.ru/")

titles = ("Рамблер/финансы",
          "Рамблер/женский",
          "Рамблер/кино")

driver.get("https://news.rambler.ru/")
# чтобы появился блок категорий, надо перейти в полноэкранный режим
driver.fullscreen_window()

# цикл проверки всех элементов кортежей поочередно
index = 0
while index < len(css_selectors):
    cat_button = driver.find_element_by_css_selector(css_selectors[index])
    cat_button.click()
    assert urls[index] in driver.current_url
    assert titles[index] in driver.title
    index += 1

driver.close()
driver.quit()
