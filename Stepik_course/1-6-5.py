import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser=webdriver.Chrome()
    browser.get(link)

    link_2 = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link_2.click()

    input_1 = browser.find_element(By.TAG_NAME, "input")
    input_1.send_keys("Nate")

    input_2 = browser.find_element(By.NAME, "last_name")
    input_2.send_keys("Sparkheart")

    input_3 = browser.find_element(By.CLASS_NAME, "city")
    input_3.send_keys("Moscow")

    input_4 = browser.find_element(By.ID, "country")
    input_4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

