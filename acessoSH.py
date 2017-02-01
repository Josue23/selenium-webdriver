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
driver.get("http://semhora.com.br/cadastro")

# Apart from the public methods given above, there are two private methods which
# might be useful with locators in page objects.
from selenium.webdriver.common.by import By
# Sexo = driver.find_element(By.XPATH, '//button[text()="Masculino"]')
# Sexo.click()

# The next line is an assertion to confirm that title has “app” word in it:
assert "app" in driver.title



# =================================================
########## inicio do código de acesso ao site #####
# preenche o campo Usuário
name = driver.find_element_by_id("txt_login")
name.send_keys('josuerodrigues@gmail.com')
name.submit()

# preenche o campo Senha
name = driver.find_element_by_id("txt_senha")
name.send_keys('123456')
name.submit()
# o submit me leva para http://semhora.com.br/perfil
########## fim do código de acesso ao site #####
# =================================================

# clica no botão salvar salvar, em Informações Pessoais, à esquerda da página
    # salvarInfos = driver.find_element_by_id("btnSubmit")
    # salvarInfos.submit()
salvarInfos = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "btnSubmit")))
salvarInfos.submit()

# http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp
# estou  http://semhora.com.br/perfil
# clica no logo do SH no topo à esquerda que leva para a home do SH
salvarEndereco = salvarInfos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logoHeader")))
salvarEndereco = WebDriverWait(driver, 10)
salvarEndereco = salvarEndereco.until(EC.element_to_be_clickable((By.ID,'logoHeader')))
# salvarEndereco = driver.find_element_by_id("logoHeader")
salvarEndereco.click()

# WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
