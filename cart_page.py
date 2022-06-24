from .locators import CartPageLocators  # импорт локаторов для методов класса
from .base_page import BasePage  # импорт базового класса
from selenium.webdriver.common.keys import Keys # для отправки сочетания клавиш в форму обратной связи
import time  # для метода задержи исполнения, нужно в некоторых тестах


class CartPage(BasePage):
    def click_on_delete_icon_in_cart_list(self):
        button = self.browser.find_element(*CartPageLocators.DELETE_FROM_CART_LIST_ICON)  # найти элемент
        button.click()  # кликнуть по элементу

    def should_be_empty_cart(self):
        cart_text = self.browser.find_element(*CartPageLocators.EMPTY_CART_TEXT).text
        assert "Ваша корзина пуста!" in cart_text

    def fill_in_name_field_in_checkout_form(self, name):
        self.browser.find_element(*CartPageLocators.CHECKOUT_FORM_NAME_FIELD).send_keys(name)

    def fill_in_phone_field_in_checkout_form(self, phone):
        self.browser.find_element(*CartPageLocators.CHECKOUT_FORM_PHONE_FIELD).send_keys(phone)

    def fill_in_email_field_in_checkout_form(self, email):
        self.browser.find_element(*CartPageLocators.CHECKOUT_FORM_EMAIL_FIELD).send_keys(email)

    def click_on_samovyvoz_radiobutton(self):
        radiobutton = self.browser.find_element(*CartPageLocators.SAMOVYVOZ_RADIOBUTTON)
        radiobutton.click()

    def click_on_confirm_order(self):
        button = self.browser.find_element(*CartPageLocators.CONFIRM_ORDER_BUTTON_IN_CHECKOUT)
        button.click()

    def should_be_order_confirmation_message(self):
        time.sleep(2)
        order_confirmation_message = self.browser.find_element(*CartPageLocators.TEXT_IN_HEADER).text
        assert "Заказ успешно сформирован!" in order_confirmation_message

    def click_on_plus_icon_in_cart_item_list(self, how_many):
        plus_icon = self.browser.find_element(*CartPageLocators.PLUS_ICON_IN_CART_ICON_LIST)
        plus_icon.click()

    def click_on_item_number_field_in_checkout(self):
        number_field = self.browser.find_element(*CartPageLocators.ITEM_NUMBER_FIELD_IN_CHECKOUT)
        number_field.click()

    def fill_in_item_number_field_in_checkout(self, item_number):
        number_field = self.browser.find_element(*CartPageLocators.ITEM_NUMBER_FIELD_IN_CHECKOUT)
        time.sleep(1)
        number_field.send_keys(Keys.CONTROL, 'a')
        number_field.send_keys(item_number)


    def should_be_sum_of_order(self, sum):
        time.sleep(1)
        sum_of_order = self.browser.find_element(*CartPageLocators.SUM_OF_ORDER_IN_CHECKOUT).text
        print(sum_of_order)
        time.sleep(2)
        assert sum in sum_of_order

