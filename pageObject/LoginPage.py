from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    textbox_username_name="email"
    textbox_password_name="password"
    button_login_xpath="//div[@class='ui fluid large blue submit button']"
    icon_setting_xpath="(//i[@class='settings icon'])[1]"
    icon_logout_xpath="(//i[@class='power icon'])[1]"
    div_cls_validationmsg_Xpath = "//div[contains(text(),'Something went wrong...')]"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def click_On_Login_Btn(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_On_Logout_btn(self):
        wait = WebDriverWait(self.driver,10)
        setting = wait.until(EC.element_to_be_clickable((By.XPATH,self.icon_setting_xpath)))
        setting.click()
        logout = wait.until(EC.element_to_be_clickable((By.XPATH, self.icon_logout_xpath)))
        logout.click()
        self.driver.close()

    def Verify_invalid_message(self):
        wait = WebDriverWait(self.driver, 15)
        validation = wait.until(EC.visibility_of_element_located((By.XPATH, self.div_cls_validationmsg_Xpath)))
        Validation = validation.text

        if Validation == "Something went wrong...":
            self.driver.find_element(By.NAME, self.textbox_username_name).clear()
            self.driver.find_element(By.NAME,self.textbox_password_name).clear()
        else:
            pass


