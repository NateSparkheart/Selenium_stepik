import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

result = ""

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    print("\nОткрываем хром..")
    yield browser
    print("\nЗакрываем хром..")
    browser.quit()
    print(result)

@pytest.mark.parametrize("lesson_id", [895, 896, 897, 898, 899, 903, 904, 905])
def test_answering(browser, lesson_id):
    global result
    link = f"https://stepik.org/lesson/236{lesson_id}/step/1"
    browser.get(link)
    browser.find_element(By.TAG_NAME, "textarea").send_keys(math.log(int(time.time() + 3599.8)))
    send_button = browser.find_element(By.CSS_SELECTOR, "[class='submit-submission']").click()
    test_result = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    try:
        assert browser.find_element(By.CLASS_NAME, "smart-hints__hint").text == "Correct!"
    except AssertionError:
        result += browser.find_element(By.CLASS_NAME, "smart-hints__hint").text



