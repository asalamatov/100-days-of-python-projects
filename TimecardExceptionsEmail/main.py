from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "+++++++++++"
PASSWORD = "+++++++++++"

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(options=c)
driver.get("https://workforcenow.adp.com/theme/unified.html#/People/PeopleTabTimeAndAttendanceCategoryTLMWebTimecardExceptions")
# email_field = driver.find_element(By.XPATH, '//*[@id="login-form_username"]')
# email_field.send_keys(EMAIL)
# next_button = driver.find_element(By.XPATH, '//*[@id="verifUseridBtn"]/span/span')
# email_field.send_keys(Keys.ENTER)
# sleep(40)
# password_field = driver.find_element(By.XPATH, '//*[@id="login-form_password"]')
# password_field.click()
# password_field.send_keys(PASSWORD)
# password_field.send_keys(Keys.ENTER)
sleep(100)