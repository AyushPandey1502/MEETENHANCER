from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome options to disable notifications and set a user-agent
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://meet.google.com/lookup/aplckzgevt?authuser=2&hs=179")

# # Check if the user is already signed in
# if "accounts.google.com" in driver.current_url:
#     # Perform the login (assuming you have credentials)
#     email = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
#     email.send_keys("ayush.afs9@gmail.com")
#     driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
#
#     password = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "password"))
#     )
#     password.send_keys("nBu95r8#Yx")
#     driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
#
#     # Wait for the login to complete
#     WebDriverWait(driver, 10).until(
#         EC.url_contains("https://meet.google.com/")
#     )
#
# input("Enter")

# # Once logged in, proceed with joining the meeting
# wait = WebDriverWait(driver, 10)
# # meet = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button/span')))
# meet = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button/span')
# meet.click()
# join_meet = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/ul/li[2]/span[3]')
# join_meet.click()
# time.sleep(5)
# # You are now on the Google Meet page. You can continue with your actions.
