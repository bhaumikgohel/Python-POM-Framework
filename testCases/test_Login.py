from operator import truediv

import allure
import  pytest
from allure_commons.types import AttachmentType
from selenium import  webdriver
from pageObject.LoginPage import Login


class Test_001_Login:
    baseURL = "https://ui.cogmento.com/?lang=en"
    username = "bhaumik36@yopmail.com"
    password = "Admin@123"

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
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
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


