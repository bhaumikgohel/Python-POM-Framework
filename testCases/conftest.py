import pytest
from pytest_metadata.plugin import pytest_addoption
from selenium import  webdriver
import  pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.delete_all_cookies()
    elif browser == "fireFox":
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.delete_all_cookies()
    return driver


def pytest_addoption(parser):
    parser.addoption("--broser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--broser")



