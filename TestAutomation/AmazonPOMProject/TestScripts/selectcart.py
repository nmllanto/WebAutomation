import unittest
import time
from selenium import webdriver
from AmazonPOMProject.Pages.homepage import HomePage
from AmazonPOMProject.Pages.loginpage import LoginPage

# Author: Noly Llanto
# Date: 07/21/2019
# Test Scenario: Login to site then navigate to cart page

class SelectCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/nolyllanto/PycharmProjects/TestAutomation/driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_goto_cart(self):
        driver = self.driver

        home = HomePage(driver)
        signin = LoginPage(driver)

        home.navigate_to_site()
        time.sleep(2)
        signin.enter_signin_email("nmllanto@gmail.com")
        signin.enter_signin_password("testing321")
        signin.click_sign_in()
        home.go_to_cart()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        if __name__ == '__main__':
            unittest.main()
