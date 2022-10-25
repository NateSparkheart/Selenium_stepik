import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    a = int(browser.find_element(By.ID, 'num1').text)
    b = int(browser.find_element(By.ID, 'num2').text)
    Select(browser.find_element(By.ID, 'dropdown')).select_by_value(str(a+b))
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(5)
    browser.quit()

