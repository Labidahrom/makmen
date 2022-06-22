from .locators import MainPageLocators
from .base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class MainPage(BasePage):
    def click_on_accept_city_in_popup_massage(self):
        button = self.browser.find_element(*MainPageLocators.CITY_POPUP_YES_BUTTON)
        button.click()

    def should_be_current_user_city_in_header(self, current_user_city):
        city_name_in_header = self.browser.find_element(*MainPageLocators.CITY_NAME_IN_HEADER).text
        print(city_name_in_header)
        assert city_name_in_header == current_user_city

    def click_on_city_name_in_header(self):
        button = self.browser.find_element(*MainPageLocators.CITY_NAME_IN_HEADER)
        button.click()

    def click_on_first_city_name_in_city_list(self):
        button = self.browser.find_element(*MainPageLocators.FIRST_CITY_NAME_IN_CITY_MENU)
        button.click()

    def should_be_first_city_from_city_list_in_header(self):
        time.sleep(1)
        city_name_in_header = self.browser.find_element(*MainPageLocators.CITY_NAME_IN_HEADER)
        city_name_in_header_name = city_name_in_header.text
        city_name_in_header.click()
        first_city_in_list = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((*MainPageLocators.FIRST_CITY_NAME_IN_CITY_MENU,))
        )
        first_city_name_in_list = first_city_in_list.text
        assert first_city_name_in_list == city_name_in_header_name

    def click_on_desktop_callback_form(self):
        button = self.browser.find_element(*MainPageLocators.DESKTOP_CALLBACK_FORM)
        button.click()

    def fill_in_name_field_in_desktop_callback_form(self, name):
        self.browser.find_element(*MainPageLocators.DESKTOP_CALLBACK_FORM_NAME_FIELD).send_keys(name)

    def fill_in_phone_number_field_in_desktop_callback_form(self, phone):
        self.browser.find_element(*MainPageLocators.DESKTOP_CALLBACK_FORM_PHONE_FIELD).send_keys(phone)

    def click_on_accept_privacy_policy_checkbox_in_callback_form(self):
        button = self.browser.find_element(*MainPageLocators.CALLBACK_FORM_POLICY_CHECKBOX)
        button.click()

    def click_on_contact_send_button_in_callback_form(self):
        button = self.browser.find_element(*MainPageLocators.CONTACT_SENT_BUTTON)
        button.click()

    def should_be_successful_send_message_window(self):
        time.sleep(1)
        successful_send_message_window_text = self.browser.find_element(*MainPageLocators.SENT_MESSAGE_WINDOW).text
        assert "Спасибо, мы свяжемся с вами в ближайшее время" in successful_send_message_window_text

    def type_in_search_query_in_header(self, product):
        self.browser.find_element(*MainPageLocators.HEADER_SEARCH_FIELD).send_keys(product)

    def click_on_search_button_in_header(self):
        button = self.browser.find_element(*MainPageLocators.HEADER_SEARCH_BUTTON)
        button.click()

    def should_be_found_products_in_search_results(self):
        search_result_number = len(self.browser.find_elements(*MainPageLocators.PRODUCT_CARD))
        print("Results found:", search_result_number)
        assert search_result_number > 0

    def click_on_account_link_in_header(self):
        button = self.browser.find_element(*MainPageLocators.ACCOUNT_LINK)
        button.click()

    def click_on_account_link_in_header_mobile(self):
        button = self.browser.find_element(*MainPageLocators.ACCOUNT_LINK_MOBILE)
        button.click()

    def click_on_register_link_in_account_menu(self):
        button = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        button.click()

    def fill_in_name_field_in_register_form(self, name):
        self.browser.find_element(*MainPageLocators.REGISTER_NAME).send_keys(name)

    def fill_in_surname_field_in_register_form(self, surname):
        self.browser.find_element(*MainPageLocators.REGISTER_SURNAME).send_keys(surname)

    def fill_in_phone_field_in_register_form(self, phone):
        self.browser.find_element(*MainPageLocators.REGISTER_PHONE).send_keys(phone)

    def fill_in_email_field_in_register_form(self, email):
        self.browser.find_element(*MainPageLocators.REGISTER_EMAIL).send_keys(email)

    def fill_in_password_field_in_register_form(self, password):
        self.browser.find_element(*MainPageLocators.REGISTER_PASSWORD).send_keys(password)

    def click_on_accept_privacy_policy_checkbox_in_register_form(self):
        button = self.browser.find_element(*MainPageLocators.REGISTER_FORM_PRIVACY_CHECKBOX)
        button.click()

    def click_on_register_form_send_button(self):
        button = self.browser.find_element(*MainPageLocators.REGISTER_FORM_SEND_BUTTON)
        button.click()


    def should_open_user_account_page(self):
        time.sleep(1)
        page_header = self.browser.find_element(*MainPageLocators.USER_PAGE_HEADER).text
        print(page_header)
        assert 'Моя учетная запись' in page_header

    def click_on_sigh_in_link_in_account_menu(self):
        button = self.browser.find_element(*MainPageLocators.SIGN_IN_LINK)
        button.click()

    def fill_in_email_field_in_sigh_in_form(self, email):
        self.browser.find_element(*MainPageLocators.LOGIN_EMAIL).send_keys(email)

    def fill_in_password_field_in_sigh_in_form(self, password):
        self.browser.find_element(*MainPageLocators.LOGIN_PASSWORD).send_keys(password)

    def click_on_sign_in_form_send_button(self):
        button = self.browser.find_element(*MainPageLocators.SIGH_IN_FORM_SEND_BUTTON)
        button.click()

    def scroll_down_screen(self):
        self.browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)

    def click_on_scroll_up_icon(self):
        button = self.browser.find_element(*MainPageLocators.SCREEN_UP_ICON)
        button.click()
        time.sleep(1)

    def shoud_be_site_header_visible_on_screen(self):
        logo_text = self.browser.find_element(*MainPageLocators.UNDER_LOGO_TEXT).text
        assert 'Оборудование для HoReCa' in logo_text

    def click_on_search_drop_down_category_meny(self):
        button = self.browser.find_element(*MainPageLocators.SEARCH_DROP_DOWN_MENU)
        button.click()

    def choose_second_item_in_search_drop_down_category_meny(self):
        item = self.browser.find_element(*MainPageLocators.SECOND_ITEM_IN_SEARCH_DROP_DOWN_MENU)
        item.click()

    def should_be_no_found_products_in_search_results(self):
        search_result_number = len(self.browser.find_elements(*MainPageLocators.PRODUCT_CARD))
        print("Results found:", search_result_number)
        assert search_result_number == 0

    def clear_product_search_field(self):
        self.browser.find_element(*MainPageLocators.HEADER_SEARCH_FIELD).clear()




















