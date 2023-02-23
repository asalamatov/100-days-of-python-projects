import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://portal.na.edu/ICS/Students/")
account = driver.find_element(By.XPATH, '//*[@id="userName"]')
account.send_keys("asalamatov")
account.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("SALazaCHEM2004@")
password.send_keys(Keys.ENTER)
time.sleep(3)