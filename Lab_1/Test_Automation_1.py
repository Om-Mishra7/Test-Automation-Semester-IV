# Assumptions | Project is on python and is a web app

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome("./chromedriver")

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.quit()