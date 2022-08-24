from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from utillities.readProperties import ReadConfig
from utillities.excelUtillities import ExcelData
from pageObjects.AccountPage import AccountPage
from utillities.customLogger import LogGen



class Test_Account:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_account_page(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("Started Account Status test")
        self.acc = AccountPage(self.driver)
        self.acc.click_sign_in()
        self.acc.set_email("jaisoneapen29@gmail.com")
        self.acc.set_password("qq123456789")
        self.acc.click_login()
        a_title = self.driver.title
        e_title = "My account - My Store"
        if a_title == e_title:
            self.logger.info("Account page login test passed")
            assert True
        else:
            self.logger.info("Account page login test failed")
            assert False

        self.acc.click_order_page()
        a_title = self.driver.title
        e_title = "Order history - My Store"
        if a_title == e_title:
            self.logger.info("Order page test passed")
            assert True
        else:
            self.logger.info("Order page test failed")
            assert False
        self.driver.back()

        self.acc.click_credit_slips()
        a_title = self.driver.title
        e_title = "Order slip - My Store"
        if a_title == e_title:
            self.logger.info("Credit slips page test passed")
            assert True
        else:
            self.logger.info("Credit slips page test failed")
            assert False
        self.driver.back()

        self.acc.click_personal_info()
        a_title = self.driver.title
        e_title = "Identity - My Store"
        if a_title == e_title:
            self.logger.info("Personal info page test passed")
            assert True
        else:
            self.logger.info("Personal info page test failed")
            assert False
        self.driver.back()

        self.acc.click_wish_lists()
        a_title = self.driver.title
        e_title = "My Store"
        if a_title == e_title:
            self.logger.info("Wish list page test passed")
            assert True
        else:
            self.logger.info("Wish list page test failed")
            assert False
        self.driver.back()

        self.acc.click_address()
        a_title = self.driver.title
        e_title = "Addresses - My Store"
        if a_title == e_title:
            self.logger.info("Address page login test passed")
            assert True
        else:
            self.logger.info("Address page login test failed")
            assert False

        file = "C:\\Users\\user\\PycharmProjects\\AutomationPracticeDemo\\TestData\\Address.xlsx"
        workbook = openpyxl.load_workbook(file)
        sheet = workbook["Sheet1"]
        self.excel = ExcelData(self.driver)

        lst_status = []

        for x in range(2, 9):
            address = self.driver.find_element(By.XPATH, "//ul[@class='last_item item box']//li[" +str(x)+ "]").text
            r = x - 1
            ex_address = self.excel.readdata(file, "Sheet1", r, 1)
            if address == ex_address:
                lst_status.append("Pass")
            else:
                lst_status.append("Fail")


        if "Fail" not in lst_status:
            self.logger.info("Account address info status test passed")
        else:
            self.logger.info("Account address info status test passed")

        self.acc.click_sign_out()

        a_title = self.driver.title
        e_title = "Login - My Store"
        if a_title == e_title:
            self.logger.info("Account page logout test passed")
            assert True
        else:
            self.logger.info("Account page logout test failed")
            assert False

        self.logger.info("Ended Account Status test successfully")

        self.driver.quit()


