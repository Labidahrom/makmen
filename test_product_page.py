from .product_page import ProductPage
from .cart_page import CartPage
import time
from selenium import webdriver
from .locators import MainPageLocators
from .locators import CartPageLocators
from selenium.webdriver.common.by import By
import pytest

# def test_item_can_be_added_to_cart(browser):
#     page = ProductPage(browser)
#     page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
#     page.click_on_add_to_cart()
#     page.click_on_continue_shopping()
#     page.should_be_number_on_cart_icon("1")

# def test_certain_amount_of_goods_can_be_added_to_cart_through_number_input_field(browser):
#     page = ProductPage(browser)
#     page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
#     page.fill_in_number_field_near_to_cart_button("3")
#     page.click_on_add_to_cart()
#     page.click_on_continue_shopping()
#     page.should_be_number_on_cart_icon("3")

# def test_certain_amount_of_goods_can_be_added_to_cart_through_click_on_plus_icon(browser):
#     page = ProductPage(browser)
#     page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
#     page.click_on_plus_icon(2)
#     page.click_on_add_to_cart()
#     page.click_on_continue_shopping()
#     page.should_be_number_on_cart_icon("3")

# def test_item_can_be_deleted_from_cart_in_cart_icon_menu(browser):
#     page = ProductPage(browser)
#     page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
#     page.click_on_add_to_cart()
#     page.click_on_continue_shopping()
#     page.should_be_number_on_cart_icon("1")
#     page.click_on_cart_icon()
#     page.click_on_delete_icon_in_cart_menu()
#     page.should_be_number_on_cart_icon("0")
#
# def test_can_checkout_after_adding_item_to_cart(browser):
#     page = ProductPage(browser)
#     page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
#     page.click_on_add_to_cart()
#     page.click_on_checkout_button()
#     page.should_be_checkout_page()

def test_item_can_be_deleted_from_cart_in_checkout_page(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_checkout_button()
    page = CartPage(browser)
    page.click_on_delete_icon_in_cart_list()
    page.should_be_empty_cart()
