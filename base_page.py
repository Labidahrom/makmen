from selenium.webdriver.support.ui import WebDriverWait  # модуль явных ожиданий, нужен для части тестов
from selenium.webdriver.support import expected_conditions as EC  # модуль условий ожидания, нужен для части тестов


class BasePage(): #создаем базовый класс
    def __init__(self, browser):  # конструктор класса
        self.browser = browser  # определяем браузер как обязательный атрибут класса

    def open(self, url):
        self.browser.get(url)

    def find_element(self, locator):  # метод поиска элементов
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element














