import allure_pytest
import allure
import xlutils
import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#setup

s=Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
print("B2B URL open Succesfully")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME,"UserName").send_keys("admin@mashvirtual.in")
time.sleep(3)
driver.find_element(By.NAME,"Password").send_keys("admin@123")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)
print("login button click")
time.sleep(5)

#CLick on Activities menu bar
driver.find_element(By.XPATH,"/html/body/app-root/app-secure/div/aside/section/ul/li[2]/a/span[1]").click()
time.sleep(3)
print("Activities button click")

#CLick on select Feed Type
driver.find_element(By.XPATH,"//li[2]//ul[1]//li[6]//a[1]").click()
time.sleep(5)
print("News button click")

# CLick on feedTypeID  bar
driver.find_element(By.XPATH,"//select[@name='feedTypeID']").click()
time.sleep(3)
print("Click on News list bar")

# CLick on Click bar
driver.find_element(By.XPATH,"//option[@value='4']").click()

time.sleep(3)
print("Click on Webinars")
time.sleep(3)

driver.find_element(By.NAME,"newsTitle").send_keys("The Remote Work, and the Gig Economy")
time.sleep(3)
print("Click on NAME Title")
time.sleep(3)

driver.find_element(By.NAME,"newsDesc").send_keys("This webinar, hosted by the World Economic Forum, explores the changing landscape of work and how automation, remote work, and the gig economy are transforming the way we work.")
time.sleep(3)
print("Click on Description Title")
time.sleep(3)

# CLick on India Host option
driver.find_element(By.XPATH,"//input[@id='hostName']").send_keys("Google")
time.sleep(3)

# CLick on India cpuntry option
driver.find_element(By.XPATH,"//tbody/tr[6]/td[3]/input[1]").click()
time.sleep(5)


# CLick on Save option
driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(5)

driver.close()
time.sleep(5)
print("Driver Close succesfully")

