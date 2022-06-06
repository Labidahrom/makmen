from .locators import MainPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

class BasePage():
    def __init__(self, browser, timeout = 10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)
        # self.browser.implicitly_wait(10)

    def find_element(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element














