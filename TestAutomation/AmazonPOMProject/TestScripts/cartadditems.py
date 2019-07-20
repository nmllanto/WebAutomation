import unittest
import time
from selenium import webdriver
from AmazonPOMProject.Pages.homepage import HomePage
from AmazonPOMProject.Pages.loginpage import LoginPage
from AmazonPOMProject.Pages.electronicspage import ElectronicPage

# Author: Noly Llanto
# Date: 07/21/2019
# Test Scenario: Adding item/s to cart

class CartAddItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/nolyllanto/PycharmProjects/TestAutomation/driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_add_items_cart(self):
        driver = self.driver

        home = HomePage(driver)
        signin = LoginPage(driver)
        electronic = ElectronicPage(driver)

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


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        if __name__ == '__main__':
            unittest.main()
