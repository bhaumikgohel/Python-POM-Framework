from selenium import  webdriver
import  pytest
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, visibility_of
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.delete_all_cookies()
    elif browser == "firefox":
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.delete_all_cookies()
    elif browser == "edge":
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.delete_all_cookies()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# ############### pytest HTML Reports ##################

def pytest_configure(config):
    config.option.metadata = True

def pytest_metadata(metadata):
    metadata['Project Name'] = 'FREE CRM'
    metadata['Module Name'] = 'Login Logout'
    metadata['Tester'] = 'Bhaumik Gohel'
    return metadata

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home",None)
    metadata.pop("Plugins",None)