import time
from tokenize import String
import pytest
from pageObject.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.CompanyPage import AddCompany


class Test_003_Addcontact:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserPassword()

    logg = LogGen.GenLog()
    @pytest.mark.sanity
    def test_verify_required_msg(self,setup):
        self.logg.info("*********** Test_003_AddContact ************")

        self.driver = setup
        self.driver.get(self.url)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_On_Login_Btn()

        self.logg.info("********** Login Successfully **********")

        self.addcontact = AddCompany(self.driver)

        time.sleep(10)

        message  = self.addcontact.Check_required_message()

        expected_messages = ["The field First Name is required.", "The field Last Name is required."]

        assert message == expected_messages

        self.driver.close()


