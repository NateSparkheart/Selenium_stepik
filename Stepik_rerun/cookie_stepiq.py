import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from auth_data import slog, spass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle # сохранение куки


browser = webdriver.Chrome()
browser.get('https://stepik.org/catalog')
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'ember234')))
# browser.find_element(By.ID, 'ember234').click()
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'login')))
# browser.find_element(By.NAME, 'login').send_keys(slog)
# browser.find_element(By.NAME, 'password').send_keys(spass)
# browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
# time.sleep(3)

# # cookies
# pickle.dump(browser.get_cookies(), open(f"stepik_cookies", "wb"))
# #
for cookie in pickle.load(open(f"stepik_cookies", "rb")):
    browser.add_cookie(cookie)

browser.refresh()
time.sleep(10)

browser.quit()