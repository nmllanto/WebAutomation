from AmazonPOMProject.Locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# Author: Noly Llanto
# Date: 07/21/2019
# Contains methods and actions performed on the Electronic page
# For test scenario, I picked to select headphones

class ElectronicPage():


    def __init__(self, driver):
        self.driver = driver

        self.headphones = Locators.elec_headphone_link_text
        self.boss_sound = Locators.boss_soundlink
        self.add_to_cart = Locators.add_to_cart_id
        self.cart_button = Locators.sidesheet_cart_but

    def select_headphones(self):
        self.driver.find_element_by_link_text(self.headphones).click()
        WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, self.boss_sound)))
        self.driver.find_element_by_xpath(self.boss_sound).click()

    def add_item_to_cart(self):
        self.driver.find_element_by_id(self.add_to_cart).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.cart_button)))
        self.driver.find_element_by_xpath(self.cart_button).click()


