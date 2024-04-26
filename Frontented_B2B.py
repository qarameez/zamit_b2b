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

s=Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://sandbox.zamit.one/")
print("B2B URL open Succesfully")
driver.maximize_window()
time.sleep(5)

#Click on Resource Voult
driver.find_element(By.XPATH,"//a[@class='nav-link'][normalize-space()='Resource Vault']").click()
time.sleep(3)
print("Resource Voult button click")

#Click on podcast Voult
driver.find_element(By.XPATH,"//img[@alt='Audios']").click()
time.sleep(3)
print("Click on podcast Voult")


#Click on video filter
driver.find_element(By.XPATH,"//input[@id='date-Today']").click()
time.sleep(4)

#Click on video filter
driver.find_element(By.XPATH,"//div[@class='overlay-box']").click()
time.sleep(4)

print("Resource Voult button click")



driver.close()
time.sleep(5)
print("Driver Close succesfully")
