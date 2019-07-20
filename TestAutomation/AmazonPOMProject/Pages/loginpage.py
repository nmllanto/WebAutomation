from AmazonPOMProject.Locators.locators import Locators

# Author: Noly Llanto
# Date: 07/21/2019
# Contains methods and actions performed on the login page

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_id = Locators.signin_email_id
        self.password_id = Locators.signin_password_id
        self.signin_but_id = Locators.signin_but_id
        self.incorrect_pass = Locators.incorrect_pass

    def enter_signin_email(self, email):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def enter_signin_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element_by_id(self.signin_but_id).click()

    def invalid_password(self):
        return self.driver.find_element_by_xpath(self.incorrect_pass).text

    def account_not_existing(self):
        return self.driver.find_element_by_xpath(self.incorrect_pass).text
