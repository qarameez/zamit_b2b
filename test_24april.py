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
time.sleep(5)


driver.find_element(By.XPATH,"//a[@id='reloadPage']").click()
time.sleep(4)
print("View Report in Web Page succesfully")

# Get the title of the webpage
title = driver.title
# Assert the title matches the expected title
expected_title = "Zamit | ZQ Report"
assert title == expected_title, f"Actual title '{title}' does not match expected title '{expected_title}'"
print("Title verification passed!")
time.sleep(4)

driver.quit()
print("quit succesfully")


















