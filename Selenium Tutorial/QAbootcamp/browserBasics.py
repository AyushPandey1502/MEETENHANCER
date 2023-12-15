import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_service=Service(r'C:/SeleniumDrivers/msedgedriver.exe')
driver = webdriver.Edge(service=edge_service)

driver.get("https://demoqa.com/")
print(driver.title)
print(driver.current_url)
driver.refresh()
driver.minimize_window()
driver.maximize_window()
# time.sleep(3)
driver.get("https://demoqa.com/elements")
driver.back()
time.sleep(5)
print(driver.current_url)
driver.forward()
time.sleep(5)
print(driver.current_url)

driver.close()
