# Sending Keys & CSS Selector
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Edge()

driver.get(r"https://vtop.vit.ac.in/vtop/open/page")
student_button = driver.find_element('id', 'stdForm')
student_button.click()

driver.implicitly_wait(30)

username = driver.find_element('id', 'username')
username.send_keys("TOPPERAYUSH152")
password = driver.find_element('id', 'password')
password.send_keys('imAyPa@', Keys.NUMPAD1, Keys.NUMPAD2, '3')

time.sleep(10)

# submit = driver.find_element('id', 'submitBtn')
submit = driver.find_element('xpath', '//*[@id="submitBtn"]')
# submit = driver.find_element(By.CSS_SELECTOR, 'button[onclick="javascript:callBuiltValidation();"]')
submit.click()

time.sleep(10)