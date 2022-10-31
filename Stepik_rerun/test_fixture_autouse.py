import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture(scope='function')
def browser():
    print('\nЗапускаем браузер для теста...')
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print('\nВыходим из браузера...')
    browser.quit()


@pytest.fixture(autouse=True, scope='class')
def plus_moral():
    yield plus_moral
    print('\nFriendly reminder that ur a legend!')



class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        print('\nЗапускаем первый тест')
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\nЗапускаем второй тест')
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")