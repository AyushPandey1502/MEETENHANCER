from playwright.sync_api import sync_playwright
import cv2
import time
import tkinter as tk
from tkinter import simpledialog


def detect_person(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use a pre-trained face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return len(faces) > 0


def automate_google_meet(google_meet_url, camera_image_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Open Google Meet
        page.goto(google_meet_url)

        # Wait for the page to load
        page.wait_for_load_state()

        while True:
            # Check if person's picture is detected
            if detect_person(camera_image_path):
                # Turn on camera and microphone
                camera_button = page.locator('aria-label=Turn on camera')
                microphone_button = page.locator('aria-label=Unmute microphone')
                camera_button.click()
                microphone_button.click()

                # Wait for changes to take effect
                page.wait_for_timeout(2000)

                print("Person detected. Keeping camera and microphone on.")
            else:
                # Turn off camera and microphone
                camera_button = page.locator('aria-label=Turn off camera')
                microphone_button = page.locator('aria-label=Mute microphone')
                camera_button.click()
                microphone_button.click()

                # Wait for changes to take effect
                page.wait_for_timeout(2000)

                print("No person detected. Turning off camera and microphone.")

            # Wait before checking again
            time.sleep(5)

        # Close the browser
        browser.close()


def get_google_meet_url():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt for the Google Meet link using a simple dialog box
    google_meet_url = simpledialog.askstring("Google Meet Link", "Enter the Google Meet link:")

    return google_meet_url


if __name__ == "__main__":
    # Get the Google Meet link from the user
    google_meet_url = get_google_meet_url()

    # Replace 'path/to/camera_image.jpg' with the path to the image of the person
    camera_image_path = 'Coding Files/captured_photo.png'

    # Start automation with the provided Google Meet link
    automate_google_meet(google_meet_url, camera_image_path)
