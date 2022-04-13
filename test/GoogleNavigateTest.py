import unittest

from selenium import webdriver

from Base.Driver import Driver


class TestExampleOne(unittest.TestCase):

    driver: webdriver

    def setUp(self):
        global driver
        driver = Driver("CHROME")

    def test_google_navigate(self):
        driver.navigate_to("https://www.google.com")

    def tearDown(self):
        driver.shut_down()