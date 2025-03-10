import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_configuration():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    yield
    browser.quit()