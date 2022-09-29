from bs4 import BeautifulSoup
from selenium import webdriver
# import requests

url = "https://premier.ticketek.com.au/events/JAYCHOU20/venues/SOEG/performances/ESOE2020678JC/tickets"

# Get HTML using requests
# try:
#     response = requests.get(url)
#     with open("response.txt", "w") as f:
#         f.write(response.text)
# except Exception as e:
#     print("Exception in getting response from get request: "+str(e))

# To configure webdriver to use Chrome browser, we have to set the path to chromedriver
driver = webdriver.Chrome("/Users/peterhua/Documents/chromedriver")

# open the URL:
products=[] # list to store name of the product
driver.get(url)
content = driver.page_source

# Parse HTML using BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")
