import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture
def browser():
    print('\nЗапускаем браузер для теста...')
    browser = webdriver.Chrome()
    browser.get(link)
    return browser


class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")