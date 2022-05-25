import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser