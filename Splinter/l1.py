import time
from splinter import Browser

with Browser('chrome', user_agent="Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)") as b:
    # переход по урл
    b.visit('https://bestlifeonline.com/funniest-cat-memes-ever/')
    # b.reload()  #f5
    # print(b.title)  #site tittle
    # print(b.html) #vivod html
    # print(b.url)

    # методы поиска элементов
    # b.find_by_css('#vi-stories-gui-container > div > button')
    # b.find_by_xpath('//*[@id="main-content"]/div[2]/div[2]/div[2]/p[7]/img')
    # pervaya_pikcha = b.find_by_tag('img').first
    # poslednyaya_pikcha = b.find_by_tag('img').first
    # #b.find_by_name('some_name')
    # b.find_by_text('Randomly Attacking Arms Since 10,000 B.C.') # любой текст погчамп
    # b.find_by_id('vi-css-custom')
    # #b.find_by_value('1024')
    # # Можно вообще искать по индексу
    # pic = b.find_by_css('[class = "number-head-mod number-head-mod-standalone"]')[4]
    # по айди ВСЕГДА 1 ЭЛЕМЕНТ

    # методы поиска ссылок, возвращает список найденых элементов
    # b.links.find_by_text("culture of the internet has changed a lot of the past 10 years")
    # b.links.find_by_partial_text('culture of').click()
    # b.links.find_by_href('https://bestlifeonline.com/scary-urban-legends/')
    # b.links.find_by_partial_href('bestlifeonline.com/scary').click()
    # Можно то же самое внутри элемента/структуры
    # b.find_by_css('#main-content > div.row.main-area.main-area--flex > div.main-content > div.content.noskimwords > '
    #               'p:nth-child(462)').links.find_by_text('Grumpy Cat').click()

    # Поиск внутри цепочки элементов
    # imgs = b.find_by_tag('img')
    # within_imgs = imgs.first.find_by_value("1024")

    # finds возвращают пустые списки в случае отсутствия элемента, но если была команда на взаимодействие с ним,
    # вернется ElementDoesNotExist исключение

    time.sleep(3)

    # Okna:
    # browser.windows  # all open windows
    # browser.windows[0]  # the first window
    # browser.windows[window_name]  # the window_name window
    # browser.windows.current  # the current window
    # browser.windows.current = browser.windows[3]  # set current window to window 3
    #
    # window = browser.windows[0]
    # window.is_current  # boolean - whether window is current active window
    # window.is_current = True  # set this window to be current window
    # window.next  # the next window
    # window.prev  # the previous window
    # window.close()  # close this window
    # window.close_others()  # close all windows except this one
