#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/selenium-webdriver-with-python/learn/v4/t/lecture/1279220
35. Implicit wait Vs. Explicit wait

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
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# driver = webdriver.Chromium("/usr/bin/chromedriver")

# wait for 15 seconds
driver.implicitly_wait(15)

driver.get("https://duckduckgo.com/")

# search using css selector
searchField = driver.find_element_by_css_selector("input[name=q]")
searchField.send_keys('semhora' + Keys.RETURN)
searchField.submit()


driver.quit()




