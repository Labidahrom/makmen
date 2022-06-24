from selenium.webdriver.support.ui import WebDriverWait  # модуль явных ожиданий, нужно для части тестов
from selenium.webdriver.support import expected_conditions as EC  # модуль условий, нужно для части тестов


class BasePage():
    def __init__(self, browser, timeout = 10):  # конструктор класса
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)


    def find_element(self, locator):  # метод поиска элементов
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element














