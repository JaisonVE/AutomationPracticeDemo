from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Register:
    btn_sign_in_xpath = "//a[normalize-space()='Sign in']"
    txt_email_create_xpath = "//input[@id='email_create']"
    btn_create_account_xpath = "//span[normalize-space()='Create an account']"
    rad_mr_xpath = "//input[@id='id_gender1']"
    rad_mrs_xpath = "//input[@id='id_gender2']"
    txt_first_name_xpath = "//input[@id='customer_firstname']"
    txt_last_name_xpath = "//input[@id='customer_lastname']"
    txt_email_xpath = "//input[@id='email']"
    txt_password_xpath = "//input[@id='passwd']"
    drdn_date_xpath = "//select[@id='days']"
    drdn_month_xpath = "//select[@id='months']"
    drdn_year_xpath = "//select[@id='years']"
    txt_company_name_xpath = "//input[@id='company']"
    txt_address_xpath = "//input[@id='address1']"
    txt_city_xpath = "//input[@id='city']"
    drdn_state_xpath = "//select[@id='id_state']"
    txt_postcode_xpath = "//input[@id='postcode']"
    txt_mobile_xpath = "//input[@id='phone_mobile']"
    btn_register_xpath = "//span[text()='Register']"

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.btn_sign_in_xpath).click()

    def set_email_create(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_create_xpath).send_keys(email)

    def click_create_acc(self):
        self.driver.find_element(By.XPATH, self.btn_create_account_xpath).click()

    def click_gender_title(self, gender):
        if gender == "Mr":
            self.driver.find_element(By.XPATH, self.rad_mr_xpath).click()
        elif gender == "Mrs":
            self.driver.find_element(By.XPATH, self.rad_mrs_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rad_mr_xpath).click()

    def set_first_name(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_first_name_xpath).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_last_name_xpath).send_keys(lastname)

    def set_email(self):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).click()

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def set_dob(self, date, month, year):
        dob_date = Select(self.driver.find_element(By.XPATH, self.drdn_date_xpath))
        dob_date.select_by_value(date)
        dob_month = Select(self.driver.find_element(By.XPATH, self.drdn_month_xpath))
        dob_month.select_by_value(month)
        dob_year = Select(self.driver.find_element(By.XPATH, self.drdn_year_xpath))
        dob_year.select_by_value(year)

    def set_company_name(self, companyname):
        self.driver.find_element(By.XPATH, self.txt_company_name_xpath).send_keys(companyname)

    def set_address(self, address):
        self.driver.find_element(By.XPATH, self.txt_address_xpath).send_keys(address)

    def set_city(self, city):
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(city)

    def set_state(self,state):
        states = Select(self.driver.find_element(By.XPATH, self.drdn_state_xpath))
        states.select_by_visible_text(state)

    def set_zip(self, postcode):
        self.driver.find_element(By.XPATH, self.txt_postcode_xpath).send_keys(postcode)

    def set_mobile(self, mobile):
        self.driver.find_element(By.XPATH, self.txt_mobile_xpath).send_keys(mobile)

    def click_register(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()



