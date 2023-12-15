import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Edge()
driver.get(r"https://vtop.vit.ac.in/vtop/open/page")
my_element = driver.find_element('id', 'stdForm')
driver.implicitly_wait(30) #time.sleep(30)
my_element.click()

# progress_element = driver.find_element('class', 'progress_label')
# print(f"{progress_element.text == 'Completed'}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), # Element filtration
        'Complete!'# The expected text
    )
)

