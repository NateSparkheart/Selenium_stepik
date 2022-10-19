from splinter import Browser

with Browser('chrome') as b:
    b.visit('https://bestlifeonline.com/funniest-cat-memes-ever/')
    # GET VALUE
    print(b.find_by_css('#main-content > div.container-fluid.post-head.text-center > div:nth-child(2) > div > h1').value)

