'''
Created on Oct 16, 2020

This project will calculate how many cities in VA end with
the suffix "-burg" using the Pandas library as a web-scraper

@author: Mathew Carter
'''

import pandas

url = 'https://en.wikipedia.org/wiki/List_of_towns_in_Virginia'

#The table of cities is in the second DataFrame object
dataframe = pandas.read_html(url)[2]

#Gets the Series object with names of cities in Virginia
cities = dataframe.get('Name')

burg_cities = []

#Goes through the names of cities in Virginia and checking that they end in "-burg"
#and that there are no duplicates
for name in cities:
    if name.endswith('burg') and name not in burg_cities:
        burg_cities.append(name)

print('List of cities ending in "-burg" in Virginia: ')
for i in range(len(burg_cities)):
    if i != len(burg_cities) - 1:
        print(burg_cities[i], end = ', ')
    else:
        print(burg_cities[i], end = '.')

print('\n\nThere are', len(burg_cities), 'cities ending in "-burg" in Virginia')
