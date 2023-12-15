import booking.constants as const
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Booking(webdriver.Edge):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()  # Crete an instance of webdriver.Edge
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        input()
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency='INR'):
        currency_element = self.find_element(By.CLASS_NAME, 'e4adce92df')
        currency_element.click()
        # select_currency = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*=selected_currency={currency}')
        # if select_currency:
        #     select_currency.click()
        # else:
        #     print(f"Element with link text '{currency}' not found.")

        select_currency = self.find_element(By.CLASS_NAME, 'cf67405157')
        select_currency.click()

    def popUp(self):
        try:
            popUp = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            popUp.click()
            print("Pop Up closed")
        except:
            print("Pop Up not found")

    def select_place_to_go(self, place_to_go):
        search_field = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ss"]'))
        )
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(2)
        first_result = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[tabindex="-1"]'))
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.CLASS_NAME, 'd777d2b248')
        selection_element.click()


        while True:
            decrease_adults_element = self.find_element(By.CLASS_NAME, 'eedba9e88a')
            decrease_adults_element.click()
            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_count = adults_value_element.get_attribute('value')  # Should give back the adults count

            if int(adults_count) == 1:
                break
