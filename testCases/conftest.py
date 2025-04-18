import pytest
from selenium import  webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    return driver