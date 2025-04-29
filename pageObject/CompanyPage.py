from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, visibility_of
from selenium.webdriver.support.wait import WebDriverWait



class AddCompany:
    icon_user_xpath = "//a//i[@class='users icon']"
    btn_create_xpath = "(//button[@class='ui linkedin button'])[3]"
    input_firstname_xpath = "//input[@name='first_name']"
    input_lastname_xpath = "//input[@name='last_name']"
    input_email_xpath = "//input[@placeholder='Email address']"
    btn_Creat_Xpath = "(//button[@class='ui linkedin button'])[3]"
    btn_save_text = "//button//i[@class='save icon']"
    label_firstname_required_xpath = "(//span[@class='inline-error-msg'])[1]"
    label_lastname_required_xpath = "(//span[@class='inline-error-msg'])[2]"



    def __init__(self,driver):
       self.driver = driver

    def Check_required_message(self):

        user= self.driver.find_element(By.XPATH, self.icon_user_xpath)
        user.click()

        self.driver.find_element(By.XPATH, self.btn_Creat_Xpath).click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located(self.driver.find_element(By.XPATH, self.btn_save_text)))

        self.driver.find_element(By.XPATH,self.btn_save_text).click()

        firstnamerequired = self.driver.find_element(By.XPATH,self.label_firstname_required_xpath)
        firstnamerequired = firstnamerequired.text

        lastnamerequired = self.driver.find_element(By.XPATH, self.label_lastname_required_xpath)
        lastnamerequired = lastnamerequired.text

        return [firstnamerequired,lastnamerequired]

    def Click_On_Side_Menu_Contact(self):
        self.driver.find_element(By.XPATH,self.icon_user_xpath)

    def Set_Username(self,fname):
        self.driver.find_element(By.XPATH,self.input_firstname_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_firstname_xpath).send_keys(fname)

    def Set_Lastname(self,lname):
        self.driver.find_element(By.XPATH,self.input_lastname_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_lastname_xpath).send_keys(lname)

    def Set_Emailid(self,email):
        self.driver.find_element(By.XPATH,self.input_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_email_xpath).send_keys(email)

    def Click_On_Save_Button(self):
        self.driver.find_element(By.XPATH,self.btn_save_text).click()
