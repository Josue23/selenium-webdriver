#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
http://seleniumhq.github.io/selenium/docs/api/py/index.html
- open a new Firefox browser
- load the Yahoo homepage
- search for “seleniumhq”
- close the browser
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()
