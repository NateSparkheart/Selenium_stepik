import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]').send_keys('Ivan')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('Ivan@mail.ru')
    browser.find_element(By.CLASS_NAME, 'btn').click()
    WebDriverWait(browser, 5).until(EC.url_to_be('http://suninjuly.github.io/registration_result.html?'))
    return browser.find_element(By.TAG_NAME, 'h1').text


class TestRegPages(unittest.TestCase):
    def test_page_1st(self):
        self.assertEqual(fill_form('http://suninjuly.github.io/registration1.html'), "Congratulations! You have "
                                                                                     "successfully registered!",
                         'SNAP')

    def test_page_2nd(self):
        self.assertEqual(fill_form('http://suninjuly.github.io/registration2.html'), "Congratulations! You have "
                                                                                     "successfully registered!",
                         'SNAP')


if __name__ == '__main__':
    unittest.main()
