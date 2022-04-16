import unittest
from selenium import webdriver
from Base.Driver import Driver
from PageObjects import SamplePageObjects

driver: webdriver


class PHPTravels(unittest.TestCase):
    base_url = None

    def setUp(self):
        global driver
        driver = Driver("CHROME")
        self.base_url = "https://www.phptravels.net/login"

    def test_php_travel_incorrect_login(self):
        self.navigate_to_webpage()
        self.enter_login_details()

    # def test_simple_navigate(self):
    #     self.navigate_to_webpage()

    def navigate_to_webpage(self):
        driver.navigate_to(self.base_url)

    def enter_login_details(self):
        driver.wait_for_element_visible(SamplePageObjects.login_text_header())
        driver.enter_text(SamplePageObjects.login_username_textfield(), "GarthD@gmail.com")
        driver.enter_text(SamplePageObjects.login_password_textfield(), "NotMyPassword")
        driver.click_element(SamplePageObjects.login_button())
        driver.wait_for_element_visible(SamplePageObjects.login_incorrect_user_details_error_message())

    def tearDown(self):
        driver.shut_down()
