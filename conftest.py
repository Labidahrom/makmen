import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--screen', action='store', default='pc',
                     help="Choose screen size: mobile or PC")

@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()
    screen = request.config.getoption("screen")
    if screen == 'pc':
        browser.maximize_window()
    else:
        browser.set_window_size(400, 800)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.fixture()
def mobile_browser(request):
    browser = webdriver.Chrome()
    browser.set_window_size(400,800)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()