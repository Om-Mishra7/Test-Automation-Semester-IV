# Assumptions | Project is on python and is a web app

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.python.org/")
print(driver.title)

search_bar = driver.find_element("name","q")

search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(10)

driver.quit()


