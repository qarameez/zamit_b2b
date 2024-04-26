
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


s = Service("C:/Users/MASH/Desktop/Selenium/Selenium/chromedriver122-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.mashvirtual.info/ZamitB2B/#/login")
print("B2B URL open Succesfully")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME, "UserName").send_keys("admin@mashvirtual.in")
time.sleep(2)
driver.find_element(By.NAME, "Password").send_keys("admin@123")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
print("login button click")
time.sleep(2)

# CLick on Activities menu bar
driver.find_element(By.XPATH, "/html/body/app-root/app-secure/div/aside/section/ul/li[2]/a/span[1]").click()
time.sleep(2)
print("Activities button click")

# CLick on select Feed Type
driver.find_element(By.XPATH, "//li[2]//ul[1]//li[6]//a[1]").click()
time.sleep(2)
print("News button click")

# CLick on feedTypeID  bar
driver.find_element(By.XPATH, "//select[@name='feedTypeID']").click()
time.sleep(2)
print("Click on News list bar")

# CLick on Click bar
driver.find_element(By.XPATH, "//option[@value='4']").click()

time.sleep(2)
print("Click on Webinars")
time.sleep(3)

driver.find_element(By.NAME, "newsTitle").send_keys(" CHAT GPT VS (Google AI) [BARD by Google AI] Title: SimGPT - AI for Efficient and Accurate Few-Shot Learning")
time.sleep(2)
print("Click on NAME Title")
time.sleep(2)

driver.find_element(By.NAME, "newsDesc").send_keys("Launched in 2022, BARD is a factual language model from Google AI designed for dialogue and conversation. It can access and process information from the real world through Google Search and keep its response consistent with search results, making it a valuable tool for information retrieval and question answering. Description: SimGPT, revealed by Google AI in January 2023, is a factual language model designed for few-shot learning. It requires minimal training data to perform well on a specific task, making it efficient and adaptable for various applications.Description: Introduced in April 2022, Megatron-Turing NLG is a generative language model by NVIDIA trained on a massive dataset of text and code in multiple languages. It can generate different creative text formats in various languages, demonstrating impressive multilingual capabilities. text and code. It's particularly adept at generating different creative text formats, like poems, code, scripts, musical pieces, email, letters, etc., and excels in long-form text generation tasks.")
time.sleep(2)
print("Click on Description Title")
time.sleep(5)

file_input = driver.find_element(By.ID, "newsThumb")
file_input.send_keys("C:/Users/MASH/Desktop/Selenium/images/5.jpg")
time.sleep(5)

file_input = driver.find_element(By.ID, "podcast")
file_input.send_keys("C:/Users/MASH/Desktop/Selenium/Audio/1.mp3")
time.sleep(5)

driver.find_element(By.XPATH, "//input[@placeholder='Episode Length']").send_keys("20")
time.sleep(3)

driver.find_element(By.ID, "videoEmbd").send_keys("https://www.youtube.com/watch?v=WKDMf76fl5I")
time.sleep(3)




# CLick on India Host option
driver.find_element(By.XPATH, "//input[@id='hostName']").send_keys("Google")
time.sleep(2)

# CLick on India cpuntry option
driver.find_element(By.XPATH, "//tbody/tr[6]/td[3]/input[1]").click()
time.sleep(2)

# CLick on Save option
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
time.sleep(2)

driver.close()
time.sleep(2)
print("Driver Close succesfully")