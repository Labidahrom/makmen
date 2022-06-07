from .locators import ProductPageLocators
from .base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class ProductPage(BasePage):
    def click_on_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON_IN_PRODUCT_CARD)
        button.click()

    def click_on_continue_shopping(self):
        button = self.browser.find_element(*ProductPageLocators.CONTINUE_SHOPPING_LINK_IN_ADD_TO_CART_POPUP)
        button.click()

    def should_be_number_on_cart_icon(self, amount_of_product):
        time.sleep(1)
        number_in_cart = self.browser.find_element(*ProductPageLocators.NUMBER_IN_CART_ICON).text
        print(number_in_cart)
        assert number_in_cart == amount_of_product

    def fill_in_number_field_near_to_cart_button(self, amount):
        number_field = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_PRODUCT_NUMBER_FIELD)
        number_field.clear()
        number_field.send_keys(amount)

    def click_on_plus_icon(self, how_many):
        plus_icon = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_PRODUCT_PLUS_ICON)
        for i in range(how_many):
            plus_icon.click()

    def click_on_cart_icon(self):
        button = self.browser.find_element(*ProductPageLocators.CART_ICON_IN_HEADER)
        button.click()

    def click_on_delete_icon_in_cart_menu(self):
        button = self.browser.find_element(*ProductPageLocators.DELETE_ICON_IN_CART_MENU_IN_HEADER)
        button.click()

    def click_on_checkout_button(self):
        time.sleep(5)
        button = self.browser.find_element(*ProductPageLocators.CHECKOUT_BUTTON_IN_AFTER_ADD_TO_CART_MENU)
        button.click()

    def should_be_checkout_page(self):
        checkout_header = self.browser.find_element(*ProductPageLocators.CHECKOUT_HEADER).text
        assert "Оформление заказа" in checkout_header
