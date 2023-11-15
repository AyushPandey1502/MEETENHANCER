from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument(r"--user-data-dir=C:\Users\ayush\AppData\Local\Google\Chrome\User Data")

# Create a WebDriver instance
driver = webdriver.Chrome(options=options)

# Navigate to the Google Meet website
driver.get("https://meet.google.com/")

try:
    # Wait for the "Join Now" button to be visible
    join_now_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".join-now-button"))
    )
    join_now_element.click()

    # Turn on the camera and microphone
    camera_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".camera-button"))
    )
    camera_element.click()

    mic_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".mic-button"))
    )
    mic_element.click()

    # Wait for 10 minutes
    import time
    time.sleep(600)

    # Leave the meeting
    leave_meeting_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".leave-meeting-button"))
    )
    leave_meeting_element.click()

except TimeoutException:
    print("Timed out waiting for an element. Please verify the page structure or increase the timeout duration.")

finally:
    # Close the browser when done
    driver.quit()
