import time
from playwright.sync_api import sync_playwright

def open_browser_and_join(meet_link):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Go to Google Meet link
        page.goto(meet_link)

        # Wait for the page to load
        page.wait_for_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt')

        # Turn off microphone and camera
        page.click('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt')

        # Join the meeting
        page.click('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt')

        # Wait for the meeting to start
        time.sleep(10)

        # Close the browser
        browser.close()

if __name__ == "__main__":
    # Get Google Meet link from the user
    meet_link = input("Enter the Google Meet link: ")

    # Open browser and join the meeting
    open_browser_and_join(meet_link)
