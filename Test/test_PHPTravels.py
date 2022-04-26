import unittest

from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType

from Base.Driver import Driver
from PageObjects import SamplePageObjects
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class PHPTravels(unittest.TestCase):
    base_url = None

    def setUp(self):
        global driver
        driver = Driver("CHROME")
        self.base_url = "https://www.phptravels.net/login"

    @allure.testcase("PHP Travel Incorrect Login")
    def test_php_travel_incorrect_login(self):
        self.navigate_to_webpage()
        self.enter_login_details()

    # def test_simple_navigate(self):
    #     pytest.skip("Will test later")

    @allure.step
    def navigate_to_webpage(self):
        driver.navigate_to(self.base_url)
        allure.attach("Successfully navigated to " + self.base_url, AttachmentType.TEXT)

    @allure.step
    def enter_login_details(self):
        driver.wait_for_element_visible(SamplePageObjects.login_text_header())
        driver.enter_text(SamplePageObjects.login_username_textfield(), "GarthD@gmail.com")
        driver.enter_text(SamplePageObjects.login_password_textfield(), "NotMyPassword")
        driver.click_element(SamplePageObjects.login_button())
        driver.wait_for_element_visible(SamplePageObjects.login_incorrect_user_details_error_message())

    def tearDown(self):
     # allure.attach(driver.take_screenshot("test.png"), name="testLoginScreen", attachment_type=AttachmentType.PNG)
        driver.shut_down()
