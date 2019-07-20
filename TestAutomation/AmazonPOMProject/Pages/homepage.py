from AmazonPOMProject.Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# Author: Noly Llanto
# Date: 07/21/2019
# Contains methods and actions performed on the home page

class HomePage():


    def __init__(self, driver):
        self.driver = driver

        self.username = Locators.home_username
        self.cartlink = Locators.home_cartlink
        self.department = Locators.home_department
        self.electronic = Locators.dept_electronic
        self.signout = Locators.home_logout_id
        self.account = Locators.home_account_id

    def is_signin_successful(self):
        expected_user = "nolyl"
        user_name = self.driver.find_element_by_xpath(self.username).text
        assert user_name == "Hello, " + expected_user

    def navigate_to_site(self):
        self.driver.get("https://www.amazon.com/")
        self.driver.find_element_by_id(self.account).click()

    def go_to_cart(self):
        self.driver.find_element_by_id(self.cartlink).click()

    def hover_department(self):
        to_dept = self.driver.find_element_by_id(self.department)
        ActionChains(self.driver).move_to_element(to_dept).perform()

    def select_electronic_dept(self):
        WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, self.electronic)))
        self.driver.find_element_by_xpath(self.electronic).click()

    def hover_account(self):
        to_account = self.driver.find_element_by_id(self.account)
        ActionChains(self.driver).move_to_element(to_account).perform()

    def logout(self):
        WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.ID, self.signout)))
        self.driver.find_element_by_id(self.signout).click()