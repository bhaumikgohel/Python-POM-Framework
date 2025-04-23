from selenium import  webdriver
import  pytest

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



