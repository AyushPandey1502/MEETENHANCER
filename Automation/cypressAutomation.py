from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


# Function to control camera and microphone
def control_google_meet(video_on=True, audio_on=True):
    # Set the path to your ChromeDriver executable
    chromedriver_path = "path/to/chromedriver"

    # Create a ChromeOptions object to customize the browser
    chrome_options = webdriver.ChromeOptions()

    # Add arguments to disable the camera and microphone (you can customize these based on your needs)
    if not video_on:
        chrome_options.add_argument("--use-fake-ui-for-media-stream=1")
    if not audio_on:
        chrome_options.add_argument("--use-fake-device-for-media-stream=1")

    # Create a Chrome driver with the specified options
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    # Open Google Meet
    driver.get("https://meet.google.com/")

    # Wait for the page to load (adjust the time based on your network speed)
    time.sleep(5)

    # Find and click the camera and microphone buttons
    camera_button = driver.find_element(By.XPATH, "//div[@data-is-muted='false'][@data-tooltip='Turn off camera']")
    microphone_button = driver.find_element(By.XPATH,
                                            "//div[@data-is-muted='false'][@data-tooltip='Turn off microphone']")

    camera_button.click()
    microphone_button.click()

    # Allow some time for changes to take effect
    time.sleep(2)

    # Close the browser
    driver.quit()


# Function to create a dialog box for entering Google Meet link
def get_google_meet_link():
    root = tk.Tk()
    root.withdraw()

    link = tk.simpledialog.askstring("Google Meet Link", "Enter the Google Meet link:")

    return link


# Main script
if __name__ == "__main__":
    # Get Google Meet link from the user
    meet_link = get_google_meet_link()

    # Control Google Meet camera and microphone
    control_google_meet(video_on=True, audio_on=True)
