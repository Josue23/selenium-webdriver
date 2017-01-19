#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://stackoverflow.com/questions/5503489/python-selenium-example-doesnt-work-says-no-module-named-keys
http://seleniumhq.github.io/selenium/docs/api/py/index.html
- load the page at the given URL
- open a new Firefox browser
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
browser = webdriver.Firefox()

# go to the URL
browser.get('http://seleniumhq.org/')

print(browser.title)
