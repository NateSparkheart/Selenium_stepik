import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
browser.execute_script('window.open("https://www.google.com");')
time.sleep(5)

browser.quit()
