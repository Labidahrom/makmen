from .catalog_page import CatalogPage
from .locators import CatalogPageLocators
import time
from selenium import webdriver
from .locators import MainPageLocators
from .locators import CartPageLocators
from selenium.webdriver.common.by import By
import pytest


# def test_number_of_displayed_items_can_be_changed(browser):
#     page = CatalogPage(browser)
#     page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
#     page.shoold_be_certain_amount_of_items_on_catalog_page(15)
#     page.click_on_number_of_items_on_page_drop_down_menu()
#     page.choose_25_in_number_of_displayed_items_drop_down_menu()
#     page.shoold_be_certain_amount_of_items_on_catalog_page(25)

def test_min_to_max_price_sorting_on_catalogue_page(browser):
    page = CatalogPage(browser)
    page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
    page.click_on_sort_drop_down_menu()
    page.choose_min_to_max_price_sorting_on_drop_down_menu()
    page.should_be_min_to_max_sorted_item_by_price()

def test_max_to_min_price_sorting_on_catalogue_page(browser):
    page = CatalogPage(browser)
    page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
    page.click_on_sort_drop_down_menu()
    page.choose_max_to_min_price_sorting_on_drop_down_menu()
    page.should_be_max_to_min_sorted_item_by_price()
#
# def test_a_to_z_alphabet_sorting_on_catalogue_page(browser):
#     page = CatalogPage(browser)
#     page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
#     page.should_be_unsorted_item_by_alphabet()
#     page.click_on_sort_drop_down_menu()
#     page.choose_a_to_z_alphabet_sorting_on_drop_down_menu()
#     page.should_be_a_to_z_sorted_item_by_alphabet()
#
# def test_z_to_a_alphabet_sorting_on_catalogue_page(browser):
#     page = CatalogPage(browser)
#     page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
#     page.should_be_unsorted_item_by_alphabet()
#     page.click_on_sort_drop_down_menu()
#     page.choose_z_to_a_alphabet_sorting_on_drop_down_menu()
#     page.should_be_z_to_a_sorted_item_by_alphabet()
#
# @pytest.mark.parametrize('link', [
#     "https://makmen.ru/elektromekhanicheskoe-oborudovanie/kartofelechistki-mashiny-dlya-chistki-korneplodov/",
#     "https://makmen.ru/elektromekhanicheskoe-oborudovanie/ovoscherezatelnye-i-protirochnye-mashiny/",
#     "https://makmen.ru/teplovoe-oborudovanie/shkafy-pekarskie/"
#     ])
# def test_links_from_ads(browser):
#     page = CatalogPage(browser)
#     page.open({link})
#     page.should_not_be_message_about_missing_page()
#     page.should_be_some_page_content()








