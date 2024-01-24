import pytest
from .BaseTest import BaseTest
from pages.CareersPage import CareersPage
from utils.DataReader import DataReader

class TestCareersPage(BaseTest):


    def test_careers_page(self):
        
        careers_page = CareersPage(self.driver)
        careers_page.click_departments()
        
        careers_page.wait_unit_dropdown_menu_displayed()
        assert careers_page.is_dropdown_menu_displayed() == True
        
        careers_page.click_to_choose_department()
        careers_page.wait_unit_department_change()
        assert careers_page.get_department_btn_lbl() == DataReader.careers_department_name
        
        assert careers_page.get_open_jobs() == DataReader.get_careers_total_jobs
        
    
        
        
        
        

        

        
        