from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import requests
import time

url = "https://premier.ticketek.com.au/events/JAYCHOU20/venues/SOEG/performances/ESOE2020678JC/tickets"

# Get HTML using requests
# try:
#     response = requests.get(url)
#     with open("response.txt", "w") as f:
#         f.write(response.text)
# except Exception as e:
#     print("Exception in getting response from get request: "+str(e))

# To configure webdriver to use Chrome browser, we have to set the path to chromedriver
options = webdriver.ChromeOptions()
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
# options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options, executable_path="/Users/peterhua/Documents/chromedriver")
# open the URL:
products=[] # list to store name of the product
driver.get(url)
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
# driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
# time.sleep(3)
content = driver.page_source

# Parse HTML using BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")
