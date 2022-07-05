# Makmen.ru test with Selenium WebDriver and Python

*Читать на другом языке: [русский](https://github.com/Labidahrom/makmen/blob/master/README.md)*

This repository contains tests written in Python for Selenium Webdriver using the Pytest framework. The tests check the functionality of the makmen.ru website, which can be used in a typical user scenario (feedback forms, a shopping cart, sorting product cards, and other elements).

# Structure of tests and description of modules
This tests use ***Page Object model***. That means that test methods are grouped into classes depending on the types of pages they belong to, and the actions for testing a web application are separated from their implementation in the code. Here the structure of the test files:
1. **Sets of test cases (test suites).** Test cases are combined into test suites based on which pages of the site they test: the main page, catalog page or product card. Each test case is a series of steps, the implementation of which should lead to a certain expected result. Each user step implemented in one method. As an example of test case from the test suite we can take checking the ability to switch the city in the site header. There are 3 test suites files in total:
* *test_main_page.py* - main page test suites
* *test_catalog_page.py* - catalog page test suites
* *test_product_page.py* - product page test suites
2. **Files with method codes from test cases (where these methods are implemented)**. Like suites of test cases, methods are grouped into classes based on their belonging to certain pages. This group includes 4 files:
* *main_page.py* - main page methods
* *catalog_page.py* - catalog page methods
* *product_page.py* - product page methods
* *cart_page.py* - cart page methods
3. **Support files**:
* *base_page.py* - parent class for all other classes
* *locators.py* - selectors for all tests here
* *conftest.py* - Pytest fixtures and parameters
* *pytest.ini* - test marker descriptions for Pytest

# Example of a test case implementation
For example we can take test case `test_should_be_right_location` from the set of test cases of the main page (*test_main_page.py*). The test checks the correctness of determining the geolocation of the site user::

    def test_should_be_right_location(browser):
        page = MainPage(browser)  # create an object of the MainPage class to access all methods of the main page
        page.open("https://makmen.ru")  # open website
        page.click_on_accept_city_in_popup_massage()  # click on the "Accept city" button
        page.should_be_current_user_city_in_header("Санкт-Петербург")  # Check expected result

As we can see, each step in the test case is a separate method with name that means what user action it implements. The code for the methods of this test case is described in the *MainPage.py* file а сами методы передаются при создании объекта класса. To check the expected result, a function called `should_be_current_user_city_in_header("St. Petersburg")` is used, which is implemented as a check of the expected value of the user's city name (it is passed as a function parameter) with the actual value.
 
Next, let's take one of the methods of the above test case: `click_on_accept_city_in_popup_massage()`. The method implements the user's click on the city selection confirmation button. This implemented like assigning a variable to the button element and then passing the click on it:

    def click_on_accept_city_in_popup_massage(self):
        button = self.browser.find_element(*MainPageLocators.CITY_POPUP_YES_BUTTON)  # find element
        button.click()  # click on an element

Selector `MainPageLocators.CITY_POPUP_YES_BUTTON` is imported from the *locators.py* module, and implemented by searching for the element by the CSS selector: `CITY_POPUP_YES_BUTTON = (By.CSS_SELECTOR, "input.prmn-cmngr__confirm-btn.btn-primary")`

This structure helps keep tests running because:
1. It allows to create different test cases without making changes to the function code. When each step of the user is described as a separate function, it is very easy to create new test cases by simply collecting them from ready-made methods as a constructor. For example, we can easily make any negative tests by removing some of the steps for filling in the fields from it or passing invalid values to them.
2. A fairly easy change in the code of the functions themselves, since the element locators are also placed in a separate module. If the CSS identifier of the element itself changes, we edit the code of this identifier in a separate file without touching the code of the function itself. Similarly, if we need to change something in the test environment (for example, instead of the Chrome browser, run tests in Firefox), we don't need to change the function code, but only need to change the browser driver in the *conftest.py* file.

 
# Requirements for the test environment and how to run tests
## Test environment requirements
Below is a list of applications required for this test suite to work:
* Windows
* Python (at least version 3.0)
* Selenium WebDriver
* Pytest
* Google Chrome
* ChromeDriver for Google Chrome

## Running Tests
Tests are run from the command line. In total, there are 3 files with sets of test cases to run:
* *test_main_page.py*
* *test_catalog_page.py*
* *test_product_page.py*

When starting, you must specify which version of the site you want to test (mobile or PC). This is done by passing a parameter to the command line. The launch of the PC version of the tests is done by the combination: 
pytest -m pc test_main_page.py - all tests of the PC version of the site for the main page will be launched. 
pytest -m mobile –screen=mobile test_main_page.py - all tests of the mobile version for the main page will be launched
