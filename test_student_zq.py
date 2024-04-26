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


# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
url = "https://www.zamit.one/"
print("Open the URL in Firefox")
driver.get(url)
print(url)
time.sleep(5)

driver.find_element(By.XPATH,"//span[normalize-space()='Teacher']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//span[normalize-space()='Student']").click()
time.sleep(3)


# Find the dropdown element by its ID, XPath, CSS Selector, etc.
dropdown_element = driver.find_element(By.XPATH,"//select[@id='class']")
# Create a Select object from the dropdown element
dropdown = Select(dropdown_element)
# Select an item by visible text
dropdown.select_by_value("2")
print("Current URL:", driver.current_url)

driver.find_element(By.XPATH,"//button[normalize-space()='Get your ZQ Now']").click()
time.sleep(2)

def find_and_check_inputbox():
    try:
        driver.execute_script("""
        let elms = document.querySelectorAll("input[type='radio']");
        elms[0].checked = true;
        """)
    except: print('i was told to skip!')
# click_completing1 = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
for qlen in range(100):
    find_and_check_inputbox()
    print("Question attempts succesfully")
    time.sleep(2)
    Next_Button = driver.find_element(By.XPATH,"//input[@value='Next']").click()
    print("Question attempts succesfully")
    time.sleep(2)

driver.quit()
print("quit succesfully")

