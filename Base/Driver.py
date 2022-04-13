import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


class Driver:
    driver: webdriver

    def __init__(self, browser_name):
        self.selenium_driver(browser_name)

    def selenium_driver(self, browser_name):
        match str(browser_name).upper():
            case "CHROME":
                self.initialize_chrome_driver()
            case "FIREFOX":
                self.initialize_gecko_driver()
            case default:
                return print("Unable to generate driver with specified browser -", browser_name)

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
        driver.get(url)

    def shut_down(self):
        driver.quit()
