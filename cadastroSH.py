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
    # driver.get("http://semhora.com.br/")
driver.get("http://semhora.com.br/cadastro")

# Apart from the public methods given above, there are two private methods which
# might be useful with locators in page objects.
from selenium.webdriver.common.by import By
# Sexo = driver.find_element(By.XPATH, '//button[text()="Masculino"]')
# Sexo.click()

# The next line is an assertion to confirm that title has “Python” word in it:
assert "app" in driver.title



# preenche o campo Nome Completo
name = driver.find_element_by_id("txt_nome")
name = driver.find_element_by_name('txt_nome')
name.send_keys('nome sobrenome')
name.submit()


# preenche o campo Data de nascimento
phone = driver.find_element_by_id("txt_nascimento")
phone.send_keys('11111111')
phone.submit()

genero = driver.find_element_by_id("options_genero")
genero.click()


# preenche o campo Confirmar Celular
celular = driver.find_element_by_id("txt_celular")
celular.send_keys('11 11111 1111')
celular.submit()

# preenche o campo Confirmar email
# email = driver.find_element_by_id("txt_email")
# email.send_keys("teste@teste.com")
email = driver.find_element_by_id('txt_email').send_keys("teste@teste.com")
email.submit()

# preenche o campo Email
# emailConfirm = driver.find_element_by_id("confirm_txt_email")
# emailConfirm.send_keys("teste@teste.com")
emailConfirm = driver.find_element_by_id('confirm_txt_email').send_keys("teste@teste.com")
emailConfirm.submit()

# preenche o campo Usuário
user = driver.find_element_by_id("txt_usuario")
user.send_keys('jecisumer1@zain.site')
user.submit()






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
