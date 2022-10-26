from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
browser.find_element(By.ID, 'book').click()

answer = str(math.log(abs(12*math.sin(int(browser.find_element(By.ID, 'input_value').text)))))
answer_area = browser.find_element(By.ID, 'answer')
browser.execute_script('return arguments[0].scrollIntoView(true);', answer_area)
answer_area.send_keys(answer)
browser.find_element(By.ID, 'solve').click()
print(browser.switch_to.alert.text.split(': ')[-1])

browser.quit()
