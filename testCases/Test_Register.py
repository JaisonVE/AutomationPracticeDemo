import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.RegisterPage import Register
from utillities.customLogger import LogGen
from utillities.readProperties import ReadConfig



class Test_Register:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_reg(self):
        self.logger.info("Starting Registration test")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.reg = Register(self.driver)
        self.reg.click_sign_in()
        self.logger.info("Entering info")
        self.email = self.random_generator() + "@gmail.com"
        self.reg.set_email_create(self.email)
        self.reg.click_create_acc()
        self.reg.click_gender_title("Mr")
        self.reg.set_first_name("Jaison")
        self.reg.set_last_name("V Eapen")
        self.reg.set_email()
        self.reg.set_password("qq123456789")
        self.reg.set_dob("24", "5", "1990")
        self.reg.set_company_name("ABC INC")
        self.reg.set_address("121-B, Bakers street")
        self.reg.set_city("Las vegas")
        self.reg.set_state("California")
        self.reg.set_zip("88905")
        self.reg.set_mobile("4844572315")
        self.reg.click_register()
        self.logger.info("Entered info successfully")
        act_title = self.driver.title
        self.logger.info("Registration test completed")
        ex_title = "My account - My Store"
        if act_title == ex_title:
            self.logger.info("Registration test passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Registration test failed")
            self.driver.quit()
            assert False




    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return "".join(random.choice(chars) for x in range(size))


