from .product_page import ProductPage
import time
from selenium import webdriver
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
import pytest

def test_item_can_be_added_to_cart(browser):
    page = ProductPage(browser)
    page.open("https://makmen.ru/index.php?route=product/product&product_id=110213")
    page.click_on_add_to_cart()
    page.click_on_continue_shopping()
    page.shoud_be_1_number_on_cart_icon()