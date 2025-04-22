from operator import truediv

import allure
import  pytest
from allure_commons.types import AttachmentType
from selenium import  webdriver
from pageObject.LoginPage import Login
from utilities.readProperties import ReadConfig

# import the untilities package name . module name and import class name
# By using class we can directly call the static method no need to create class object

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserPassword()

    @allure.severity(allure.severity_level.MINOR)
    def test_homePageTitle(self,setup):
        # use setup fixture to remove duplicate code
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        if act_title == "Cogmento CRM":
            assert True
            self.driver.close()
        else:
            # allure.attach(self.driver.get_screenshot_as_png(),name="Title Not Matched",attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)

        # Creare LoginPage Object
        self.lp = Login(self.driver)

        # Enter User name and Password
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_On_Login_Btn()

        # User Logout successfully
        self.lp.click_On_Logout_btn()


