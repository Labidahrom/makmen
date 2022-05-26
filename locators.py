from selenium.webdriver.common.by import By


class BasePageLocators():
    CITY_POPUP_YES_BUTTON = (By.CSS_SELECTOR, ".prmn-cmngr__confirm-btn.btn-primary")
    CITY_NAME_IN_HEADER = (By.CSS_SELECTOR, ".prmn-cmngr__city")
    FIRST_CITY_NAME_IN_CITY_MENU = (By.CSS_SELECTOR, "a.prmn-cmngr-cities__city-name")
    DESKTOP_CALLBACK_FORM = (By.CSS_SELECTOR, ".fly_callback")
    DESKTOP_CALLBACK_FORM_NAME_FIELD = (By.XPATH, "//input[@name='customer_name']")
    DESKTOP_CALLBACK_FORM_PHONE_FIELD = (By.XPATH, "//input[@name='customer_phone']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, ".radio")
    CONTACT_SENT_BUTTON = (By.CSS_SELECTOR, "button.callback_button")
    SENT_MESSAGE_WINDOW = (By.CSS_SELECTOR, ".callback_success")