import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'first').send_keys('Ivan')
    browser.find_element(By.CLASS_NAME, 'second').send_keys('Ivanov')
    browser.find_element(By.CLASS_NAME, 'third').send_keys('Ivan@mail.ru')
    browser.find_element(By.CLASS_NAME, 'btn').click()
    WebDriverWait(browser, 5).until(EC.url_to_be('http://suninjuly.github.io/registration_result.html?'))
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(5)
    browser.quit()


