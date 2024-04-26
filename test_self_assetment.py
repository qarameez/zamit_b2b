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

# Download file
    download_button = driver.find_element(By.XPATH, "//button[normalize-space()='Get your ZQ Now']")
    download_button.click()
    time.sleep(3)

    click_submitbutton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    click_submitbutton.click()
    time.sleep(3)

    click_selfbutton = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2)")
    click_selfbutton.click()
    time.sleep(3)

    # click_FirstQuestion = driver.find_element(By.XPATH,"//span[normalize-space()='Agree']")
    # click_FirstQuestion.click()
    # time.sleep(3)
    # click_Firstnextpage = driver.find_element(By.XPATH, "//input[@value='Next']")
    # click_Firstnextpage.click()
    # time.sleep(4)
    # print("FirstQuestion")

    # click_2Question = driver.find_element(By.XPATH,"//span[normalize-space()='Agree']")
    # click_2Question.click()
    # time.sleep(3)
    # click_2nextpage = driver.find_element(By.XPATH, "//input[@value='Next']")
    # click_2nextpage.click()
    # time.sleep(4)
    # print("2Question")
    #
    # click_3Question = driver.find_element(By.XPATH, "//span[normalize-space()='Agree']")
    # click_3Question.click()
    # time.sleep(3)
    # click_3nextpage = driver.find_element(By.XPATH, "//input[@value='Next']")
    # click_3nextpage.click()
    # time.sleep(4)
    # print("3Question")

    # click_4Question = driver.find_element(By.XPATH, "//span[normalize-space()='Agree']")
    # click_4Question.click()
    # time.sleep(3)
    # click_4nextpage = driver.find_element(By.XPATH, "//input[@value='Next']")
    # click_4nextpage.click()
    # time.sleep(4)
    # print("4Question")
    #
    # click_4Question = driver.find_element(By.XPATH, "//span[normalize-space()='Agree']")
    # click_4Question.click()
    # time.sleep(3)
    # click_4nextpage = driver.find_element(By.XPATH, "//input[@value='Next']")
    # click_4nextpage.click()
    # time.sleep(4)
    # print("4Question")
    #
    # click_completing = driver.find_element(By.XPATH, "// input[ @ value = 'Next']")
    # click_completing.click()
    # print("Thank you for completing Social Perception Self dimension.Click on Next to continue with your analysis.")

    click_completing1 = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
    click_completing1[0].click()
    print("You have successfully completed your self-appraisal")

    # Assert if still on login page or redirected back
    if driver.current_url == "Exam completed - zamit ZQ":
        print("Dashboard logged into the login page")
    else:
        print("Dashboard page not opened successfully")




    # Quit the WebDriver
    driver.quit()

