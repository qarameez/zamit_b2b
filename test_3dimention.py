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
from selenium.webdriver.common.alert import Alert
import time


# Create a new instance of the Firefox driver

driver = webdriver.Chrome()  # Initialize the WebDriver, assuming it's Chrome
driver.get("https://www.zamit.one/") # Replace 'your_website_url_here' with the actual URL
driver.maximize_window()

    # Test Case 1: Verify successful login with valid credentials
login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
emailphone = driver.find_element(By.XPATH, "//input[@id='emailphone']").send_keys("zamit_user74@yopmail.com")
time.sleep(2)
login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password").click()
time.sleep(2)
insert_pass = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("qwerty")
click_submit_button = driver.find_element(By.ID, "submit-btn").click()
time.sleep(2)

driver.find_element(By.XPATH, "//span[normalize-space()='Student']").click()
time.sleep(2)
print("Student succesfully")

driver.find_element(By.XPATH, "//button[normalize-space()='Get your ZQ Now']").click()
time.sleep(2)
print("Get your ZQ Now succesfully")

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
print("click on Submit succesfully")

driver.find_element(By.LINK_TEXT, "ZQ").click()
time.sleep(2)
print("ZQ succesfully")



driver.find_element(By.XPATH,"//input[@value='Next']").click()
time.sleep(2)
print("Thank you for completing Technological Skills dimension. You have completed 33% of your analysis.")
time.sleep(2)


driver.find_element(By.XPATH,"//a[normalize-space()='Next']").click()
time.sleep(2)
print("Learning Power Click on Next to begin with the next dimension")
time.sleep(5)


driver.find_element(By.XPATH,"//a[normalize-space()='Next']").click()
time.sleep(2)
print("Welcome to your school for the day! succesfully")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,".btn.next-btn").click()
time.sleep(2)
print("The red location pins represent each location succesfully")
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Next']").click()
time.sleep(2)
print("Welcome to your school for the day!  succesfully")
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Lets begin']").click()
time.sleep(2)
print("The red location pins   succesfully")
time.sleep(2)


driver.find_element(By.XPATH,"//a[@type='button']").click()
time.sleep(2)
print("Assembly  succesfully")
time.sleep(2)


driver.quit()
print("quit succesfully")


















