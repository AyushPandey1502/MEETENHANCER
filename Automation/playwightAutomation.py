from playwright.sync_api import sync_playwright
import tkinter as tk
from tkinter import simpledialog
from threading import Thread

def control_google_meet(video_on=True, audio_on=True):
    with sync_playwright() as p:
        # Start a new browser context
        browser = p.chromium.launch()

        # Create a new page
        page = browser.new_page()

        # Open Google Meet
        page.goto("https://meet.google.com/")

        # Wait for the page to load (adjust the time based on your network speed)
        page.wait_for_timeout(5000)

        # Find and click the camera and microphone buttons
        camera_button = page.locator('[data-is-muted="false"][data-tooltip="Turn off camera"]')
        microphone_button = page.locator('[data-is-muted="false"][data-tooltip="Turn off microphone"]')

        camera_button.click()
        microphone_button.click()

        # Allow some time for changes to take effect
        page.wait_for_timeout(2000)

        # Close the browser
        browser.close()

def get_google_meet_link():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    link = simpledialog.askstring("Google Meet Link", "Enter the Google Meet link:")
    root.destroy()  # Destroy the root window after getting the input
    return link

if __name__ == "__main__":
    # Run Tkinter in a separate thread to avoid the "Too early to create dialog window" error
    thread = Thread(target=get_google_meet_link)
    thread.start()
    thread.join()

    # Control Google Meet camera and microphone
    control_google_meet(video_on=True, audio_on=True)
