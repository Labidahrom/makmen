from selenium.webdriver.common.by import By


class BasePageLocators():
    CITY_POPUP_YES_BUTTON = (By.CSS_SELECTOR, ".prmn-cmngr__confirm-btn.btn-primary")
    CITY_NAME_IN_HEADER = (By.CSS_SELECTOR, ".prmn-cmngr__city")