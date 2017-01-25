#!/usr/bin/env python3
# -*- coding:utf-8  -*-
'''
http://seleniumhq.github.io/selenium/docs/api/py/index.html
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://duckduckgo.com/')
        self.assertIn('DuckDuckGo', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)