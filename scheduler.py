# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Event Scheduler page 
driver.get("Event Scheduler page link") 

# Event title 
title = driver.find_element(By.XPATH, "title element(locator)")
title.send_keys("Title Name")

#Event date
date = driver.find_element(By.XPATH, "date(locator)")
date.send_keys("Date")

# Event participants 
participants = driver.find_element(By.XPATH, "participants email list")
participants.send_keys("participants email list")

#Submit 
submit = driver.find_element(By.XPATH, "submit(locator)")
submit.click()

#Verity that the event appears 
event_list = driver.find_element(By.XPATH, "event_list(locator)")
assert event_list


time.sleep(3)