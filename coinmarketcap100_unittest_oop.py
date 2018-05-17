import unittest
from selenium import webdriver


class CoinMarketCapSort(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\SeleniumDrivers\Chrome\chromedriver.exe')

    def test_market_cap_sort_dec(self):
        driver = self.driver
        driver.get("https://coinmarketcap.com")
        sort_button = driver.find_element_by_id("th-marketcap")
        sort_button.click()
        # список элементов, отсортированных по убыванию
        list_mcap_elements_dec = driver.find_elements_by_css_selector(".market-cap")
        del list_mcap_elements_dec[-1]

        # цикл проверяет, чтобы следующий элемент списка был меньше предыдущего
        count = 0
        for i in range(0, len(list_mcap_elements_dec) - 1):  # последний элемент списка надо выводить отдельно
            elem_current = list_mcap_elements_dec[i].text
            elem_next = list_mcap_elements_dec[i + 1].text
            # условие для сравнения строк разной длины ("$146 109 484 586 больше $67 635 761 404")
            if len(elem_current) > len(elem_next):
                count += 1
            # условие для сравнения строк одинаковой длины ("$67 635 761 404 больше $27 646 445 524")
            if elem_current > elem_next:
                count += 1
        elem_last = list_mcap_elements_dec[-1].text
        if elem_last < elem_current or len(elem_last) < len(elem_current):
            count += 1
        # проверено 100 элементов, если счетчик == 100, то все элементы расположены в порядке убывания
        assert count == 100

    def test_market_cap_sort_inc(self):
        driver = self.driver
        driver.get("https://coinmarketcap.com")
        sort_button = driver.find_element_by_id("th-marketcap")
        sort_button.click()
        sort_button.click()
        # список элементов, отсортированных по возрастанию
        list_mcap_elements_inc = driver.find_elements_by_css_selector(".market-cap")
        del list_mcap_elements_inc[-1]

        # цикл проверяет, чтобы следующий элемент списка был больше предыдущего
        count = 0
        for i in range(0, len(list_mcap_elements_inc) - 1):  # последний элемент списка надо выводить отдельно
            elem_current = list_mcap_elements_inc[i].text
            elem_next = list_mcap_elements_inc[i + 1].text
            # условие для сравнения строк разной длины ("$67 635 761 404" меньше "$146 109 484 586")
            if len(elem_current) < len(elem_next):
                count += 1
            # условие для сравнения строк одинаковой длины ("$27 646 445 524" больше "$67 635 761 404")
            if elem_current < elem_next:
                count += 1
        elem_last = list_mcap_elements_inc[-1].text
        if elem_last > elem_current or len(elem_last) > len(elem_current):
            count += 1
        # проверено 100 элементов, если счетчик == 100, то все элементы расположены в порядке убывания
        assert count == 100

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
