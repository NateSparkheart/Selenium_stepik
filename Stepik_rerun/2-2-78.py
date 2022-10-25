import os

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    browser.find_element(By.CSS_SELECTOR, '.form-control:first-of-type').send_keys('Nate')
    browser.find_element(By.CSS_SELECTOR, 'div input:nth-child(4)').send_keys('Sparky')
    browser.find_element(By.CSS_SELECTOR, 'div input:nth-child(6)').send_keys('ns@g.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    browser.find_element(By.ID, 'file').send_keys(os.path.join(current_dir, 'file278.txt'))
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(10)
    browser.quit()