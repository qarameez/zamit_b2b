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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)
class Test_b2blogin:
    # def __init__(self):
    #     self.driver = None
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        s = Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
        print("B2B URL open Succesfully")
        driver.maximize_window()
        time.sleep(5)

        if "ZAMITB2B" not in driver.title:
            print("Title mismatch")
        else:
            print("Title verified")

        driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_login(self):
        s = Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
        print("B2B URL open Succesfully")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.NAME, "UserName").send_keys("admin@mashvirtual.in")
        time.sleep(3)
        driver.find_element(By.NAME, "Password").send_keys("admin@123")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
        print("login button click")
        time.sleep(5)
        if "Welcome to ZAMIT Web System" in driver.find_element(By.XPATH,"//h1[normalize-space()='Welcome to ZAMIT Web System']").text:
            assert True
            print("Title User found")
        else:
            assert False
        driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_podcast(self):
        s = Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
        print("B2B URL open Succesfully")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.NAME, "UserName").send_keys("admin@mashvirtual.in")
        time.sleep(3)
        driver.find_element(By.NAME, "Password").send_keys("admin@103")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
        print("login button click")
        time.sleep(5)
        if "Username or Password does not match" in driver.find_element(By.XPATH,"//div[@id='message']").text:
            assert True
            print("Title User found")
        else:
            assert False
        driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_access_b2b_dashboard(self, attachmentType=None):
        s = Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
        print("B2B URL open Succesfully")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.NAME, "UserName").send_keys("admin@mashvirtual.in")
        time.sleep(3)
        driver.find_element(By.NAME, "Password").send_keys("admin@10g3")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
        print("login button click")
        time.sleep(5)
        if "Username or Password does noot match" in driver.find_element(By.XPATH,"//div[@id='message']").text:
            assert True
            print("Title User found")
        else:
            # allure.attach(self.driver.get_screenshot_as_png(),name="screenshot test_access_b2b_dashboard",attachment_type=attachmentType.PNG)
            assert False
        driver.quit()


def test_creationpodcaste():
    s = Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
    print("B2B URL open Succesfully")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.NAME, "UserName").send_keys("admin@mashvirtual.in")
    time.sleep(3)
    driver.find_element(By.NAME, "Password").send_keys("admin@123")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)
    print("login button click")
    time.sleep(5)

    # CLick on Activities menu bar
    driver.find_element(By.XPATH, "/html/body/app-root/app-secure/div/aside/section/ul/li[2]/a/span[1]").click()
    time.sleep(3)
    print("Activities button click")

    # CLick on select Feed Type
    driver.find_element(By.XPATH, "//li[2]//ul[1]//li[6]//a[1]").click()
    time.sleep(5)
    print("News button click")

    # CLick on feedTypeID  bar
    driver.find_element(By.XPATH, "//select[@name='feedTypeID']").click()
    time.sleep(3)
    print("Click on News list bar")

    # CLick on Click bar
    driver.find_element(By.XPATH, "//option[@value='4']").click()

    time.sleep(3)
    print("Click on Webinars")
    time.sleep(3)

    driver.find_element(By.NAME, "newsTitle").send_keys("Title: International Day of forests  ?")
    time.sleep(3)
    print("Click on NAME Title")
    time.sleep(3)

    driver.find_element(By.NAME, "newsDesc").send_keys(
        "Description: A global observance that forests cover about one third of the world's land mass Dive into the world of alternative health and wellness practices. Each episode explores a different popular trend, separating fact from fiction with the help of medical professionals and experts.")
    time.sleep(3)
    print("Click on Description Title")
    time.sleep(3)

    # CLick on India Host option
    driver.find_element(By.XPATH, "//input[@id='hostName']").send_keys("Google")
    time.sleep(3)

    # CLick on India cpuntry option
    driver.find_element(By.XPATH, "//tbody/tr[6]/td[3]/input[1]").click()
    time.sleep(5)

    # CLick on Save option
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(5)

    driver.close()
    time.sleep(5)
    print("Driver Close succesfully")

@allure.severity(allure.severity_level.NORMAL)
def test_podcasteverify():
    s = Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    driver.get("https://sandbox.zamit.one/")
    print("B2B URL open Succesfully")
    driver.maximize_window()
    time.sleep(5)

    # Click on Resource Voult
    driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Resource Vault']").click()
    time.sleep(3)
    print("Resource Voult button click")

    # Click on podcast Voult
    driver.find_element(By.XPATH, "//img[@alt='Audios']").click()
    time.sleep(3)
    print("Click on podcast Voult")

    # Click on video filter
    driver.find_element(By.XPATH, "//input[@id='date-Today']").click()
    time.sleep(4)

    # Click on video filter
    driver.find_element(By.XPATH, "//div[@class='overlay-box']").click()
    time.sleep(4)

    print("Resource Voult button click")

    driver.close()
    time.sleep(5)
    print("Driver Close succesfully")










