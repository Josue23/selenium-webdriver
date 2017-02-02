from selenium import webdriver
from selenium.webdriver.common.keys import Keys
baseurl="https://www.semhora.com.br"
driver = webdriver.Firefox()
driver.get(baseurl)

# eventos = driver.find_element_by_css_selector(".eventbox")
# print(eventos)

all_options = driver.find_element_by_class_name("relacionadosContent")
    cell = row.find_elements_by_css_selector("eventBox")
    # print(type(cell))
    print(cell)
    # print(row.text)
    # print(cell.text)

# for evento in eventos:
#     link_name = driver.find_element_by_css_selector(".eventBox")
#     link_name.text
#     print (link_name.get_attribute('textContent'))

driver.close()














# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# baseurl="https://www.semhora.com.br"
# driver = webdriver.Firefox()
# driver.get(baseurl)
# link_name = driver.find_element_by_css_selector(".eventBox")
# link_name.text
# print (link_name.get_attribute('textContent'))
# driver.close()



