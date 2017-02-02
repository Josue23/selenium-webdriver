
# http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/

import urllib.request
from bs4 import BeautifulSoup 

import csv  
from datetime import datetime

# specify the url
quote_page = 'https://www.semhora.com.br' 

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser') 

# Take out the <div> of name and get its value
# name_box = soup.find('h1', attrs={'class': 'name'})
name_box = soup.find('h4', attrs={'class': 'relacionadosContent'})


# name = name_box.text.strip() # strip() is used to remove starting and trailing  
print(  name_box )

# get the index price
#
# price_box = soup.find('div', attrs={'class':'price'})  
# price = price_box.text  
# print (price)
