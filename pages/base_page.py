from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by: By, value: str):
        with allure.step(f'Find element by {by} with value "{value}"'):
            return self.driver.find_element(by, value)

    def finds(self, by: By, value: str):
        with allure.step(f'Find elements by {by} with value "{value}"'):
            return self.driver.find_elements(by, value)

    def open(self, url: str):
        with allure.step(f'Open URL: {url}'):
            self.driver.get(url)

    def element_is_exist(self, element, description="Element should be exist"):
        with allure.step(description):
            assert element is not None, description
    def element_is_not_exist(self, element, description="Search form exists, but it should not!"):
        if element is not None:
            with allure.step(description):
                raise AssertionError(description)

class GoogleMainPage(BasePage):
    URL = 'https://www.google.com'
    SEARCH_BOX = (By.NAME, 'q')

    def open(self):
        super().open(self.URL)

    def get_search_box(self):
        try:
            return self.find(*self.SEARCH_BOX)
        except Exception:
            return None