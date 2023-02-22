from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# assert "Python" in driver.title
x_path = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(x_path.text)