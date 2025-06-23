import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Type of browser. E.g. chrome or firefox"
    )

@pytest.fixture(scope='function')
def browser(request):
    browser_type = request.config.getoption("--browser")
    driver = None
    if browser_type == "chrome":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        with allure.step(f'Open browser: {browser_type}'):
            driver = webdriver.Chrome(options=options)
    elif browser_type == "firefox":
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        with allure.step(f'Open browser: {browser_type}'):
            driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")
    driver.implicitly_wait(10)
    yield driver
    with allure.step(f'Close browser: {browser_type}'):
        driver.quit() 