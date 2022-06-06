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

    def shoud_be_1_number_on_cart_icon(self):
        number_in_cart = self.browser.find_element(*ProductPageLocators.NUMBER_IN_CART_ICON).text
        print(number_in_cart)
        assert number_in_cart == "1"
