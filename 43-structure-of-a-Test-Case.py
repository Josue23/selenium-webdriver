#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://www.udemy.com/selenium-webdriver-with-python/learn/v4/t/lecture/1316618
43. Structure of a Test Case

the test case consists of three methods:
    def setUp
        # called fixture
        # consists navigate to the site

    def test_WaitForCheckOutPhotosButton
        # inherits from TestCase class

    def tearDow
        # called fixture
        # quits the webdriver

    unittest.main()
        # execites the test case by calling the unittest test runner

'''

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by  import By

import unittest


class WaitForElements(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com")


    def test_WaitForCheckOutPhotosButton(self):
        bLocator = "//span[.='Check out my coolest photos']"
        # <span class="wsite-button-inner">Check out my coolest photos</span> código html no site
        #
        seebutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, bLocator)))


    def test_waitForSearchField(self):
        sLocator = "input.wsite-search-input"
        # <input type='text' name='q' class='wsite-search-input' autocomplete='off' placeholder='Search'/>
        #
        sField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sLocator)))


    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
