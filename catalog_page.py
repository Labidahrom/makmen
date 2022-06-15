from .base_page import BasePage
from .locators import CatalogPageLocators
from .locators import CartPageLocators
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
        assert counter == len(ele_list)

    def choose_max_to_min_price_sorting_on_drop_down_menu(self):
        max_to_min = self.browser.find_element(*CatalogPageLocators.MAX_TO_MIN_IN_DROP_DOWN_MENU)
        max_to_min.click()

    def should_be_max_to_min_sorted_item_by_price(self):
        item_list = self.browser.find_elements(*CatalogPageLocators.ITEM_PRICE_IN_LISTING)
        counter = 0
        for i in range(len(item_list)):
            price = float((item_list[i].text)[0:-2].replace(" ", ""))
            print(price)
            if i == 0:
                zero_price = price
            if price <= zero_price:
                zero_price = price
                counter += 1
        assert counter == 15

    def choose_a_to_z_alphabet_sorting_on_drop_down_menu(self):
        a_to_z = self.browser.find_element(*CatalogPageLocators.A_TO_Z_IN_DROP_DOWN_MENU)
        a_to_z.click()
        
    def should_be_a_to_z_sorted_item_by_alphabet(self):
        item_list = self.browser.find_elements(*CatalogPageLocators.ITEM_NAMES_IN_LISTING)
        counter = 0
        for i in range(len(item_list)):
            print(ord(item_list[i].text[0]))
            item_first_lеtter_code = ord(item_list[i].text[0])
            if i == 0:
                zero_code = item_first_lеtter_code
            if item_first_lеtter_code >= zero_code:
                zero_code = item_first_lеtter_code
                counter += 1
        assert counter == len(item_list)

    def choose_z_to_a_alphabet_sorting_on_drop_down_menu(self):
        z_to_a = self.browser.find_element(*CatalogPageLocators.Z_TO_A_IN_DROP_DOWN_MENU)
        z_to_a.click()

    def should_be_z_to_a_sorted_item_by_alphabet(self):
        item_list = self.browser.find_elements(*CatalogPageLocators.ITEM_NAMES_IN_LISTING)
        counter = 0
        for i in range(len(item_list)):
            print(ord(item_list[i].text[0]))
            item_first_lеtter_code = ord(item_list[i].text[0])
            if i == 0:
                zero_code = item_first_lеtter_code
            if item_first_lеtter_code <= zero_code:
                zero_code = item_first_lеtter_code
                counter += 1
        assert counter == len(item_list)

    def should_not_be_message_about_missing_page(self):
        header_text = self.browser.find_element(*CatalogPageLocators.PAGE_HEADER).text
        assert "Запрашиваемая страница не найдена!" not in header_text

    def should_be_header_of_the_page(self):
        header_text = self.browser.find_element(*CatalogPageLocators.PAGE_HEADER).text
        print(header_text)
        assert len(header_text) > 0


