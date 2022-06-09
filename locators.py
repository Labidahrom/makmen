from selenium.webdriver.common.by import By


class MainPageLocators():
    CITY_POPUP_YES_BUTTON = (By.CSS_SELECTOR, "input.prmn-cmngr__confirm-btn.btn-primary")
    CITY_NAME_IN_HEADER = (By.CSS_SELECTOR, ".prmn-cmngr__city")
    FIRST_CITY_NAME_IN_CITY_MENU = (By.XPATH, "//a[@data-id='4115']")
    DESKTOP_CALLBACK_FORM = (By.CSS_SELECTOR, ".fly_callback")
    DESKTOP_CALLBACK_FORM_NAME_FIELD = (By.XPATH, "//input[@name='customer_name']")
    DESKTOP_CALLBACK_FORM_PHONE_FIELD = (By.XPATH, "//input[@name='customer_phone']")
    CALLBACK_FORM_POLICY_CHECKBOX = (By.CSS_SELECTOR, ".radio")
    CONTACT_SENT_BUTTON = (By.CSS_SELECTOR, "button.callback_button")
    SENT_MESSAGE_WINDOW = (By.CSS_SELECTOR, ".callback_success")
    HEADER_SEARCH_FIELD = (By.CSS_SELECTOR, "#div_search .form-control")
    HEADER_SEARCH_BUTTON = (By.CSS_SELECTOR, "#div_search button.search")
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product-layout")
    ACCOUNT_LINK = (By.CSS_SELECTOR, ".dropdown-toggle .hidden-xs")
    REGISTER_LINK = (By.XPATH, "//a[@onclick='register();']")
    SIGN_IN_LINK = (By.XPATH, "//a[@onclick='login();']")
    REGISTER_NAME = (By.XPATH, "//input[@name='firstname']")
    REGISTER_SURNAME = (By.XPATH, "//input[@name='lastname']")
    REGISTER_PHONE = (By.XPATH, "//input[@name='telephone']")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "div#popup_register input[name='email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "div#popup_register input[name='password']")
    REGISTER_FORM_PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "label.input span")
    REGISTER_FORM_SEND_BUTTON = (By.CSS_SELECTOR, ".register_button")
    SIGH_IN_FORM_SEND_BUTTON = (By.CSS_SELECTOR, ".login_button")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "div#popup_login input[name='email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "div#popup_login input[name='password']")
    ACCOUNT_HEADER = (By.CSS_SELECTOR, "span.hidden-xs")
    SCREEN_UP_ICON = (By.CSS_SELECTOR, ".fa-chevron-up")
    SEARCH_DROP_DOWN_MENU = (By.CSS_SELECTOR, "#div_search button.dropdown-toggle.btn-lg")
    SECOND_ITEM_IN_SEARCH_DROP_DOWN_MENU = (By.CSS_SELECTOR, ".open ul.dropdown-menu li:nth-child(2) a")


class ProductPageLocators():
    ADD_TO_CART_BUTTON_IN_PRODUCT_CARD = (By.CSS_SELECTOR, ".add_to_cart.button")
    CONTINUE_SHOPPING_LINK_IN_ADD_TO_CART_POPUP = (By.CSS_SELECTOR, ".col-xs-6.text-left a")
    NUMBER_IN_CART_ICON = (By.CSS_SELECTOR, "#cart-total")
    AMOUNT_OF_PRODUCT_NUMBER_FIELD = (By.CSS_SELECTOR, "#input-quantity")
    AMOUNT_OF_PRODUCT_PLUS_ICON = (By.CSS_SELECTOR, ".fa-plus.btn-default")
    CART_ICON_IN_HEADER = (By.CSS_SELECTOR, "#cart")
    DELETE_ICON_IN_CART_MENU_IN_HEADER = (By.CSS_SELECTOR, ".fa.fa-times")
    CHECKOUT_BUTTON_IN_AFTER_ADD_TO_CART_MENU = (By.CSS_SELECTOR, ".modal-body .btn-primary")
    CHECKOUT_HEADER = (By.CSS_SELECTOR, "div h1")


class CartPageLocators():
    DELETE_FROM_CART_LIST_ICON = (By.CSS_SELECTOR, ".btn-danger")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, ".content")