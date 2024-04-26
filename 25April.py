import time
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
driver.maximize_window()

# Open the URL
url = "https://www.zamit.one/"
print("Open the URL in Firefox")
driver.get(url)
print(url)


# Click on Login button
login_button = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
login_button.click()

# Enter email/phone
emailphone_input = driver.find_element(By.XPATH, "//input[@id='emailphone']")
emailphone_input.send_keys("zamit_user73@yopmail.com")

# Click on "Login with Password" button
login_pass_button = driver.find_element(By.LINK_TEXT, "Login with Password")
login_pass_button.click()

# Enter password
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys("qwerty")

# Click on submit button
submit_button = driver.find_element(By.ID, "submit-btn")
submit_button.click()
time.sleep(2)


driver.find_element(By.XPATH, "//button[normalize-space()='Get your ZQ Now']").click()
time.sleep(2)
print("Get your ZQ Now succesfully")

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
print("Clcik on Submit succesfully")

# Click on "Download" link
driver.find_element(By.XPATH, "//a[normalize-space()='Report']").click()
time.sleep(15)
# Scroll down the page by 500 pixels
driver.execute_script("window.scrollBy(0, 1000);")

# Scroll up the page by 500 pixels
driver.execute_script("window.scrollBy(0, -1000);")


# Alternatively, you can scroll to a specific element by its XPath
# element = driver.find_element_by_xpath("xpath_of_element")
# driver.execute_script("arguments[0].scrollIntoView();", element)

# Wait for some time to see the effect
driver.back()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Download']").click()
time.sleep(20)

# Quit the browser session
driver.quit()
print("quit successfully")


