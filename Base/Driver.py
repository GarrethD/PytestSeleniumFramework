from time import sleep

import webdriver_manager.chrome
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, SessionNotCreatedException, \
    ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webelement import WebElement


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
        global driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        service = ChromeService(executable_path=webdriver_manager.chrome.ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    def initialize_gecko_driver(self):
        global driver
        profile = webdriver.FirefoxOptions()
        profile.set_preference("dom.webnotifications.serviceworker.enabled", False)
        profile.set_preference("dom.webnotifications.enabled", False)
        service = FirefoxService(executable_path=webdriver_manager.chrome.ChromeDriverManager().install())
        driver = webdriver.Firefox(service=service, options=profile)

    def navigate_to(self, url):
        try:
            driver.get(url)
        except SessionNotCreatedException as ex:
            print("Failed to navigate to url.", ex.msg)

    def is_element_visible(self, xpath):
        is_visible = False
        timer = 30
        element: WebElement
        try:
            while timer <= self.global_timeout:
                sleep(1000)
                is_visible = driver.find_elements(By.XPATH, xpath).size() < 1
                if is_visible:
                    element = driver.find_element(By.XPATH, xpath)
                    if element.is_displayed() and element.is_enabled():
                        break
                    else:
                        timer += 1
        except ElementNotVisibleException as ex:
            print("Element not visible.", ex.msg)
        finally:
            return is_visible

    def wait_for_element_visible(self, xpath):
        if not self.is_element_visible(xpath):
            print("Failed to wait for element to be visible.")

    def click_element(self, xpath):
        try:
            self.wait_for_element_visible(xpath)
        except ElementNotVisibleException as ex:
            print("Element not visible.", ex.msg)
        except ElementClickInterceptedException as ex:
            print("Element not intractable.", ex.msg)
        finally:
            driver.find_element(By.XPATH, xpath).click()

    def enter_text(self, xpath, text_to_enter):
        try:
            self.wait_for_element_visible(xpath)
        except ElementClickInterceptedException as ex:
            print("Element not intractable.", ex.msg)
        finally:
            driver.find_element(By.XPATH, xpath).send_keys(text_to_enter)

    def shut_down(self):
        driver.quit()
