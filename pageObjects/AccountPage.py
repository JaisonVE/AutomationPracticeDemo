from selenium.webdriver.common.by import By


class AccountPage:
    img_logo_xpath = "//img[@alt='My Store']"
    btn_sign_in_xpath = "//a[normalize-space()='Sign in']"
    txt_email_xpath = "//input[@id='email']"
    txt_password_xpath = "//input[@id='passwd']"
    btn_log_in_xpath = "//span[normalize-space()='Sign in']"
    btn_order_xpath = "//span[normalize-space()='Order history and details']"
    btn_credit_slips_xpath = "//span[normalize-space()='My credit slips']"
    btn_address_xpath = "//span[normalize-space()='My addresses']"
    btn_personal_info_xpath = "//span[normalize-space()='My personal information']"
    btn_wishlists_xpath = "//span[normalize-space()='My wishlists']"
    btn_sign_out_xpath = "//a[@class='logout']"

    def __init__(self, driver):
        self.driver = driver

    def find_logo(self):
        self.driver.find_element(By.XPATH, self.img_logo_xpath)


    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.btn_sign_in_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_log_in_xpath).click()

    def click_order_page(self):
        self.driver.find_element(By.XPATH, self.btn_order_xpath).click()

    def click_credit_slips(self):
        self.driver.find_element(By.XPATH, self.btn_credit_slips_xpath).click()

    def click_personal_info(self):
        self.driver.find_element(By.XPATH, self.btn_personal_info_xpath).click()

    def click_wish_lists(self):
        self.driver.find_element(By.XPATH, self.btn_wishlists_xpath).click()

    def click_address(self):
        self.driver.find_element(By.XPATH, self.btn_address_xpath).click()

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.btn_sign_in_xpath).click()

    def click_sign_out(self):
        self.driver.find_element(By.XPATH, self.btn_sign_out_xpath).click()



