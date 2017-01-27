#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# https://selenium-python.readthedocs.io/getting-started.html

# The selenium.webdriver module provides all the WebDriver implementations.
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote.
from selenium import webdriver

# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

# Next, the instance of Firefox WebDriver is created.
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get("http://www.python.org")

# The next line is an assertion to confirm that title has “Python” word in it:
assert "Python" in driver.title

#  the input text element can be located by its name attribute using find_element_by_name method
elem = driver.find_element_by_name("q")

#  To be safe, we’ll first clear any prepopulated text in the input field
#  (e.g. “Search”) so it doesn’t affect our search results:
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# After submission of the page, you should get the result if there is any.
# To ensure that some results are found, make an assertion:
assert "No results found." not in driver.page_source


driver.close()
'''

# https://selenium-python.readthedocs.io/getting-started.html
# o mesmo exemplo, usando unittest
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inheriting from TestCase class is the way to tell unittest module
# that this is a test case
class PythonOrgSearch(unittest.TestCase):

    # Here you are creating the instance of Firefox WebDriver.
    def setUp(self):
        self.driver = webdriver.Firefox()

    # This is the test case method.
    def test_search_in_python_org(self):
        driver = self.driver

        # The driver.get method will navigate to a page given by the URL
        driver.get("http://www.python.org")

        # This is an assertion to confirm that title has “Python” word in it:
        self.assertIn("Python", driver.title)

        # the input text element can be located by its
        # name attribute using find_element_by_name method
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    # The tearDown method will get called after every test method
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
