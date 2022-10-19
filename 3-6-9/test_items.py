import time

from selenium.webdriver.common.by import By


def test_user_can_see_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"), "add_to_basket_button is missing"
    time.sleep(5)
