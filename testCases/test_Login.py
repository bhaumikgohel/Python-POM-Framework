from operator import truediv

import allure
import  pytest
from allure_commons.types import AttachmentType
from selenium import  webdriver
from pageObject.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# import the untilities package name . module name and import class name
# By using class we can directly call the static method no need to create class object

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserPassword()

    # Create one more variable and call the logger method by using class name LogGen
    logg = LogGen.GenLog()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logg.info("************** Test_001_Login ********************")

        self.logg.info("**************** Verify Home Page Title *************")
        # use setup fixture to remove duplicate code
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        if act_title == "Cogmento CR":
            assert True
            self.logg.info("**************** Home Page Title Test is Passed *************")
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Title Not Matched",attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.logg.error("**************** Home Page Title Test is Failed *************")
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logg.info("**************** Login Test is Started *************")
        self.driver = setup
        self.driver.get(self.baseURL)

        # Creare LoginPage Object
        self.lp = Login(self.driver)

        self.logg.info("**************** Enter Login Credentials *************")
        # Enter User name and Password
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logg.info("**************** Click on Login  *************")
        self.lp.click_On_Login_Btn()
        self.logg.info("**************** Login Successfully  *************")

        # User Logout successfully
        self.logg.info("**************** Logout Test Started  *************")
        self.lp.click_On_Logout_btn()
        self.logg.info("**************** Logout Successfully  *************")


