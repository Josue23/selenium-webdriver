#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/selenium-webdriver-with-python/learn/v4/t/lecture/1279214

Este teste acessa o site
https://duckduckgo.com/
'''

from selenium import webdriver

driver = webdriver.Firefox()
# driver = webdriver.Chromium("/usr/bin/chromedriver")

driver.get("https://duckduckgo.com/")

driver.quit()
