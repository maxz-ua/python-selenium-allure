import pytest
from pages.base_page import GoogleMainPage
import allure


@allure.feature('Google Failed Search')
@allure.story('Search box should NOT be present on homepage')
def test_google_search_box_not_exists(browser):
    page = GoogleMainPage(browser)
    page.open()
    search_box = page.get_search_box()
    page.element_is_not_exist(search_box)