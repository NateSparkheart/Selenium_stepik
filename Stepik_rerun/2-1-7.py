import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

try:
    answer = str(math.log(abs(12*math.sin(int(browser.find_element(By.ID, 'treasure').get_attribute('valuex'))))))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(10)
    browser.quit()