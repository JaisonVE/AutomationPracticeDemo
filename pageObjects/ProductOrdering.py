from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductOrdering:
    txt_search_xpath = "//input[@id='search_query_top']"
    btn_search_xpath = "//button[@class='btn btn-default button-search']"
    btn_dress1_xpath = "(//div[@class='right-block']//a[@title='Printed Summer Dress'])[1]"
    btn_dress2_xpath = "(//div[@class='right-block']//a[@title='Printed Dress'])[1]"
    txt_quantity_xpath = "//input[@id='quantity_wanted']"
    drdn_size_xpath = "//select[@id='group_1']"
    btn_add_cart_xpath = "//button[normalize-space()='Add to cart']"
    btn_continue_xpath = "//span[normalize-space()='Continue shopping']"
    btn_view_cart_xpath = "//a[@title='View my shopping cart']"
    btn_checkout_xpath = "//span[text()='Proceed to checkout']"
    btn_ship_checkout_xpath = "//button[@name='processCarrier']//span[normalize-space()='Proceed to checkout']"
    check_terms_xpath = "//input[@id='cgv']"
    btn_pay_by_wire_xpath = "//a[@class='bankwire']"
    btn_pay_by_check_xpath = "//a[@class='cheque']"
    btn_order_confirmation_xpath = "//span[text()='I confirm my order']"


    def __init__(self, driver):
        self.driver = driver

    def set_search(self, item):
        self.driver.find_element(By.XPATH, self.txt_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_search_xpath).send_keys(item)
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def click_dress1(self):
        self.driver.find_element(By.XPATH, self.btn_dress1_xpath).click()

    def click_dress2(self):
        self.driver.find_element(By.XPATH, self.btn_dress2_xpath).click()

    def set_dress(self, quantity, size):
        self.driver.find_element(By.XPATH, self.txt_quantity_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_quantity_xpath).send_keys(quantity)
        dress_size = Select(self.driver.find_element(By.XPATH, self.drdn_size_xpath))
        dress_size.select_by_visible_text(size)

    def dress1_colour(self, colour):
        if colour == "Orange":
            self.driver.find_element(By.XPATH, "//ul[@id='color_to_pick_list']//li[2]").click()
        elif colour == "Black":
            self.driver.find_element(By.XPATH, "//ul[@id='color_to_pick_list']//li[1]").click()
        elif colour == "Blue":
            self.driver.find_element(By.XPATH, "//ul[@id='color_to_pick_list']//li[3]").click()
        elif colour == "Yellow":
            self.driver.find_element(By.XPATH, "//ul[@id='color_to_pick_list']//li[4]").click()
        else:
            self.driver.find_element(By.XPATH, "//ul[@id='color_to_pick_list']//li[4]").click()

    def dress_colour(self, colour):
        self.driver.find_element(By.XPATH, "//ul[@id='color_to_pick_list']//a[@name='" + colour + "']").click()

    def click_add_cart(self):
        self.driver.find_element(By.XPATH, self.btn_add_cart_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def view_cart(self):
        self.driver.find_element(By.XPATH, self.btn_view_cart_xpath).click()

    def click_checkout(self):
        self.driver.find_element(By.XPATH, self.btn_checkout_xpath).click()

    def click_ship_checkout(self):
        self.driver.find_element(By.XPATH, self.check_terms_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_ship_checkout_xpath).click()


    def click_pay_by_wire(self):
        self.driver.find_element(By.XPATH, self.btn_pay_by_wire_xpath).click()

    def click_pay_by_check(self):
        self.driver.find_element(By.XPATH, self.btn_pay_by_check_xpath).click()

    def click_confirm_order(self):
        self.driver.find_element(By.XPATH, self.btn_order_confirmation_xpath).click()
