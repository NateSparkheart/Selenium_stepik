import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.find_element(By.CLASS_NAME, 'btn').click()
browser.switch_to.window(browser.window_handles[1])
answer = str(math.log(abs(12*math.sin(int(browser.find_element(By.ID, 'input_value').text)))))
browser.find_element(By.ID, 'answer').send_keys(answer)
browser.find_element(By.CLASS_NAME, 'btn').click()
browser.quit()