import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


@pytest.fixture()
def setup(request):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
        "--window-size=1920,1080",
        "--ignore-certificate-errors",
    ]
    for option in options:
        chrome_options.add_argument(option)

    request.cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    yield request.cls.driver
    request.cls.driver.close()
