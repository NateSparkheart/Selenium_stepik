import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def browser():
    print("\nЗапускаем браузер для теста..")
    browser = webdriver.Chrome()
    yield browser
    print("\nПока браузер!")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print("\nГотовим данные для каждого теста по умолчанию (автоюз фикстура)")

class TestMainPage1():  # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("\nПервый пошел..")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("\nПервый всё!")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\nВторой пошел..")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("\nВторой всё!")