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
# driver = webdriver.Firefox()
# url = "https://www.zamit.one/"
# print("Open the URL in Firefox")
# driver.get(url)
# print(url)
# time.sleep(3)

# def test_login():
#     login = driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
#     if driver.current_url == "Zamit | Login":
#         print("Succesfuuly login page open")
#     else:
#         print("Login page failed")
#
# driver.quit()


# def test_login1():
#
#     login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#
#     if driver.current_url == "Zamit | Login":  # Corrected the comparison operator from '=' to '=='
#         print("Successfully logged into the login page")
#     else:
#         print("Login page not opened successfully")
#
#     driver.quit()  # Moved this outside the if-else block to ensure it's executed after the check


# def test_validlogin():
#     login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#
#     if driver.current_url == "Zamit | Login":  # Corrected the comparison operator from '=' to '=='
#         print("Successfully logged into the login page")
#
#     emailphone =  driver.find_element(By.XPATH,"//input[@id='emailphone']").send_keys("teach6@yopmail.com")
#     time.sleep(2)
#
#     login_pass_button  = driver.find_element(By.LINK_TEXT,"Login with Password").click()
#     time.sleep(2)
#
#     insert_pass =  driver.find_element(By.XPATH,"//input[@id='password']").send_keys("qwe@123")
#
#     click_submit_button = driver.find_element(By.ID,"submit-btn").click()
#     time.sleep(2)
#
#     if driver.current_url == "Zamit | Empowering Students, Teachers &amp; Schools for Future Readiness":  # Corrected the comparison operator from '=' to '=='
#         print("Dashboard logged into the login page")
#     else:
#         print("Dashboard page not opened successfully")
#
#     driver.quit()







# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_validlogin():
#     driver = webdriver.Chrome()  # Initialize the WebDriver, assuming it's Chrome
#     driver.get("https://www.zamit.one/")  # Replace 'your_website_url_here' with the actual URL
#
#     # Test Case 1: Verify successful login with valid credentials
#     login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#     emailphone = driver.find_element(By.XPATH, "//input[@id='emailphone']").send_keys("teach6@yopmail.com")
#     time.sleep(2)
#     login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password").click()
#     time.sleep(2)
#     insert_pass = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("qwe@123")
#     click_submit_button = driver.find_element(By.ID, "submit-btn").click()
#     time.sleep(2)
#     assert driver.current_url == "Zamit | Empowering Students, Teachers & Schools for Future Readiness", "Test Case 1 Failed: Dashboard page not opened successfully"
#     print("Test Case 1 Passed: Successfully logged into the dashboard after login")
#
#     driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_validlogin1():
#     driver = webdriver.Chrome()  # Initialize the WebDriver, assuming it's Chrome
#     driver.get("https://www.zamit.one/")  # Replace 'your_website_url_here' with the actual URL
#
#     # Test Case 1: Verify successful login with valid credentials
#     login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#     emailphone = driver.find_element(By.XPATH, "//input[@id='emailphone']").send_keys("teach6@yopmail.com")
#     time.sleep(2)
#     login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password").click()
#     time.sleep(2)
#     insert_pass = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("qwe@123")
#     click_submit_button = driver.find_element(By.ID, "submit-btn").click()
#     time.sleep(2)
#     assert driver.current_url == "Zamit | Empowering Students, Teachers &amp; Schools for Future Readiness", "Test Case 1 Failed: Dashboard page not opened successfully"
#     print("Test Case 1 Passed: Successfully logged into the dashboard after login")
#
#     driver.quit()
#
# def test_invalid_email_login():
#     driver = webdriver.Chrome()
#     driver.get("https://www.zamit.one/")
#
#     login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#     # Provide invalid email/phone
#     invalid_email = "invalid_email@domain.com"
#     emailphone = driver.find_element(By.XPATH, "//input[@id='emailphone']").send_keys(invalid_email)
#     time.sleep(2)
#     login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password").click()
#     time.sleep(2)
#     # Skip password entry as this test is only for email validation
#     click_submit_button = driver.find_element(By.ID, "submit-btn").click()
#     time.sleep(2)
#     # Assert if still on login page or redirected back
#     assert driver.current_url == "Zamit | Login", f"Test Case 2 Failed: Invalid email '{invalid_email}' didn't trigger login failure"
#     print("Test Case 2 Passed: Login failed with invalid email")
#
#     driver.quit()
#
# def test_invalid_password_login():
#     driver = webdriver.Chrome()
#     driver.get("https://www.zamit.one/")
#
#     login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#     # Provide valid email/phone
#     valid_email = "teach6@yopmail.com"
#     emailphone = driver.find_element(By.XPATH, "//input[@id='emailphone']").send_keys(valid_email)
#     time.sleep(2)
#     login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password").click()
#     time.sleep(2)
#     # Provide invalid password
#     invalid_password = "invalid_password"
#     insert_pass = driver.find_element(By.XPATH, "//input[@id='password']").send_keys(invalid_password)
#     click_submit_button = driver.find_element(By.ID, "submit-btn").click()
#     time.sleep(2)
#     # Assert if still on login page or redirected back
#     assert driver.current_url == "Zamit | Login", "Test Case 3 Failed: Invalid password didn't trigger login failure"
#     print("Test Case 3 Passed: Login failed with invalid password")
#
#     driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_validlogin1():
    driver = webdriver.Chrome()  # Initialize the WebDriver, assuming it's Chrome
    driver.get("https://www.zamit.one/") # Replace 'your_website_url_here' with the actual URL
    driver.maximize_window()

    # Test Case 1: Verify successful login with valid credentials
    login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    emailphone = driver.find_element(By.XPATH, "//input[@id='emailphone']").send_keys("zamit_user9@yopmail.com")
    time.sleep(2)
    login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password").click()
    time.sleep(2)
    insert_pass = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("zamit129")
    click_submit_button = driver.find_element(By.ID, "submit-btn").click()
    time.sleep(5)
    if driver.current_url == "Zamit | Empowering Students, Teachers &amp; Schools for Future Readiness":  # Corrected the comparison operator from '=' to '=='
        print("Successfully logged into the login page")
    else:
        print("Login page not opened successfully")

    # assert driver.current_url == "Zamit | Empowering Students, Teachers &amp; Schools for Future Readiness", "Test Case 1 Failed: Dashboard page not opened successfully"
    # print("Test Case 1 Passed: Successfully logged into the dashboard after login")



    # Find the element to hover over
    element_to_hover_over = driver.find_element(By.XPATH, "//a[@id='dropdownloggedIn']")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover_over).perform()
    element_to_click = driver.find_element(By.XPATH, "//a[normalize-space()='My Dashboard']")
    element_to_click.click()
    time.sleep(5)

# Download file
    download_button = driver.find_element(By.XPATH, "//a[@id='download_report']")
    download_button.click()
    time.sleep(5)

    # Quit the WebDriver
    driver.quit()




