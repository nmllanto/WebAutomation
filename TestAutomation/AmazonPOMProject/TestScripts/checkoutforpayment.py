import unittest
import time
from selenium import webdriver
from AmazonPOMProject.Pages.homepage import HomePage
from AmazonPOMProject.Pages.loginpage import LoginPage
from AmazonPOMProject.Pages.electronicspage import ElectronicPage
from AmazonPOMProject.Pages.cartpage import CartPage

# Author: Noly Llanto
# Date: 07/21/2019
# Test Scenario: Checking out for payment options

class CheckoutPaymentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/nolyllanto/PycharmProjects/TestAutomation/driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_checkout_payment(self):
        driver = self.driver

        home = HomePage(driver)
        signin = LoginPage(driver)
        electronic = ElectronicPage(driver)
        cart = CartPage(driver)

        home.navigate_to_site()
        time.sleep(2)

        # login valid account
        signin.enter_signin_email("nmllanto@gmail.com")
        signin.enter_signin_password("testing321")
        signin.click_sign_in()

        #navigate to cart page
        home.go_to_cart()

        # navigate to electronics page to add items in cart
        home.hover_department()
        home.select_electronic_dept()

        # Add a headphone to cart
        electronic.select_headphones()
        electronic.add_item_to_cart()

        # Verify cart is not empty
        item_count = cart.check_cart_not_empty()
        self.assertGreater(item_count, 0, "Cart is Empty")

        # Proceed to checkout payment option page
        cart.proceed_to_checkout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        if __name__ == '__main__':
            unittest.main()
