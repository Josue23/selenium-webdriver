#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://www.udemy.com/selenium-webdriver-with-python/learn/v4/t/lecture/1316666
44. Assert Methods

verifica o título da página
'''

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by  import By

import unittest


class AssertTitle(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("http://travelingtony.weebly.com")


    def test_AssertTitle(self):
        self.assertEqual(driver.title, "Traveling Tony's Photography - Welcome")


    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()




