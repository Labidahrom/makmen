from .base_page import BasePage

def test_should_be_right_location(browser):
    link = "https://makmen.ru"
    page = BasePage(browser, link)
    page.open()
    page.accept_city_in_popup_massage()
    page.should_be_right_city_in_header("Санкт-Петербург")

def test_can_be_changed_from_header(browser):
    link = "https://makmen.ru"
    page = BasePage(browser, link)
    page.open()
    page.accept_city_in_popup_massage()
    page.can_change_city_in_the_header_menu()
