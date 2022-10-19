from splinter import Browser

browser = Browser('chrome')  # пустые скобки = по умолчанию файрфокс

browser.visit('http://google.com')

input_element = browser.find_by_name('q').fill('splinter - python acceptance testing for web applications')


button_element = browser.find_by_name('btnK').click()

if browser.is_text_present('splinter.readthedocs.io'):
    print("Yeas, we got it! ;)")
else:
    print("Alas!")

browser.quit()


