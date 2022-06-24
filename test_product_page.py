from .product_page import ProductPage  # импортируем класс с методами страницы товара
from .cart_page import CartPage # импортируем класс с методами страницы корзины
import pytest


@pytest.mark.mobile  # тест можно запускать в мобильной версии сайта
@pytest.mark.pc  # тест можно запускать в десктопной версии сайта
def test_item_can_be_added_to_cart(browser):
    page = ProductPage(browser)  # создаем объект класса ProductPage для доступа к методам страницы товара
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213") # открыть сайт
    page.click_on_add_to_cart() # кликнуть по кнопке "Добавить в корзину"
    page.click_on_continue_shopping() # кликнуть по кнопке "Продолжить покупки"
    page.should_be_number_on_cart_icon("1") # проверить ожидаемый результат


@pytest.mark.mobile
@pytest.mark.pc
def test_certain_amount_of_goods_can_be_added_to_cart_through_number_input_field(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.fill_in_number_field_near_to_cart_button("3")
    page.click_on_add_to_cart()
    page.click_on_continue_shopping()
    page.should_be_number_on_cart_icon("3")


@pytest.mark.mobile
@pytest.mark.pc
def test_certain_amount_of_goods_can_be_added_to_cart_through_click_on_plus_icon(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_plus_icon(2)
    page.click_on_add_to_cart()
    page.click_on_continue_shopping()
    page.should_be_number_on_cart_icon("3")


@pytest.mark.mobile
@pytest.mark.pc
def test_item_can_be_deleted_from_cart_in_cart_icon_menu(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_continue_shopping()
    page.should_be_number_on_cart_icon("1")
    page.click_on_cart_icon()
    page.click_on_delete_icon_in_cart_menu()
    page.should_be_number_on_cart_icon("0")


@pytest.mark.mobile
@pytest.mark.pc
def test_can_checkout_after_adding_item_to_cart(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_checkout_button()
    page.should_be_checkout_page()


@pytest.mark.mobile
@pytest.mark.pc
def test_item_can_be_deleted_from_cart_in_checkout_page(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_checkout_button()
    page = CartPage(browser)  # пересоздаем page как объект класса CartPage, т.к происходит переход в корзину"
    page.click_on_delete_icon_in_cart_list()
    page.should_be_empty_cart()


@pytest.mark.mobile
@pytest.mark.pc
def test_can_send_order_from_checkout_page(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_checkout_button()
    page = CartPage(browser)
    page.fill_in_name_field_in_checkout_form("This is test")
    page.fill_in_phone_field_in_checkout_form("9999999999")
    page.fill_in_email_field_in_checkout_form("test@yandex.ru")
    page.click_on_samovyvoz_radiobutton()
    page.click_on_confirm_order()
    page.should_be_order_confirmation_message()


@pytest.mark.pc
def test_price_in_cart_with_item_amount_pc(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_checkout_button()
    page = CartPage(browser)
    page.click_on_plus_icon_in_cart_item_list(1)
    page.should_be_sum_of_order("158 404.20")


@pytest.mark.mobile
def test_price_in_cart_with_item_amount_mobile(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_checkout_button()
    page = CartPage(browser)
    page.click_on_item_number_field_in_checkout()
    page.fill_in_item_number_field_in_checkout('2\n')
    page.should_be_sum_of_order("158 404.20")




