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

    def test_google_navigate(self):
        self.navigate_to_webpage()

    def navigate_to_webpage(self):
        driver.navigate_to("https://www.phptravels.net/login")
        print("Succesfully navigaated to " + self.base_url)

    def tearDown(self):
        driver.shut_down()