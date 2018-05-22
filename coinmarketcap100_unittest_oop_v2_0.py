# новая версия -- теперь два метода, проверяющие сортировку по убыванию и по возрастанию, перенесены в один
# метод. таким образом, используются 3 метода, каждый из которых используется по 1 разу, в отличие от прошлых версий,
# в которых было 4 метода, setUp и tearDown использовались по 2 раза, и test_inc / test_dec по разу.
# старые версии -- Ran 2 tests in 43.017s
# эта версия -- Ran 1 test in 13.598s -- Ran 1 test in 21.855s

import unittest
from selenium import webdriver


class CoinMarketCapSort(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('C:\SeleniumDrivers\Chrome\chromedriver.exe')
        self.driver.get("https://coinmarketcap.com")
        self.sort_button = self.driver.find_element_by_id("th-marketcap")
        self.sort_button.click()

    def test_market_cap_sort(self):
        # список элементов, отсортированных по убыванию
        list_mcap_elements_dec = self.driver.find_elements_by_css_selector(".market-cap")
        del list_mcap_elements_dec[-1]

        # список элементов, отсортированных по возрастанию
        self.sort_button.click()
        list_mcap_elements_inc = self.driver.find_elements_by_css_selector(".market-cap")
        del list_mcap_elements_inc[-1]

        # работа с list_mcap_elements_dec
        # цикл проверяет, чтобы следующий элемент списка был меньше предыдущего
        count = 0
        for i in range(0, len(list_mcap_elements_dec) - 1):  # последний элемент списка надо выводить отдельно
            elem_current = list_mcap_elements_dec[i].text
            elem_next = list_mcap_elements_dec[i + 1].text
            # if "$1 000" больше "$100" or "$2 000" больше "$1 000"
            if len(elem_current) > len(elem_next) or elem_current > elem_next:
                count += 1
        elem_last = list_mcap_elements_dec[-1].text
        if elem_last < elem_current or len(elem_last) < len(elem_current):
            count += 1
        # проверено 100 элементов, если счетчик == 100, то все элементы расположены в порядке убывания
        assert count == 100
        print("сортировка по убыванию -- ОК")

        # если все элементы в списке list_mcap_elements_dec расположены по убыванию, то этот список надо сравнить с
        # перевернутым list_mcap_elements_inc. если списки равны, то и сортировка по возрастанию работает правильно.
        # список элементов по возрастанию -->> список элементов по убыванию
        list_mcap_elements_inc.reverse()

        assert list_mcap_elements_dec == list_mcap_elements_inc
        print("сортировка по возрастанию -- ОК")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
