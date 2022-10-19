from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

try:
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Vlad")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Savickiy")

    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Krasnogorsk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/button[3]")
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()

