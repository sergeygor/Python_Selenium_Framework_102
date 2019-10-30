import unittest
from selenium import webdriver
import time


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path='/Users/sergeygordeev/Desktop/EDU/Python/Python_Selenium_Framework_102/drivers/geckodriver')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

# navigate to the application home page
        cls.driver.get('https://magento.com/products/magento-open-source')

    def test_search_by_category(self):
# get the search textbox
        self.driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Get A Free Demo'])[1]/following::i[1]").click()
        self.search_field = self.driver.find_element_by_xpath(
         "(.//*[normalize-space(text()) and normalize-space(.)='Find what you seek'])[1]/following::input[1]")
        self.search_field.click()
# enter search keyword and submit
        self.search_field.clear()
        self.search_field.send_keys("phones")
        x = self.driver.title
        print(f'{x} search by category')
        self.driver.find_element_by_id("page-search-btn").click()
# get all the anchor elements which have product names
# displayed currently on result page using
# find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//ol[@class='search-results node-results']//h3")
        self.assertEqual(10, len(products))


    def test_search_by_name(self):
# get the search textbox
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Get A Free Demo'])[1]/following::i[1]").click()
        self.search_field = self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Find what you seek'])[1]/following::input[1]")
        self.search_field.click()
        # enter search keyword and submit
        self.search_field.clear()
        self.search_field.send_keys("alumni")
        x = self.driver.title
        print(f'{x} search by name')
        self.driver.find_element_by_id("page-search-btn").click()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//ol[@class='search-results node-results']//h3")
        self.assertEqual(7, len(products))

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
# close window and quit driver
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
