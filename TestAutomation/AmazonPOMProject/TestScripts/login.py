import unittest
import time
from selenium import webdriver
from AmazonPOMProject.Pages.loginpage import LoginPage
from AmazonPOMProject.Pages.homepage import HomePage
import HtmlTestRunner

# Author: Noly Llanto
# Date: 07/21/2019
# Test Scenario: Different login attempt to https://www.amazon.com/

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/nolyllanto/PycharmProjects/TestAutomation/driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        """
        Script to login with valid email and password
        :return: none
        """
        driver = self.driver

        signin = LoginPage(driver)
        home = HomePage(driver)

        home.navigate_to_site()
        time.sleep(2)
        signin.enter_signin_email("nmllanto@gmail.com")
        signin.enter_signin_password("testing321")
        signin.click_sign_in()
        home.is_signin_successful()

    def test_invalid_password(self):
        driver = self.driver
        expected_error = "Your password is incorrect"

        signin = LoginPage(driver)
        home = HomePage(driver)

        home.navigate_to_site()
        time.sleep(2)
        signin.enter_signin_email("nmllanto@gmail.com")
        signin.enter_signin_password("testing123")
        signin.click_sign_in()
        error_message = signin.invalid_password()
        self.assertEqual(error_message, expected_error)

    def test_invalid_email(self):
        driver = self.driver
        expected_error = "We cannot find an account with that email address"

        signin = LoginPage(driver)
        home = HomePage(driver)

        home.navigate_to_site()
        time.sleep(2)
        signin.enter_signin_email("nmllnto@gmail.com")
        signin.enter_signin_password("testing123")
        signin.click_sign_in()
        error_message = signin.account_not_existing()
        self.assertEqual(error_message, expected_error)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/nolyllanto/PycharmProjects/TestAutomation/AmazonPOMProject/Reports'))
