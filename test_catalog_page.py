from .catalog_page import CatalogPage
from .locators import CatalogPageLocators
import time
from selenium import webdriver
from .locators import MainPageLocators
from .locators import CartPageLocators
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.mobile
@pytest.mark.pc
def test_number_of_displayed_items_can_be_changed(browser):
    page = CatalogPage(browser)
    page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
    page.shoold_be_certain_amount_of_items_on_catalog_page(15)
    page.click_on_number_of_items_on_page_drop_down_menu()
    page.choose_25_in_number_of_displayed_items_drop_down_menu()
    page.shoold_be_certain_amount_of_items_on_catalog_page(25)


@pytest.mark.mobile
@pytest.mark.pc
def test_min_to_max_price_sorting_on_catalogue_page(browser):
    page = CatalogPage(browser)
    page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
    page.click_on_sort_drop_down_menu()
    page.choose_min_to_max_price_sorting_on_drop_down_menu()
    page.should_be_min_to_max_sorted_item_by_price()


@pytest.mark.mobile
@pytest.mark.pc
def test_max_to_min_price_sorting_on_catalogue_page(browser):
    page = CatalogPage(browser)
    page.open("https://makmen.ru/teplovoe-oborudovanie/aksessuary-dlya-teplovogo-oborudovaniya/")
    page.click_on_sort_drop_down_menu()
    page.choose_max_to_min_price_sorting_on_drop_down_menu()
    page.should_be_max_to_min_sorted_item_by_price()


@pytest.mark.mobile
@pytest.mark.pc
def test_a_to_z_alphabet_sorting_on_catalogue_page(browser):
    page = CatalogPage(browser)
    page.open("https://makmen.ru/moechnoe-oborudovanie/aksessuary-dlya-moechnogo-oborudovaniya/")
    page.click_on_sort_drop_down_menu()
    page.choose_a_to_z_alphabet_sorting_on_drop_down_menu()
    page.should_be_a_to_z_sorted_item_by_alphabet()


@pytest.mark.mobile
@pytest.mark.pc
def test_z_to_a_alphabet_sorting_on_catalogue_page(browser):
    page = CatalogPage(browser)
    page.open("https://makmen.ru/moechnoe-oborudovanie/aksessuary-dlya-moechnogo-oborudovaniya/")
    page.click_on_sort_drop_down_menu()
    page.choose_z_to_a_alphabet_sorting_on_drop_down_menu()
    page.should_be_z_to_a_sorted_item_by_alphabet()


@pytest.mark.mobile
@pytest.mark.pc
@pytest.mark.parametrize('link', [
    "https://makmen.ru/teplovoe-oborudovanie/parokonvektomaty/",
    "https://makmen.ru/upakovochnoe-oborudovanie/apparaty-upakovochnye-vakuumnye/",
    "https://makmen.ru/elektromekhanicheskoe-oborudovanie/testomesy/",
    "https://makmen.ru/kholodilnoe-oborudovanie/shkafy-kholodilnye-morozilnye/",
    "https://makmen.ru/elektromekhanicheskoe-oborudovanie/slaysery/",
    "https://makmen.ru/teplovoe-oborudovanie/pechi-konvektsionnye/",
    "https://makmen.ru/kholodilnoe-oborudovanie/frizery/",
    "https://makmen.ru/teplovoe-oborudovanie/pechi-dlya-pitstsy/",
    "https://makmen.ru/teplovoe-oborudovanie/shkafy-zharochnye/",
    "https://makmen.ru/kholodilnoe-oborudovanie/shkafy-shokovogo-okhlazhdeniya-zamorozki/",
    "https://makmen.ru/teplovoe-oborudovanie/shkafy-rasstoechnye/",
    "https://makmen.ru/kholodilnoe-oborudovanie/shkafy-vitriny-vinnye/",
    "https://makmen.ru/teplovoe-oborudovanie/shkafy-pekarskie/",
    "https://makmen.ru/teplovoe-oborudovanie/poverkhnosti-zharochnye/",
    "https://makmen.ru/kholodilnoe-oborudovanie/stoly-kholodilnye-morozilnye/",
    "https://makmen.ru/elektromekhanicheskoe-oborudovanie/testoraskatyvayuschie-mashiny/",
    "https://makmen.ru/neytralnoe-tekhnologicheskoe-oborudovanie/zonty-ventilyatsionnye/",
    "https://makmen.ru/elektromekhanicheskoe-oborudovanie/ovoscherezatelnye-i-protirochnye-mashiny/",
    "https://makmen.ru/elektromekhanicheskoe-oborudovanie/testodeliteli/",
    "https://makmen.ru/elektromekhanicheskoe-oborudovanie/farshemeshalki/",
    "https://makmen.ru/teplovoe-oborudovanie/pechi-rotatsionnye/",
    "https://makmen.ru/teplovoe-oborudovanie/grili-kontaktnye/",
    "https://makmen.ru/elektromekhanicheskoe-oborudovanie/kartofelechistki-mashiny-dlya-chistki-korneplodov/",
    "https://makmen.ru/upakovochnoe-oborudovanie/zapayschiki-lotkov/",
    "https://makmen.ru/kholodilnoe-oborudovanie/bonety-i-shkafy-so-vstroennym-agregatom/",
    "https://makmen.ru/teplovoe-oborudovanie/apparaty-ponchikovye/",
    "https://makmen.ru/barnoe-i-kofeynoe-oborudovanie/sokookhladiteli-granitory/",
    "https://makmen.ru/teplovoe-oborudovanie/cheburechnitsy/",
    "https://makmen.ru/oborudovanie-dlya-razdachi-gotovykh-blyud/prilavki-neytralnye/",
    "https://makmen.ru/unox",
    "https://makmen.ru/teplovoe-oborudovanie/parokonvektomaty/unox/",
    "https://makmen.ru/teplovoe-oborudovanie/pechi-konvektsionnye/unox/",
    "https://makmen.ru/hurakan",
    "https://makmen.ru/kholodilnoe-oborudovanie/stoly-kholodilnye-morozilnye/hicold/",
    "https://makmen.ru/hicold",
    "https://makmen.ru/apach-bakery-line",
    "https://makmen.ru/sirman",
    "https://makmen.ru/frostor",
    "https://makmen.ru/kayman",
    "https://makmen.ru/fiorenzato",
    "https://makmen.ru/starfood",
    "https://makmen.ru/hamilton-beach",
    "https://makmen.ru/tefcold",
    "https://makmen.ru/cancan",
    "https://makmen.ru/dihr",
    "https://makmen.ru/hoshizaki",
    "https://makmen.ru/vema",
    "https://makmen.ru/menumaster",
    "https://makmen.ru/lainox",
    "https://makmen.ru/radax",
    "https://makmen.ru/cunill",
    "https://makmen.ru/varimixer"
])
def test_links_from_ads(browser, link):
    page = CatalogPage(browser)
    page.open(f"{link}")
    page.should_not_be_message_about_missing_page()
    page.should_be_header_of_the_page()








