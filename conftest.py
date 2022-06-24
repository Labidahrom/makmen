import pytest
from selenium import webdriver  # импорт команд для управления браузером


def pytest_addoption(parser):  # обработчик опции ширины экрана для запуска мобильной/пк версии сайта
    parser.addoption('--screen', action='store', default='pc',
                     help="Choose screen size: mobile or PC")

@pytest.fixture()
def browser(request):  # фикстура с браузером для тестов
    browser = webdriver.Chrome()
    screen = request.config.getoption("screen")
    if screen == 'pc':
        browser.maximize_window()
    else:
        browser.set_window_size(400, 800)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
