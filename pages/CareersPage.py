from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utils.DataReader import DataReader

class CareersPage(BasePage):
    
    __departments_btn = "//button[@id='sl']"
    __departments_ddl = "//div[contains(@class, 'dropdown-menu show')]"
    __department_lbl = f"//a[contains(text(), '{DataReader.careers_department_name}')]"
    __department_selected_btn = f"//button[contains(@class, 'selected')][contains(text(), '{DataReader.careers_department_name}')]"
    __department_jobs_lnk = "//a[contains(@class, 'card')]"
    
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def get_department_btn_lbl(self):
        return self._get_element(By.XPATH, self.__department_selected_btn).text
           
    def click_departments(self):
        self._click(By.XPATH, self.__departments_btn)
        
    def click_to_choose_department(self):
        self._click(By.XPATH, self.__department_lbl)
        
    def get_open_jobs(self):
        return len(self._get_elements(By.XPATH, self.__department_jobs_lnk))
    
    def is_dropdown_menu_displayed(self):
        return self._is_displayed(By.XPATH, self.__departments_ddl)
    
    def wait_unit_dropdown_menu_displayed(self):
        self._wait_until_displayed(By.XPATH, self.__departments_ddl)
        
    def wait_unit_department_change(self):
        self._wait_until_displayed(By.XPATH, self.__department_selected_btn)
        
    
        
        
    