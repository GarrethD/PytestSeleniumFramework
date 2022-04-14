from asyncio import sleep

import webdriver_manager.chrome
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, SessionNotCreatedException, \
    ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UnreachableBrowserException:
    pass


class Driver:
    driver: webdriver
    global_timeout = 30

    def __init__(self, browser_name):
        self.selenium_driver(browser_name)

    def selenium_driver(self, browser_name):
        try:
            match str(browser_name).upper():
                case "CHROME":
                    self.initialize_chrome_driver()
                case "FIREFOX":
                    self.initialize_gecko_driver()
                case default:
                    return print("Unable to generate driver with specified browser -", browser_name)
        except UnreachableBrowserException as ex:
            print("Failed to open browser.", ex)

    def initialize_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        service = ChromeService(executable_path=webdriver_manager.chrome.ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def initialize_gecko_driver(self):
        profile = webdriver.FirefoxOptions()
        profile.set_preference("dom.webnotifications.serviceworker.enabled", False)
        profile.set_preference("dom.webnotifications.enabled", False)
        service = FirefoxService(executable_path=webdriver_manager.chrome.ChromeDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=profile)

    def navigate_to(self, url):
        try:
            self.driver.get(url)
        except SessionNotCreatedException as ex:
            print("Failed to navigate to url.", ex.msg)

    def wait_for_element_visible(self, xpath):
        element: WebElement
        try:
            WebDriverWait(self.driver, self.global_timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except ElementNotVisibleException as ex:
            print("Element not visible.", ex.msg)

    def click_element(self, xpath):
        try:
            self.wait_for_element_visible(xpath)
            self.driver.find_element(By.XPATH, xpath).click()
        except ElementNotVisibleException as ex:
            print("Element not visible.", ex.msg)
        except ElementClickInterceptedException as ex:
            print("Element not intractable.", ex.msg)

    def enter_text(self, xpath, text_to_enter):
        try:
            self.wait_for_element_visible(xpath)
            self.driver.find_element(By.XPATH, xpath).send_keys(text_to_enter)
        except ElementClickInterceptedException as ex:
            print("Element not intractable.", ex.msg)

    def shut_down(self):
        self.driver.quit()
