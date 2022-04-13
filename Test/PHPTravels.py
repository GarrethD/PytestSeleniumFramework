import unittest
from selenium import webdriver
from Base.Driver import Driver
from PageObjects import SamplePageObjects


class TestExampleOne(unittest.TestCase):

    driver: webdriver
    base_url = None

    def setUp(self):
        global driver
        global base_url
        driver = Driver("CHROME")
        base_url = "https://www.phptravels.net/login"

    def test_attempt_login(self):
        self.navigate_to_webpage()
        self.enter_login_details()

    def navigate_to_webpage(self):
        driver.navigate_to(base_url)

    def enter_login_details(self):
        driver.enter_text(SamplePageObjects.login_username_textfield(), "GarthD@gmail.com")
        driver.enter_text(SamplePageObjects.login_password_textfield(), "NotMyPassword")
        driver.click_element(SamplePageObjects.login_button())
        driver.wait_element(SamplePageObjects.login_incorrect_user_details_error_message())

    def tearDown(self):
        driver.shut_down()