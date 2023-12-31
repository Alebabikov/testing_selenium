import time

from pages.base_page import link
from pages.login_page import PythonSite
import allure



class TestP:
    @allure.feature('click title')
    @allure.story('clickability')
    def test_click(self, driver):
        login_page = PythonSite(driver, link)
        login_page.open()
        login_page.test_click_title()

