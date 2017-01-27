#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://selenium-python.readthedocs.io/getting-started.html

# The selenium.webdriver module provides all the WebDriver implementations.
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote.
from selenium import webdriver

# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

# provides useful methods for interacting HTML <select> element
from selenium.webdriver.support.ui import Select

# Next, the instance of Firefox WebDriver is created.
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get("http://semhora.com.br/contato")

# The next line is an assertion to confirm that title has “Python” word in it:
assert "app" in driver.title

#  the input text element can be located by its name attribute using find_element_by_name method
    # elem = driver.find_element_by_name("q")

#  To be safe, we’ll first clear any prepopulated text in the input field
#  (e.g. “Search”) so it doesn’t affect our search results:
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)

# After submission of the page, you should get the result if there is any.
# To ensure that some results are found, make an assertion:
    # assert "No results found." not in driver.page_source

# imprime todos os valores do <select> Assunto
element = driver.find_element_by_id("subject")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()

driver.quit()
