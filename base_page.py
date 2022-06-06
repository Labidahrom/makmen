from .locators import BasePageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

class BasePage():
    def __init__(self, browser, timeout = 10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)
        # self.browser.implicitly_wait(10)

    def find_element(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def generate_email_for_registration(self):
        return str(random.randint(0, 1000)) + str(random.randint(0, 1000)) + "@yandex.ru"

    # def accept_city_in_popup_massage(self):
    #     accept_city_button = self.browser.find_element(*BasePageLocators.CITY_POPUP_YES_BUTTON)
    #     accept_city_button.click()



    # def can_change_city_in_the_header_menu(self):
    #     city_name_in_header = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER)
    #     city_name_in_header.click()
    #     time.sleep(2)
    #     first_city_name_in_header = self.browser.find_element(*BasePageLocators.FIRST_CITY_NAME_IN_CITY_MENU)
    #     extract_first_city_name_in_header = first_city_name_in_header.text
    #     first_city_name_in_header.click()
    #     time.sleep(2)
    #     city_name_in_header = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER).text
    #     assert extract_first_city_name_in_header == city_name_in_header

    # def open_desktop_callback_form(self):
    #     desktop_callback_form = self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM)
    #     desktop_callback_form.click()

    # def fill_in_contacts_in_desktop_callback_form(self, name, phone_number):
    #     name_field = self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM_NAME_FIELD)
    #     name_field.send_keys(name)
    #     phone_field = self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM_PHONE_FIELD)
    #     phone_field.send_keys(phone_number)

    # def accept_privacy_policy_checkbox(self):
    #     privacy_policy_checkbox = self.browser.find_element(*BasePageLocators.PRIVACY_POLICY_CHECKBOX)
    #     privacy_policy_checkbox.click()

    # def push_contact_send_button(self):
    #     contact_send_button = self.browser.find_element(*BasePageLocators.CONTACT_SENT_BUTTON)
    #     contact_send_button.click()

    # def should_be_successful_send_message_window(self):
    #     successful_send_message_window_text = self.browser.find_element(*BasePageLocators.SENT_MESSAGE_WINDOW).text
    #     assert "Спасибо, мы свяжемся с вами в ближайшее время" in successful_send_message_window_text

    # def search_for_product(self, product):
    #     header_search_field = self.browser.find_element(*BasePageLocators.HEADER_SEARCH_FIELD)
    #     header_search_field.send_keys(product)
    #     header_search_button = self.browser.find_element(*BasePageLocators.HEADER_SEARCH_BUTTON)
    #     header_search_button.click()

    # def should_be_found_products(self):
    #     search_result_number = len(self.browser.find_elements(*BasePageLocators.PRODUCT_CARD))
    #     print(search_result_number)
    #     assert search_result_number > 0

    # def fill_in_registration_form(self, name, surname, phone, email, password):
    #     account_link = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
    #     account_link.click()
    #     register_link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
    #     register_link.click()
    #     register_name = self.browser.find_element(*BasePageLocators.REGISTER_NAME)
    #     register_name.send_keys(name)
    #     register_surname = self.browser.find_element(*BasePageLocators.REGISTER_SURNAME)
    #     register_surname.send_keys(surname)
    #     register_phone = self.browser.find_element(*BasePageLocators.REGISTER_PHONE)
    #     register_phone.send_keys(phone)
    #     register_email = self.browser.find_element(*BasePageLocators.REGISTER_EMAIL)
    #     register_email.send_keys(email)
    #     register_password = self.browser.find_element(*BasePageLocators.REGISTER_PASSWORD)
    #     register_password.send_keys(password)
    #     register_form_checkbox = self.browser.find_element(*BasePageLocators.REGISTER_FORM_CHECKBOX)
    #     register_form_checkbox.click()
    #     register_button = self.browser.find_element(*BasePageLocators.REGISTER_BUTTON)
    #     register_button.click()

    # def should_be_user_account_page(self, user_name):
    #     user_account_header = self.browser.find_element(*BasePageLocators.ACCOUNT_HEADER).text
    #     assert user_name in user_account_header

#new function list
    def click_on_accept_city_in_popup_massage(self):
        button = self.browser.find_element(*BasePageLocators.CITY_POPUP_YES_BUTTON)
        button.click()

    def should_be_current_user_city_in_header(self, current_user_city):
        city_name_in_header = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER).text
        print(city_name_in_header)
        assert city_name_in_header == current_user_city

    def click_on_city_name_in_header(self):
        button = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER)
        button.click()

    def click_on_first_city_name_in_city_list(self):
        button = self.browser.find_element(*BasePageLocators.FIRST_CITY_NAME_IN_CITY_MENU)
        button.click()

    def should_be_first_city_from_city_list_in_header(self):
        time.sleep(1)
        city_name_in_header = self.browser.find_element(*BasePageLocators.CITY_NAME_IN_HEADER)
        city_name_in_header_name = city_name_in_header.text
        city_name_in_header.click()
        first_city_in_list = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@data-id='4115']"))
        )
        first_city_name_in_list = first_city_in_list.text
        assert first_city_name_in_list == city_name_in_header_name

    def click_on_desktop_callback_form(self):
        button = self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM)
        button.click()

    def fill_in_name_field_in_desktop_callback_form(self, name):
        self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM_NAME_FIELD).send_keys(name)

    def fill_in_phone_number_field_in_desktop_callback_form(self, phone):
        self.browser.find_element(*BasePageLocators.DESKTOP_CALLBACK_FORM_PHONE_FIELD).send_keys(phone)

    def click_on_accept_privacy_policy_checkbox_in_callback_form(self):
        button = self.browser.find_element(*BasePageLocators.CALLBACK_FORM_POLICY_CHECKBOX)
        button.click()

    def click_on_contact_send_button_in_callback_form(self):
        button = self.browser.find_element(*BasePageLocators.CONTACT_SENT_BUTTON)
        button.click()

    def should_be_successful_send_message_window(self):
        time.sleep(1)
        successful_send_message_window_text = self.browser.find_element(*BasePageLocators.SENT_MESSAGE_WINDOW).text
        assert "Спасибо, мы свяжемся с вами в ближайшее время" in successful_send_message_window_text

    def type_in_search_query_in_header(self, product):
        self.browser.find_element(*BasePageLocators.HEADER_SEARCH_FIELD).send_keys(product)

    def click_on_search_button_in_header(self):
        button = self.browser.find_element(*BasePageLocators.HEADER_SEARCH_BUTTON)
        button.click()

    def should_be_found_products_in_search_results(self):
        search_result_number = len(self.browser.find_elements(*BasePageLocators.PRODUCT_CARD))
        print("Results found:", search_result_number)
        assert search_result_number > 0

    def click_on_account_link_in_header(self):
        button = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
        button.click()

    def click_on_register_link_in_account_menu(self):
        button = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        button.click()

    def fill_in_name_field_in_register_form(self, name):
        self.browser.find_element(*BasePageLocators.REGISTER_NAME).send_keys(name)

    def fill_in_surname_field_in_register_form(self, surname):
        self.browser.find_element(*BasePageLocators.REGISTER_SURNAME).send_keys(surname)

    def fill_in_phone_field_in_register_form(self, phone):
        self.browser.find_element(*BasePageLocators.REGISTER_PHONE).send_keys(phone)

    def fill_in_email_field_in_register_form(self, email):
        self.browser.find_element(*BasePageLocators.REGISTER_EMAIL).send_keys(email)

    def fill_in_password_field_in_register_form(self, password):
        self.browser.find_element(*BasePageLocators.REGISTER_PASSWORD).send_keys(password)

    def click_on_accept_privacy_policy_checkbox_in_register_form(self):
        button = self.browser.find_element(*BasePageLocators.REGISTER_FORM_PRIVACY_CHECKBOX)
        button.click()

    def click_on_register_form_send_button(self):
        button = self.browser.find_element(*BasePageLocators.REGISTER_FORM_SEND_BUTTON)
        button.click()

    def should_open_user_account_page(self, user_name):
        time.sleep(1)
        account_name = self.browser.find_element(*BasePageLocators.ACCOUNT_HEADER).text
        assert user_name in account_name

    def click_on_sigh_in_link_in_account_menu(self):
        button = self.browser.find_element(*BasePageLocators.SIGN_IN_LINK)
        button.click()

    def fill_in_email_field_in_sigh_in_form(self, email):
        self.browser.find_element(*BasePageLocators.LOGIN_EMAIL).send_keys(email)

    def fill_in_password_field_in_sigh_in_form(self, password):
        self.browser.find_element(*BasePageLocators.LOGIN_PASSWORD).send_keys(password)

    def click_on_sign_in_form_send_button(self):
        button = self.browser.find_element(*BasePageLocators.SIGH_IN_FORM_SEND_BUTTON)
        button.click()

    def scroll_down_screen(self):
        self.browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        self.browser.execute_script("window.scrollIntoView(alignToTop)")


    def click_on_scroll_up_icon(self):
        button = self.browser.find_element(*BasePageLocators.SCREEN_UP_ICON)
        button.click()
        time.sleep(1)

    def shoud_be_site_header_visible_on_screen(self):
        account_link = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
        assert account_link.is_displayed()

    def click_on_search_drop_down_category_meny(self):
        button = self.browser.find_element(*BasePageLocators.SEARCH_DROP_DOWN_MENU)
        button.click()

    def choose_second_item_in_search_drop_down_category_meny(self):
        item = self.browser.find_element(*BasePageLocators.SECOND_ITEM_IN_SEARCH_DROP_DOWN_MENU)
        item.click()

    def should_be_no_found_products_in_search_results(self):
        search_result_number = len(self.browser.find_elements(*BasePageLocators.PRODUCT_CARD))
        print("Results found:", search_result_number)
        assert search_result_number == 0

    def clear_product_search_field(self):
        self.browser.find_element(*BasePageLocators.HEADER_SEARCH_FIELD).clear()




















