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

    def can_change_city_in_the_header_menu(self):
        city_name_in_header = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER)
        city_name_in_header.click()
        time.sleep(2)
        first_city_name_in_header = self.browser.find_element(*BasePageLocators.FIRST_CITY_NAME_IN_CITY_MENU)
        extract_first_city_name_in_header = first_city_name_in_header.text
        first_city_name_in_header.click()
        time.sleep(2)
        city_name_in_header = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER).text
        assert extract_first_city_name_in_header == city_name_in_header

    def open_desktop_callback_form(self):
        desktop_callback_form = self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM)
        desktop_callback_form.click()

    def fill_in_contacts_in_desktop_callback_form(self, name, phone_number):
        name_field = self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM_NAME_FIELD)
        name_field.send_keys(name)
        phone_field = self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM_PHONE_FIELD)
        phone_field.send_keys(phone_number)

    def accept_privacy_policy_checkbox(self):
        privacy_policy_checkbox = self.browser.find_element(*BasePageLocators.PRIVACY_POLICY_CHECKBOX)
        privacy_policy_checkbox.click()

    def push_contact_sent_button(self):
        contact_sent_button = self.browser.find_element(*BasePageLocators.CONTACT_SENT_BUTTON)
        contact_sent_button.click()

    def should_be_successful_sent_message_window(self):
        successful_sent_message_window_text = self.browser.find_element(*BasePageLocators.SENT_MESSAGE_WINDOW).text
        assert "Спасибо, мы свяжемся с вами в ближайшее время" in successful_sent_message_window_text