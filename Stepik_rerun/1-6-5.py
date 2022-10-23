from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/find_link_text')
browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))).click()


browser.find_element(By.TAG_NAME, 'input').send_keys('Roflan')
browser.find_element(By.NAME, 'last_name').send_keys('Prikolovi4')
browser.find_element(By.CLASS_NAME, 'city').send_keys('Vinnica')
browser.find_element(By.ID, 'country').send_keys('Evrounit')
browser.find_element(By.CSS_SELECTOR, '.btn').click()

