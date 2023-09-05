import time

import locators
from pages.base_page import BasePage


class PythonSite(BasePage):
    def test_click_title(self):
        click_link = self.driver.find_element(*locators.Main.PYTHON_PAGE1)
        click_link.click()
        time.sleep(12)
        click_link = self.driver.find_element(*locators.Main.PYTHON_PAGE2)
        click_link.click()
        time.sleep(10)
        click_link = self.driver.find_element(*locators.Main.PYTHON_PAGE3)
        click_link.click()
        time.sleep(10)