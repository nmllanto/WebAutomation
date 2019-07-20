import unittest
import time
from selenium import webdriver
from AmazonPOMProject.Pages.loginpage import LoginPage
from AmazonPOMProject.Pages.homepage import HomePage
import HtmlTestRunner

# Author: Noly Llanto
# Date: 07/21/2019
# Test Scenario: logout from https://www.amazon.com/

class LogoutTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/nolyllanto/PycharmProjects/TestAutomation/driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_logout(self):
        driver = self.driver

        signin = LoginPage(driver)
        home = HomePage(driver)

        home.navigate_to_site()
        time.sleep(2)
        signin.enter_signin_email("nmllanto@gmail.com")
        signin.enter_signin_password("testing321")
        signin.click_sign_in()
        home.is_signin_successful()
        home.hover_account()
        time.sleep(2)
        home.logout()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/nolyllanto/PycharmProjects/TestAutomation/AmazonPOMProject/Reports'))
