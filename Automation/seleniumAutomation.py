from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk, Label, Entry, Button

# Define variables in the global scope
mail_address = ""
password = ""
meet_link = ""

def login_google_account(mail_address, password):
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    driver.find_element(By.ID, "identifierId").send_keys(mail_address)
    driver.find_element(By.ID, "identifierNext").click()

    # Wait for the password input field to be visible
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    password_input.send_keys(password)

    driver.find_element(By.ID, "passwordNext").click()

    # Wait for login to complete
    WebDriverWait(driver, 20).until(EC.title_contains("Google"))

def turn_off_mic_cam():
    # Turn off Microphone
    mic_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div'))
    )
    mic_button.click()

    # Turn off Camera
    cam_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div'))
    )
    cam_button.click()

def join_meet():
    # Join meet
    join_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt'))
    )
    join_button.click()

def get_user_input():
    # Create the main application window
    root = Tk()
    root.title("User Input")

    # Create and place the labels and entry widgets for email, password, and meet link
    email_label = Label(root, text="Enter your Gmail address:")
    email_entry = Entry(root)

    password_label = Label(root, text="Enter your password:")
    password_entry = Entry(root, show='*')

    meet_link_label = Label(root, text="Enter the Google Meet link:")
    meet_link_entry = Entry(root)

    # Place the widgets in the window
    email_label.pack()
    email_entry.pack()

    password_label.pack()
    password_entry.pack()

    meet_link_label.pack()
    meet_link_entry.pack()

    # Function to be called when the OK button is clicked
    def on_ok_click():
        # Retrieve the values from the entry widgets
        global mail_address, password, meet_link
        mail_address = email_entry.get()
        password = password_entry.get()
        meet_link = meet_link_entry.get()

        # Close the main window
        root.destroy()

        # Use the values as needed
        print("Email:", mail_address)
        print("Password:", password)
        print("Meet Link:", meet_link)

    # Create and place the OK button
    ok_button = Button(root, text="OK", command=on_ok_click)
    ok_button.pack()

    # Run the Tkinter main loop
    root.mainloop()

# Call the function to get user input
get_user_input()

# Create a Chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)

# Login to Google account
login_google_account(mail_address, password)

# Go to the specified Google Meet link
driver.get(meet_link)

# Turn off microphone and camera
turn_off_mic_cam()

# Join the meeting
join_meet()

# Note: Don't forget to close the webdriver instance after finishing the script
driver.quit()
