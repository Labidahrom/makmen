from .main_page import MainPage  # импортируем класс с методами главной страницы
import pytest


@pytest.mark.mobile  # тест можно запускать в мобильной версии сайта
@pytest.mark.pc  # тест можно запускать в десктопной версии сайта
def test_should_be_right_location(browser):
    page = MainPage(browser)  # создаем объект класса MainPage что бы получить доступ ко всем методам главной страницы
    page.open("https://makmen.ru")  # открыть сайт
    page.click_on_accept_city_in_popup_massage()  # кликнуть по кнопке "Принять город"
    page.should_be_current_user_city_in_header("Санкт-Петербург")  # Проверка ожидаемого результата


@pytest.mark.mobile
@pytest.mark.pc
def test_city_can_be_changed_from_header(browser):
    page = MainPage(browser)
    page.open("https://makmen.ru")
    page.click_on_accept_city_in_popup_massage()
    page.click_on_city_name_in_header()
    page.click_on_first_city_name_in_city_list()
    page.should_be_first_city_from_city_list_in_header()


@pytest.mark.pc
def test_desktop_callback_form(browser):
    page = MainPage(browser)
    page.open("https://makmen.ru")
    page.click_on_accept_city_in_popup_massage()
    page.click_on_desktop_callback_form()
    page.fill_in_name_field_in_desktop_callback_form("This is test")
    page.fill_in_phone_number_field_in_desktop_callback_form("9999999999")
    page.click_on_accept_privacy_policy_checkbox_in_callback_form()
    page.click_on_contact_send_button_in_callback_form()
    page.should_be_successful_send_message_window()


@pytest.mark.mobile
@pytest.mark.pc
def test_header_product_search(browser):
    page = MainPage(browser)
    page.open("https://makmen.ru")
    page.click_on_accept_city_in_popup_massage()
    page.type_in_search_query_in_header("слайсер")
    page.click_on_search_button_in_header()
    page.should_be_found_products_in_search_results()


@pytest.mark.mobile
@pytest.mark.pc
def test_header_product_search_in_certain_category(browser):
    page = MainPage(browser)
    page.open("https://makmen.ru")
    page.click_on_accept_city_in_popup_massage()
    page.click_on_search_drop_down_category_meny()
    page.choose_second_item_in_search_drop_down_category_meny()
    page.type_in_search_query_in_header("блендер")
    page.click_on_search_button_in_header()
    page.should_be_found_products_in_search_results()
    page.clear_product_search_field()
    page.click_on_search_drop_down_category_meny()
    page.choose_second_item_in_search_drop_down_category_meny()
    page.type_in_search_query_in_header("слайсер")
    page.click_on_search_button_in_header()
    page.should_be_no_found_products_in_search_results()


@pytest.mark.pc
@pytest.mark.mobile
def test_register_new_user(browser):
    page = MainPage(browser)
    page.open("https://makmen.ru")
    page.click_on_accept_city_in_popup_massage()
    page.click_on_account_link_in_header_mobile()
    page.click_on_register_link_in_account_menu()
    page.fill_in_name_field_in_register_form("test1")
    page.fill_in_surname_field_in_register_form("testov")
    page.fill_in_phone_field_in_register_form("9999999999")
    page.fill_in_email_field_in_register_form("test-emaz6@yandex.ru")
    page.fill_in_password_field_in_register_form("9999999999")
    page.click_on_accept_privacy_policy_checkbox_in_register_form()
    page.click_on_register_form_send_button()
    page.should_open_user_account_page()


@pytest.mark.mobile
@pytest.mark.pc
@pytest.mark.xfail(reason="unresolved sigh in bug")
def test_sign_in_user(browser):
    page = MainPage(browser)
    page.open("https://makmen.ru")
    page.click_on_accept_city_in_popup_massage()
    page.click_on_account_link_in_header()
    page.click_on_sigh_in_link_in_account_menu()
    page.fill_in_email_field_in_sigh_in_form("test-email1361@yandex.ru")
    page.fill_in_password_field_in_sigh_in_form("9999999999")
    page.click_on_sign_in_form_send_button()
    page.should_open_user_account_page("test1")


@pytest.mark.mobile
@pytest.mark.pc
def test_scroll_up_screen_icon(browser):
    page = MainPage(browser)
    page.open("https://makmen.ru")
    page.click_on_accept_city_in_popup_massage()
    page.scroll_down_screen()
    page.click_on_scroll_up_icon()
    page.shoud_be_site_header_visible_on_screen()






