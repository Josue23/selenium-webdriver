#!/usr/bin/env python3
# -*- coding:utf-8  -*-

# http://www.kochi-coders.com/2014/03/10/lets-scrape-the-page-using-beautiful-soup-4/

# Importing Beautiful Soup 4
from bs4 import BeautifulSoup

# This is major difference between Beautiful Soup 3 and 4. In 3 it was just
from BeautifulSoup import BeautifulSoup

# Next we will import the request module for opening the Url
import urllib.request

# We now need to open the page at the above Url.
url="http://www.utexas.edu/world/univ/alpha/"
page = urllib.request.urlopen(url)

# Creating the Soup
soup = BeautifulSoup(page.read())

# Finding the pattern in the page
universities=soup.find_all('a',class_='institution')

# From the pattern we can see that all universities will be within <a> tag with
# css class institution. So we need to find all the <a> tags whose class
# is institution to find all the universities. We can use Beautiful Soup 4 find_all() method to accomplish this.

universities=soup.find_all('a',class_='institution')

# In the above code line, we used find_all method in Beautiful Soup 4 to
# find all the universities. We found all the <a> tags with class institution.
# In Beautiful Soup 4 we can use the keyword argument class_ to search based
# on the css classes. We can iterate over each university by using the code below

for university in universities:
    print(university['href']+","+university.string)

# In the above page each University name is stored as the string of the <a> tag
# and URL  are stored as the href property of the <a> tag. So in the above code,
# by using university.string we will get each university name and using
# university[‘href’] we will get the university URL.


