#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://selenium-python.readthedocs.io/getting-started.html
# http://stackoverflow.com/questions/25537567/how-to-open-website-and-fill-in-input-using-selenium-webdriver#25537644

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


# preenche o campo Seu nome
name = driver.find_element_by_id("name")
name.send_keys('Maria da Silva')
name.submit()

# preenche o campo Seu email
name = driver.find_element_by_id("email")
name.send_keys('test@test.com')
name.submit()

# preenche o campo Seu Seu telefone
phone = driver.find_element_by_id("phone")
phone.send_keys('11 97654 5682')
phone.submit()

# preenche o campo Qual evento?
evento = driver.find_element_by_id("event")
evento.send_keys('Event')
evento.submit()

# imprime todos os valores do <select> Assunto
element = driver.find_element_by_id("subject")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()

# preenche o campo Mensagem
mensagem = driver.find_element_by_id("message")
mensagem.send_keys('Lorem Ipsum Generator provides a GTK+ graphical user interface, a command-line interface, and a Python module that generate random "lorem ipsum" text (a popular kind of dummy text). ')
mensagem.submit()

select = Select(driver.find_element_by_name('subject'))
# select.select_by_index(index)
# select.select_by_visible_text("text")
select.select_by_value('Reclamação')

driver.quit()
