from selenium import webdriver
import time

# create a new Firefox session
driver = webdriver.Firefox(executable_path='/Users/sergeygordeev/Desktop/EDU/Python/Python_Selenium_Framework_102/drivers/geckodriver')
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to application home page
driver.get("https://magento.com/products/magento-open-source")

# get the search textbox
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Get A Free Demo'])[1]/following::i[1]").click()

search_field = driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Find what you seek'])[1]/following::input[1]")
search_field.click()
search_field.clear()

# enter search keyword and submit
search_field.send_keys('glasses')
driver.find_element_by_id("page-search-btn").click()

# get all the anchor elements which have product names displayed
products = driver.find_elements_by_xpath("//ol[@class='search-results node-results']//h3")

# # get the number of anchor elements found
print("Found " + str(len(products)) + " products:")

# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print(product.text)
# # close the browser window
time.sleep(2)
driver.close()
driver.quit()





