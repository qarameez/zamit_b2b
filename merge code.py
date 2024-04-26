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
driver = webdriver.Firefox()
url = "https://www.zamit.one/"
print("Open the URL in Firefox")
driver.get(url)
print(url)
time.sleep(2)

#Test Case 1: Verify successful login with valid credentials
login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
emailphone = driver.find_element(By.XPATH, "//input[@id='emailphone']").send_keys("zamit_user75@yopmail.com")
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
print("Question attempts succesfully")


def find_and_check_inputbox():
    try:
        driver.execute_script("""
        let elms = document.querySelectorAll("input[type='radio']");
        elms[0].checked = true;
        """)
    except: print('i was told to skip!')

    try:
        driver.execute_script("""
        document.querySelector('video').play();
        """)
        time.sleep(5)
    except:
        print('Video not found or could not be played')

# click_completing1 = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
for qlen in range(16):
    find_and_check_inputbox()
    print("Question attempts succesfully")
    time.sleep(2)
    Next_Button = driver.find_element(By.XPATH,"//input[@value='Next']").click()
    print("Question attempts succesfully")
    time.sleep(2)


find_and_check_inputbox()
driver.find_element(By.XPATH,"//input[@value='Save & Exit']").click()
time.sleep(2)
print("Save & Exit succesfully")
time.sleep(5)
print("Close succesfully")

driver.find_element(By.XPATH,"//p[contains(@class,'lead text-muted')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Close']").click()
print("Popup Close succesfully")
time.sleep(3)

# driver = webdriver.Firefox()
url = "https://www.zamit.one/"
print("Open the URL in Firefox")
driver.get(url)
print(url)
time.sleep(2)


driver.find_element(By.XPATH, "//button[normalize-space()='Get your ZQ Now']").click()
time.sleep(2)
print("Get your ZQ Now succesfully")

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
print("Clcik on Submit succesfully")

# Click on "Download" link
driver.find_element(By.XPATH, "//a[normalize-space()='Report']").click()
time.sleep(5)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Download']").click()
time.sleep(20)

# Quit the browser session
driver.quit()
print("quit successfully")




















