'''
Created on Oct 16, 2020

This project will calculate how many cities in VA end with
the suffix -burg

@author: Mathew Carter
'''

import pandas

url = 'https://en.wikipedia.org/wiki/List_of_towns_in_Virginia'

#The table of cities is in the second DataFrame object
dataframe = pandas.read_html(url)[2]

#Gets the Series of names of cities in Virginia
cities = dataframe.get('Name')

burg_cities = []
for name in cities:
    if name.endswith('burg') and name not in burg_cities:
        burg_cities.append(name)

print('List of cities ending in "-burg" in Virginia: ')
for city in burg_cities:
    print(city, end = ', ')
print('\n\nThere are', len(burg_cities), 'cities ending in "-burg" in Virginia')





