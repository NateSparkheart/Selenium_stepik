from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


class TestMainPage1():
    @classmethod
    def setup_class(self):
        print('\nЗапускаем браузер для первого тестового набора...')
        self.browser = webdriver.Chrome()
        self.browser.get(link)

    @classmethod
    def teardown_class(self):
        print('\nЗакрываем браузер...')
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('Запускаем тест ссылки на логин...')
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('\nЗапускаем тест ссылки на корзину')
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():
    def setup_method(self):
        print("\nЗапускаем браузер для теста из второго набора...")
        self.browser = webdriver.Chrome()
        self.browser.get(link)

    def teardown_method(self):
        print('\nЗакрываем браузер...')
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('Запускаем тест ссылки на логин...')
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('Запускаем тест ссылки на корзину...')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")