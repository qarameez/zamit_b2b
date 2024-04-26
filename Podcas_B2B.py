from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()


# Functional Test Cases
def test_login_functionality():
    driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
    time.sleep(5)
    assert "ZamitB2B" in driver.title
    print("B2B URL open Successfully")

    driver.find_element(By.NAME, "UserName").send_keys("admin@mashvirtual.in")
    driver.find_element(By.NAME, "Password").send_keys("admin@123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)
    print("Login button clicked")


def test_navigation_to_activities_page():
    driver.find_element(By.XPATH, "/html/body/app-root/app-secure/div/aside/section/ul/li[2]/a/span[1]").click()
    time.sleep(3)
    print("Activities button clicked")


def test_selecting_news_feed_type():
    driver.find_element(By.XPATH, "//li[2]//ul[1]//li[6]//a[1]").click()
    time.sleep(5)
    print("News button clicked")


def test_entering_news_title():
    driver.find_element(By.NAME, "newsTitle").send_keys("The Remote Work, and the Gig Economy")
    time.sleep(3)
    print("Entered news title")


def test_entering_news_description():
    driver.find_element(By.NAME, "newsDesc").send_keys(
        "This webinar, hosted by the World Economic Forum, explores the changing landscape of work and how automation, remote work, and the gig economy are transforming the way we work.")
    time.sleep(3)
    print("Entered news description")


# Non-Functional Test Cases
def test_page_load_time():
    start_time = time.time()
    driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
    end_time = time.time()
    page_load_time = end_time - start_time
    assert page_load_time < 10  # Assuming page load time should be less than 10 seconds
    print(f"Page loaded in {page_load_time} seconds")


def test_response_time():
    driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
    start_time = time.time()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    end_time = time.time()
    response_time = end_time - start_time
    assert response_time < 5  # Assuming response time should be less than 5 seconds
    print(f"Response time after login click: {response_time} seconds")


# Execute Test Cases
test_login_functionality()
test_navigation_to_activities_page()
test_selecting_news_feed_type()
test_entering_news_title()
test_entering_news_description()
test_page_load_time()
test_response_time()

# Close WebDriver
driver.quit()
print("Tests completed successfully")
