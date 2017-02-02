#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://selenium-python.readthedocs.io/getting-started.html
# http://stackoverflow.com/questions/25537567/how-to-open-website-and-fill-in-input-using-selenium-webdriver#25537644
# http://www.seleniumeasy.com/selenium-tutorials/css-selectors-tutorial-for-selenium-with-examples

# The selenium.webdriver module provides all the WebDriver implementations.
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

# provides useful methods for interacting HTML <select> element
from selenium.webdriver.support.ui import Select

# Next, the instance of Firefox WebDriver is created.
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
    # driver.get("http://semhora.com.br/")
driver.get("http://semhora.com.br/")

# Apart from the public methods given above, there are two private methods which
# might be useful with locators in page objects.
from selenium.webdriver.common.by import By
# Sexo = driver.find_element(By.XPATH, '//button[text()="Masculino"]')
# Sexo.click()

# The next line is an assertion to confirm that title has “app” word in it:
assert "app" in driver.title

# imprime todos os valores do <select> Assunto
all_options = driver.find_element_by_class_name("relacionadosContent")
# all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()

