from .base_page import BasePage
import time

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

def test_desktop_callback_form(browser):
    link = "https://makmen.ru"
    page = BasePage(browser, link)
    page.open()
    page.accept_city_in_popup_massage()
    page.open_desktop_callback_form()
    time.sleep(2)
    page.fill_in_contacts_in_desktop_callback_form("Test", "9999999999")
    page.accept_privacy_policy_checkbox()
    page.push_contact_sent_button()
    time.sleep(2)
    page.should_be_successful_sent_message_window()