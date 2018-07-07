import time
from coinmarket_locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. i.e. python.org"""

    def is_title_matches(self):
        """Verifies that the hardcoded text 'Cryptocurrency Market Capitalizations' appears in page title"""
        return "Cryptocurrency Market Capitalizations" in self.driver.title

    def click_sort_button(self):
        """Нажатие на кнопку сортировки столбца Market Cap"""
        market_cap_sort_button = self.driver.find_element(*MainPageLocators.MARKET_CAP_SORT_BUTTON)
        market_cap_sort_button.click()
        time.sleep(1)

    def double_click_sort_button(self):
        """Два последовательных нажатия на кнопку сортировки столбца Market Cap"""
        market_cap_sort_button = self.driver.find_element(*MainPageLocators.MARKET_CAP_SORT_BUTTON)
        market_cap_sort_button.click()
        time.sleep(1)
        market_cap_sort_button.click()
        time.sleep(1)

    def market_cap_value_1(self):
        market_cap_1 = self.driver.find_element(*MainPageLocators.MARKET_CAP_1)
        value_1 = market_cap_1.text
        return value_1

    def market_cap_value_100(self):
        market_cap_100 = self.driver.find_element(*MainPageLocators.MARKET_CAP_100)
        value_100 = market_cap_100.text
        return value_100
