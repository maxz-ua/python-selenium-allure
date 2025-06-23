import pytest
from pages.base_page import GoogleMainPage
import allure

@allure.feature('Google Smoke Search')
@allure.story('Search box is present on homepage')
@pytest.mark.smoke
def test_google_search_box_exists(browser):
    page = GoogleMainPage(browser)
    page.open()
    search_box = page.get_search_box()
    page.element_is_exist(search_box)