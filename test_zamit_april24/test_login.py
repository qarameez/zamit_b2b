import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

def test_successful_login():
    driver = webdriver.Chrome()
    driver.get("https://www.zamit.one/")
    driver.maximize_window()

    # Test Case 1: Verify successful login with valid credentials
    login_link = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
    login_link.click()
    emailphone_input = driver.find_element(By.XPATH, "//input[@id='emailphone']")
    emailphone_input.send_keys("zamit_user9@yopmail.com")
    time.sleep(2)
    login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password")
    login_pass_button.click()
    time.sleep(2)
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys("zamit129")
    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()
    time.sleep(5)

    assert "Logged in successfully" in driver.page_source, "Failed to login with valid credentials"
    print("Test case 'Successful Login' passed")

def test_invalid_credentials_login():
    driver = webdriver.Chrome()
    driver.get("https://www.zamit.one/")
    driver.maximize_window()

    # Test Case 2: Verify error message for invalid credentials
    login_link = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
    login_link.click()
    emailphone_input = driver.find_element(By.XPATH, "//input[@id='emailphone']")
    emailphone_input.send_keys("invalid_user@yopmail.com")
    time.sleep(2)
    login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password")
    login_pass_button.click()
    time.sleep(2)
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys("invalid_password")
    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()
    time.sleep(5)

    assert "Invalid username or password" in driver.page_source, "No error message displayed for invalid credentials"
    print("Test case 'Invalid Credentials Login' passed")

def test_forgot_password_functionality():
    driver = webdriver.Chrome()
    driver.get("https://www.zamit.one/")
    driver.maximize_window()

    # Test Case 3: Verify forgot password functionality
    login_link = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
    login_link.click()
    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot Password")
    forgot_password_link.click()
    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    email_input.send_keys("registered_email@example.com")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(5)

    assert "Password reset instructions sent" in driver.page_source, "Password reset instructions not sent"
    print("Test case 'Forgot Password Functionality' passed")

# Non-Functional Test Cases
def test_performance():
    driver = webdriver.Chrome()
    driver.get("https://www.zamit.one/")
    driver.maximize_window()

    # Test Case 4: Measure login process time under normal load
    login_link = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
    login_link.click()
    emailphone_input = driver.find_element(By.XPATH, "//input[@id='emailphone']")
    emailphone_input.send_keys("zamit_user9@yopmail.com")
    time.sleep(2)
    login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password")
    login_pass_button.click()
    time.sleep(2)
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys("zamit129")
    submit_button = driver.find_element(By.ID, "submit-btn")
    submit_button.click()
    start_time = time.time()
    time.sleep(5)
    end_time = time.time()
    print(f"Login process time: {end_time - start_time} seconds")

def test_security():
    driver = webdriver.Chrome()
    driver.get("https://www.zamit.one/")
    driver.maximize_window()

    # Test Case 5: Check for security vulnerabilities during login
    pass  # Add security testing code here

def test_usability():
    driver = webdriver.Chrome()
    driver.get("https://www.zamit.one/")
    driver.maximize_window()

    # Test Case 6: Evaluate the usability of the login page
    login_link = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
    assert login_link.is_displayed(), "Login link not found or not displayed"
    print("Login link found and displayed successfully")

# Execute test cases
test_successful_login()
test_invalid_credentials_login()
test_forgot_password_functionality()
test_performance()
test_security()
test_usability()
