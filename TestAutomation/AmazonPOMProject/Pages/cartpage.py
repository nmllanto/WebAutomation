from AmazonPOMProject.Locators.locators import Locators

# Author: Noly Llanto
# Date: 07/21/2019
# Contains methods and actions performed on the cart page

class CartPage():

    def __init__(self, driver):
        self.driver = driver

        self.cart_item_count = Locators.cart_item_count_id
        self.checkout_payment = Locators.proceed_checkout

    def proceed_to_checkout(self):
        self.driver.find_element_by_xpath(self.checkout_payment).click()

    def check_cart_not_empty(self):
        item_count = int(self.driver.find_element_by_id(self.cart_item_count).text)
        return item_count

