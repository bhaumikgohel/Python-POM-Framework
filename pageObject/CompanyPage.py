from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from LoginPage import Login


class AddCompany:
    icon_user_xpath = "//i[@class='users icon']"
    btn_create_xpath = "(//button[@class='ui linkedin button'])[3]"
    input_firstname_xpath = "//input[@name='first_name']"
    input_lastname_xpath = "//input[@name='last_name']"
    input_email_xpath = "//input[@placeholder='Email address']"
    btn_save_text = "//button//i[@class='save icon']"
    label_firstname_required_xpath = "(//label//span[@class='inline-error-msg'])[1]"
    label_lastname_required_xpath = "(//label//span[@class='inline-error-msg'])[2]"



    def __init__(self,driver):
       self.driver = driver

    def Check_required_message(self):
        self.driver.find_elelment(By.XPATH,'btn_save_text')
        firstnamerequired = self.driver.find_elelment(By.XPATH,self.label_firstname_required_xpath).text
        lastnamerequired = self.driver.find_elelment(By.XPATH, self.label_lastname_required_xpath).text

        if firstnamerequired == "The field First Name is required." | lastnamerequired == "The field Last Name is required.":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def Click_On_Side_Menu_Contact(self):
        self.driver.find_elelment(By.XPATH,self.icon_user_xpath)

    def Set_Username(self,fname):
        self.driver.find_elelment(By.XPATH,self.input_firstname_xpath).clear()
        self.driver.find_elelment(By.XPATH,self.input_firstname_xpath).send_keys(fname)

    def Set_Lastname(self,lname):
        self.driver.find_elelment(By.XPATH,self.input_lastname_xpath).clear()
        self.driver.find_elelment(By.XPATH,self.input_lastname_xpath).send_keys(lname)

    def Set_Emailid(self,email):
        self.driver.find_elelment(By.XPATH,self.input_email_xpath).clear()
        self.driver.find_elelment(By.XPATH,self.input_email_xpath).send_keys(email)

    def Click_On_Save_Button(self):
        self.driver.find_elelment(By.XPATH,self.btn_save_text).click()
