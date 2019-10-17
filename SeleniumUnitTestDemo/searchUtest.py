import unittest
from selenium import webdriver
import time


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/sergeygordeev/Desktop/EDU/Python/Python_Selenium_Framework_102/drivers/geckodriver')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

# navigate to the application home page
        self.driver.get('https://magento.com/products/magento-open-source')

    def test_search_by_category(self):
# get the search textbox
        self.driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Get A Free Demo'])[1]/following::i[1]").click()
        self.search_field = self.driver.find_element_by_xpath(
         "(.//*[normalize-space(text()) and normalize-space(.)='Find what you seek'])[1]/following::input[1]")
        self.search_field.click()
# enter search keyword and submit
        self.search_field.send_keys("phones")
        x = self.driver.title
        print(x)
        self.driver.find_element_by_id("page-search-btn").click()
# get all the anchor elements which have product names
# displayed currently on result page using
# find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//ol[@class='search-results node-results']//h3")
        self.assertEqual(10, len(products))

    def tearDown(self):
        time.sleep(2)
# close window and quit driver
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
