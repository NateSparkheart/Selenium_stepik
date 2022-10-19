from splinter import Browser

browser = Browser('chrome')
browser.visit('https://www.google.ru/')

element = browser.find_by_name('q')
element.fill('google')

