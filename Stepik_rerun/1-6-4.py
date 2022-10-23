from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'input').send_keys('Roflan')
    browser.find_element(By.NAME, 'last_name').send_keys('Prikolovi4')
    browser.find_element(By.CLASS_NAME, 'city').send_keys('Vinnica')
    browser.find_element(By.ID, 'country').send_keys('Evrounit')
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(25)
    browser.quit()

