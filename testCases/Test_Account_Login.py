from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from utillities.readProperties import ReadConfig
from utillities.excelUtillities import ExcelData
from pageObjects.AccountPage import AccountPage
from utillities.customLogger import LogGen



class Test_Account_Login:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_account_login(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("Starting Account Login Data driven test")
        self.acc = AccountPage(self.driver)
        self.acc.click_sign_in()

        file = "C:\\Users\\user\\PycharmProjects\\AutomationPracticeDemo\\TestData\\LoginData.xlsx"
        workbook = openpyxl.load_workbook(file)
        sheet = workbook["Sheet1"]
        self.excel = ExcelData(self.driver)

        self.rows = self.excel.getrowcount(file, "Sheet1")
        lst_status=[]

        for r in range(2, self.rows+1):
            self.user = self.excel.readdata(file, "Sheet1", r, 1)
            self.password = self.excel.readdata(file, "Sheet1", r, 2)
            self.exp = self.excel.readdata(file, "Sheet1", r, 3)
            self.acc.set_email(self.user)
            self.acc.set_password(self.password)
            self.acc.click_login()
            a_title = self.driver.title
            e_title = "My account - My Store"
            if a_title == e_title:
                if self.exp == "Pass":
                    self.acc.click_sign_out()
                    lst_status.append("Pass")
                else:
                    self.acc.click_sign_out()
                    lst_status.append("Fail")
            elif a_title != e_title:
                if self.exp == "Pass":
                    lst_status.append("Fail")
                else:
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Account login test passed")
        else:
            self.logger.info("Account login test failed")

        self.logger.info("Ended Account Login Data driven test successfully")

        self.driver.quit()






