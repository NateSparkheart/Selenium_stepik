import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

try:
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12*math.sin(int(browser.find_element(By.ID, 'input_value').text))))))
    button = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()