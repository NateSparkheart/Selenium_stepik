from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration1.html")

labels = browser.find_elements(By.TAG_NAME, 'label')
inputs = browser.find_elements(By.TAG_NAME, "input")

for i, label in enumerate(labels): # i - это номер элемента (с нулевого), label - содержание, представленное текстом
    if label.text[-1] == '*':
        inputs[i].send_keys('ROFL') # в i-тое инпутсов вставляем рофлы

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_element = browser.find_element(By.TAG_NAME, "h1") # Элемент по тэгу
assert "Congratulations! You have successfully registered!" == welcome_text_element.text
# метод .text выделяет ТОЛЬКО ТЕКСТ ЭЛЕМЕНТА

time.sleep(10)
browser.quit()