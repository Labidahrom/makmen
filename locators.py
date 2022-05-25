from selenium.webdriver.common.by import By


class BasePageLocators():
    CITY_POPUP_YES_BUTTON = (By.CSS_SELECTOR, ".prmn-cmngr__confirm-btn.btn-primary")
    CITY_NAME_IN_HEADER = (By.CSS_SELECTOR, ".prmn-cmngr__city")
    FIRST_CITY_NAME_IN_CITY_MENU = (By.CSS_SELECTOR, "a.prmn-cmngr-cities__city-name")