from .locators import CartPageLocators
from .base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

class CartPage(BasePage):
    def click_on_delete_icon_in_cart_list(self):
        button = self.browser.find_element(*CartPageLocators.DELETE_FROM_CART_LIST_ICON)
        button.click()

    def should_be_empty_cart(self):
        cart_text = self.browser.find_element(*CartPageLocators.EMPTY_CART_TEXT).text
        assert "Ваша корзина пуста!" in cart_text