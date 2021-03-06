from selenium import webdriver
import time


browser = webdriver.Chrome(executable_path='./webdrivers/chromedriver')
browser.implicitly_wait(15)
browser.get('https://www.rezultati.com/')

field_utakmice = browser.find_element_by_id('fs')
tables = field_utakmice.find_elements_by_class_name('soccer')

def update_feed(a=None, b=None):
    for table in tables[a:b]:
        thead = table.find_element_by_tag_name('thead')
        text = thead.text.split('\n')
        if len(text) > 1:
            text = text[1]
        print('\n-------\n', text, sep='') # league

        tbody = table.find_element_by_tag_name('tbody')
        trs = tbody.find_elements_by_tag_name('tr')
        for tr in trs:
            row = " ".join(tr.text.split('\n'))
            print(row) # resultats

update_feed()
a, b = 0, 0
while True:
    time.sleep(3)
    b += 10
    # update one part at a time, 10 leagues in this case
    update_feed(a, b)
    a = b
    if b > len(tables):
        # reset a and b to repeat the process
        a, b = 0, 0
