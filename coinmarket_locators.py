from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """
    A class for main page locators. All main page locators should come here
    Класс локаторов главной страницы. Все локаторы главной страницы следует размещать здесь
    """
    MARKET_CAP_SORT_BUTTON = (By.ID, "th-marketcap")
    MARKET_CAP_1 = (By.XPATH, "//tr[1]/td[3]")
    MARKET_CAP_100 = (By.XPATH, "//tr[100]/td[3]")
