import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.set_capability("acceptInsecureCerts", True)
    driver = webdriver.Remote(command_executor='http://192.168.1.158:4444/wd/hub', options=options)
    driver.maximize_window()
    yield driver
    driver.quit()



