from selenium.webdriver.common.by import By  # библиотека для работы селекторов


class MainPageLocators():  # локаторы для главной страницы
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
    ACCOUNT_LINK_MOBILE = (By.CSS_SELECTOR, ".fa-user")
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
    USER_PAGE_HEADER = (By.CSS_SELECTOR, "h3 span")
    SCREEN_UP_ICON = (By.CSS_SELECTOR, ".fa-chevron-up")
    SEARCH_DROP_DOWN_MENU = (By.CSS_SELECTOR, "#div_search button.dropdown-toggle.btn-lg")
    SECOND_ITEM_IN_SEARCH_DROP_DOWN_MENU = (By.CSS_SELECTOR, ".open ul.dropdown-menu li:nth-child(2) a")
    UNDER_LOGO_TEXT = (By.CSS_SELECTOR, ".logo-title div.title")


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
    TEXT_IN_HEADER = (By.CSS_SELECTOR, "#content h1")
    CHECKOUT_FORM_NAME_FIELD = (By.CSS_SELECTOR, "#customer_firstname")
    CHECKOUT_FORM_PHONE_FIELD = (By.CSS_SELECTOR, "#customer_telephone")
    CHECKOUT_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#customer_email")
    SAMOVYVOZ_RADIOBUTTON = (By.XPATH, "//label[@for='pickup.pickup']")
    CONFIRM_ORDER_BUTTON_IN_CHECKOUT = (By.CSS_SELECTOR, ".simplecheckout-button-right #button-confirm")
    PLUS_ICON_IN_CART_ICON_LIST = (By.CSS_SELECTOR, ".input-group-btn .fa-plus")
    SUM_OF_ORDER_IN_CHECKOUT = (By.CSS_SELECTOR, "#total_total .simplecheckout-cart-total-value")
    ITEM_NUMBER_FIELD_IN_CHECKOUT = (By.XPATH, "//input[@data-onchange='changeProductQuantity']")


class CatalogPageLocators():
    NUMBER_OF_ITEMS_DROP_DOWN_MENU = (By.CSS_SELECTOR, "#input-limit")
    ITEMS_25_IN_DROP_DOWN_MENU = (By.XPATH, "//option[text()='25']")
    ITEM_PRICE_IN_LISTING = (By.CSS_SELECTOR, ".caption .price")
    SORTING_DROP_DOWN_MENU = (By.CSS_SELECTOR, "#input-sort")
    MIN_TO_MAX_IN_DROP_DOWN_MENU = (By.XPATH, "//option[text()='По цене (возрастанию)']")
    MAX_TO_MIN_IN_DROP_DOWN_MENU = (By.XPATH, "//option[text()='По цене (убыванию)']")
    A_TO_Z_IN_DROP_DOWN_MENU = (By.XPATH, "//option[text()='По имени (A - Я)']")
    ITEM_NAMES_IN_LISTING = (By.CSS_SELECTOR, ".caption a[href*='makmen']")
    Z_TO_A_IN_DROP_DOWN_MENU = (By.XPATH, "//option[text()='По имени (Я - A)']")
    PAGE_HEADER = (By.CSS_SELECTOR, "div h1")

