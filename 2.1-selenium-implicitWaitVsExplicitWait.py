#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/selenium-webdriver-with-python/learn/v4/t/lecture/1279220
35. Implicit wait Vs. Explicit wait

descobrir o segundo elemento com a tag <a> em um documento html
(//a)[2]

Implicit Wait
- webdriver polls the DOM for a certain amount of time when trying to find an element.

- Set for the lifetime of the webdriver object instance ( = set until you quit the driver )

- "NoSuchElementException" is thrown(lançada) if the element is not found.


Explicit Wait
- before waits for a certain condition to be true before proceeding with the next commands

- has a timeout

- if the condition is true before the timeout then webdriver proceeds with the next commands

- if the condition is not true in the allocated time, then a "TimeoutException" is thrown(lançada)

'''

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

# expected conditions, usado para verificar expected conditions
from selenium.webdriver.support import expected_conditions as EC

# provide locate extrategies
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver = webdriver.Chromium("/usr/bin/chromedriver")

driver.get("http://duckduckgo.com/")

# define the search fields
flocator = "input[name=q]"

# webdriver wait for max 10 seconds
try:
    searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, flocator)))
finally:
    driver.quit()

