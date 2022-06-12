from .base_page import BasePage
from .locators import CatalogPageLocators
from .locators import MainPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class CatalogPage(BasePage):
    def shoold_be_certain_amount_of_items_on_catalog_page(self, number_of_items):
        items_on_catalog_page = len(self.browser.find_elements(*MainPageLocators.PRODUCT_CARD))
        print("Results found:", items_on_catalog_page)
        assert items_on_catalog_page == number_of_items

    def click_on_number_of_items_on_page_drop_down_menu(self):
        menu = self.browser.find_element(*CatalogPageLocators.NUMBER_OF_ITEMS_DROP_DOWN_MENU)
        menu.click()

    def choose_25_in_number_of_displayed_items_drop_down_menu(self):
        item25 = self.browser.find_element(*CatalogPageLocators.ITEMS_25_IN_DROP_DOWN_MENU)
        item25.click()

    def click_on_sort_drop_down_menu(self):
        menu = self.browser.find_element(*CatalogPageLocators.SORTING_DROP_DOWN_MENU)
        menu.click()

    def choose_min_to_max_price_sorting_on_drop_down_menu(self):
        min_to_max = self.browser.find_element(*CatalogPageLocators.MIN_TO_MAX_IN_DROP_DOWN_MENU)
        min_to_max.click()

    def should_be_min_to_max_sorted_item_by_price(self):
        ele_list = self.browser.find_elements(*CatalogPageLocators.ITEM_PRICE_IN_LISTING)
        zero_price = 0
        counter = 0
        for i in range(len(ele_list)):
            price = float((ele_list[i].text)[0:-2].replace(" ", ""))
            print(price)
            if price >= zero_price:
                zero_price = price
                counter += 1
        assert counter == 15

    def choose_max_to_min_price_sorting_on_drop_down_menu(self):
        max_to_min = self.browser.find_element(*CatalogPageLocators.MAX_TO_MIN_IN_DROP_DOWN_MENU)
        max_to_min.click()

    def should_be_max_to_min_sorted_item_by_price(self):
        ele_list = self.browser.find_elements(*CatalogPageLocators.ITEM_PRICE_IN_LISTING)
        counter = 0
        for i in range(len(ele_list)):
            price = float((ele_list[i].text)[0:-2].replace(" ", ""))
            print(price)
            if i == 0:
                zero_price = price
            if price <= zero_price:
                zero_price = price
                counter += 1
        assert counter == 15
