import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value")
y = calc(x.text)

text_area = browser.find_element(By.ID, "answer")
text_area.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox").click()

radiobutton = browser.find_element(By.ID, "robotsRule").click()

submit_button = browser.find_element(By.TAG_NAME, "button").click()


time.sleep(15)
browser.quit()