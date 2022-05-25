from .locators import BasePageLocators
import time

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def accept_city_in_popup_massage(self):
        accept_city_button = self.browser.find_element(*BasePageLocators.CITY_POPUP_YES_BUTTON)
        accept_city_button.click()

    def should_be_right_city_in_header(self, current_user_city):
        city_name_in_header = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER).text
        print(city_name_in_header)
        assert city_name_in_header == current_user_city