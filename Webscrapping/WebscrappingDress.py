import smtplib
from email.message import EmailMessage

from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from utillities.customLogger import LogGen
import openpyxl


base_url = "http://automationpractice.com/"
logger = LogGen.loggen()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(base_url)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("Dress")
driver.find_element(By.XPATH, "//button[@class='btn btn-default button-search']").click()
dressnames = driver.find_elements(By.XPATH, "//h5[@itemprop='name']")
prices = driver.find_elements(By.XPATH, "//div[@class='right-block']//span[@itemprop='price']")

mydressname = []
myprice = []

for dressname in dressnames:
    mydressname.append(dressname.text)

for price in prices:
    myprice.append(price.text)

finallist = zip(mydressname, myprice)

wb = Workbook()
sh1 = wb.active
sh1.append(['Name', 'Price'])

for x in list(finallist):
    sh1.append(x)

wb.save("AutomationPracticeDressRecords.xlsx")

