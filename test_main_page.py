from .base_page import BasePage
import time
from .locators import BasePageLocators

# def test_should_be_right_location(browser):
#     link = "https://makmen.ru"
#     page = BasePage(browser, link)
#     page.open()
#     page.accept_city_in_popup_massage()
#     page.should_be_right_city_in_header("Санкт-Петербург")
#
# def test_city_can_be_changed_from_header(browser):
#     link = "https://makmen.ru"
#     page = BasePage(browser, link)
#     page.open()
#     page.accept_city_in_popup_massage()
#     page.can_change_city_in_the_header_menu()

# def test_desktop_callback_form(browser):
#     link = "https://makmen.ru"
#     page = BasePage(browser, link)
#     page.open()
#     page.accept_city_in_popup_massage()
#     page.open_desktop_callback_form()
#     time.sleep(2)
#     page.fill_in_contacts_in_desktop_callback_form("Test", "9999999999")
#     page.accept_privacy_policy_checkbox()
#     page.push_contact_sent_button()
#     time.sleep(2)
#     page.should_be_successful_sent_message_window()

# def test_header_product_search(browser):
#     link = "https://makmen.ru"
#     page = BasePage(browser, link)
#     page.open()
#     page.accept_city_in_popup_massage()
#     page.search_for_product("слайсер")
#     page.should_be_found_products()

def test_register_new_user(browser):
    link = "https://makmen.ru"
    page = BasePage(browser, link)
    # browser.implicitly_wait(10)
    page.open()
    page.accept_city_in_popup_massage()
    page.fill_in_registration_form("Test_user3", "Test_surname12", "99999999999", "t443t@yandex.ru", "1111tes111")
    page.should_be_user_account_page("Test_user3")
