from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.Configuration import Configuration

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Configuration.timeout)
        
    def _click(self, by, locator_value):
        element = self._get_element(by, locator_value)
        element.click() 
        
    def _send_keys(self, by, locator_value, text):
        element = self._get_element(by, locator_value)
        element.clear()
        element.send_keys(text)
        
    def _is_displayed(self, by, locator_value):
        element = self._get_element(by, locator_value)
        return element.is_displayed()
       
    def _get_element(self, by, locator_value):
        element = None
        element = self.driver.find_element(by=by, value=locator_value)
        return element
    
    def _get_elements(self, by, locator_value):
        elements = None
        elements = self.driver.find_elements(by=by, value=locator_value)
        return elements
    
    def _wait_until_displayed(self, by, locator_value):
        element = self.wait.until(EC.element_to_be_clickable((by,locator_value)))