import pytest
import time
from selenium import webdriver
from utils.Configuration import Configuration


@pytest.fixture
def setup_and_teardown(request):
    global driver
    driver = None
    browser = Configuration.default_browser
    driver = initialize_webdriver(browser.lower())
    driver.maximize_window()
    url = Configuration.start_url
    driver.get(url)
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()
    
    
    
def initialize_webdriver(browser):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")