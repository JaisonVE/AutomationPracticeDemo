from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from utillities.excelUtillities import ExcelData
from pageObjects.ProductOrdering import ProductOrdering
from pageObjects.AccountPage import AccountPage
from utillities.customLogger import LogGen
from utillities.readProperties import ReadConfig


class Test_Product:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_product_ordering(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("Started Product Ordering test")
        self.acc = AccountPage(self.driver)
        self.logger.info("Logging in")
        self.acc.click_sign_in()
        self.acc.set_email("jaisoneapen29@gmail.com")
        self.acc.set_password("qq123456789")
        self.acc.click_login()
        self.logger.info("Successfully Logged in")
        self.prod = ProductOrdering(self.driver)
        self.prod.set_search("printed dress")
        self.logger.info("searching product")
        self.prod.click_dress1()
        self.prod.set_dress("1", "M")
        self.prod.dress_colour("Blue")
        self.prod.click_add_cart()
        self.logger.info("Added dress to cart")
        self.prod.view_cart()
        product = self.driver.find_element(By.XPATH, "//td[@class='cart_description']//p").text
        if product == "Printed Summer Dress":
            self.logger.info("Dress added successfully to cart")
            assert True
        else:
            self.logger.info("Dress not added to cart")
            assert False

        self.prod.click_checkout()

        file = "C:\\Users\\user\\PycharmProjects\\AutomationPracticeDemo\\TestData\\Address.xlsx"
        workbook = openpyxl.load_workbook(file)
        sheet = workbook["Sheet2"]
        self.excel = ExcelData(self.driver)
        lst_status1 = []

        for x in range(2, 7):
            address = self.driver.find_element(By.XPATH, "//ul[@id='address_delivery']//li[" + str(x) + "]").text
            r = x - 1
            ex_address = self.excel.readdata(file, "Sheet2", r, 1)
            if address == ex_address:
                lst_status1.append("Pass")
                assert True
            else:
                lst_status1.append("Fail")
                assert False

        if "Fail" not in lst_status1:
            self.logger.info("Delivery address info status test passed")
        else:
            self.logger.info("Delivery address info status test failed")

        lst_status2 = []

        for x in range(2, 7):
            address = self.driver.find_element(By.XPATH, "//ul[@id='address_invoice']//li[" + str(x) + "]").text
            r = x - 1
            ex_address = self.excel.readdata(file, "Sheet2", r, 1)
            if address == ex_address:
                lst_status2.append("Pass")
                assert True
            else:
                lst_status2.append("Fail")
                assert False

        if "Fail" not in lst_status2:
            self.logger.info("Invoice address info status test passed")
        else:
            self.logger.info("Invoice address info status test failed")

        self.prod.click_checkout()
        self.prod.click_ship_checkout()
        self.prod.click_pay_by_wire()
        self.prod.click_confirm_order()
        self.logger.info("Ended Product Ordering test successfully")
        self.driver.quit()
