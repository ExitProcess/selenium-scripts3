import unittest
from selenium import webdriver
import coinmarket_page


class CoinMarketSort(unittest.TestCase):
    """
    A sample test class to show how page object works
    Этот класс показывает, как работает Page Object Pattern
    """

    def setUp(self):
        self.driver = webdriver.Chrome('C:\SeleniumDrivers\Chrome\chromedriver.exe')
        self.driver.get("https://coinmarketcap.com")

    def test_market_cap_sort(self):
        """
        Тест проверяет работу сортировки Market Cap (рыночной стоимости) на сайте https://coinmarketcap.com
        Алгоритм:
        1. происходит клик по сортировке столбца Market Cap, т.о. список сортируется по убыванию
        2. фиксируются значения Market Cap #1 (для Bitcoin) и Market Cap #100 (для Storm)
        3. снова происходит клик по сортировке столбца Market Cap, т.о. список сортируется по возрастанию
        4. снова фиксируются значения Market Cap #1 и #100
        5. полученные в шаге 4 значения сравниваются со значениями из шага 2
        6. Market Cap #1 и #100 после кликов должны быть равны Market Cap #100 и #1 до кликов, соответственно.
        """

        #  Загрузка главной страницы. Для этого теста главная страница -- https://coinmarketcap.com
        main_page = coinmarket_page.MainPage(self.driver)
        #  Проверка, загрузилась ли главная страница (слова Cryptocurrency Market Capitalizations в title)
        assert main_page.is_title_matches(), "https://coinmarketcap.com не загрузился"

        main_page.click_sort_button()
        before_1 = main_page.market_cap_value_1()  # $114 188 952 645
        before_100 = main_page.market_cap_value_100()  # $94 676 142

        main_page.click_sort_button()
        after_1 = main_page.market_cap_value_1()  # $94 676 142
        after_100 = main_page.market_cap_value_100()  # $114 188 952 645

        assert before_1 == after_100 and before_100 == after_1, "сортировка Market Cap не работает"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
