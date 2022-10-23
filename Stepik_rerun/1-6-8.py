from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'input').send_keys('Roflan')
    browser.find_element(By.NAME, 'last_name').send_keys('Prikolovi4')
    browser.find_element(By.CLASS_NAME, 'city').send_keys('Vinnica')
    browser.find_element(By.ID, 'country').send_keys('Evrounit')
    browser.find_element(By.XPATH, '/html/body/div[1]/form/div[6]/button[3]').click()

finally:
    time.sleep(25)
    browser.quit()

