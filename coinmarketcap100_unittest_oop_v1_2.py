# v 1.2 -- используется переменная класса, и другой алгоритм проверки списка элементов по возрастанию
# перевернутый список элементов по возрастанию сравнивается с проверенным списком элементов по убыванию
# скрипт работает быстрее, в отличие от скрипта с проверкой каждого элемента списка отдельно

import unittest
from selenium import webdriver


class CoinMarketCapSort(unittest.TestCase):
    # тут сохраняется текст элементов, список из первого метода (по убыванию)
    list_mcap_elements_dec_text = []

    def setUp(self):
        # метод setUp запускается перед каждым методом теста
        self.driver = webdriver.Chrome('C:\SeleniumDrivers\Chrome\chromedriver.exe')
        self.driver.get("https://coinmarketcap.com")
        self.sort_button = self.driver.find_element_by_id("th-marketcap")
        self.sort_button.click()

    def test_market_cap_sort_dec(self):
        # список элементов, отсортированных по убыванию
        list_mcap_elements_dec = self.driver.find_elements_by_css_selector(".market-cap")
        del list_mcap_elements_dec[-1]

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
        # если сортировка по убыванию работает правильно, то создается переменная класса list_mcap_elements_dec_text
        # в списке хранится текст каждого элемента (можно добавлять и после каждой проверки, но так понятнее)
        for element in list_mcap_elements_dec:
            CoinMarketCapSort.list_mcap_elements_dec_text.append(element.text)

    def test_market_cap_sort_inc(self):
        self.sort_button.click()
        # список элементов, отсортированных по возрастанию
        list_mcap_elements_inc = self.driver.find_elements_by_css_selector(".market-cap")
        del list_mcap_elements_inc[-1]
        # список элементов по возрастанию ->> список элементов по убыванию
        list_mcap_elements_inc.reverse()
        # текст этих элементов
        list_mcap_elements_inc_reverse_text = []

        for element in list_mcap_elements_inc:
            list_mcap_elements_inc_reverse_text.append(element.text)

        assert CoinMarketCapSort.list_mcap_elements_dec_text == list_mcap_elements_inc_reverse_text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
