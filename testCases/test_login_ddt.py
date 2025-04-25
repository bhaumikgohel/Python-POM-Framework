import time
from operator import truediv

import allure
from allure_commons.types import AttachmentType
from pageObject.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import Excelutilities

# import the untilities package name . module name and import class name
# By using class we can directly call the static method no need to create class object

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "./TestData/Login_Testdata.xlsx"
    logg = LogGen.GenLog()

    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self,setup):
        self.logg.info("************* Test_002_DDT_Login_Testcase ***********")
        self.logg.info("**************** Login Test is Started *************")
        self.driver = setup
        self.driver.get(self.baseURL)

        # Creare LoginPage Object
        self.lp = Login(self.driver)

        self.logg.info("********** Get Data from Excel File from Untilities **********")
        self.rows = Excelutilities.getRowCount(self.path,"Sheet1")
        print("Numebr of Rows in excel is :" + str(self.rows))

        self.cols = Excelutilities.getColCount(self.path,'Sheet1')

        for r in range(2,self.rows + 1):

            self.user = Excelutilities.readData(self.path,'Sheet1',r,1)
            self.password = Excelutilities.readData(self.path,'Sheet1',r,2)


            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)

            self.lp.click_On_Login_Btn()



            act_title = self.driver.title

            if act_title == "Cogmento CRM":
               self.driver.close()




