import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import json

url = 'https://en.wikipedia.org/wiki/List_of_Sri_Lanka_Test_cricketers'
html = urlopen(url) 
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')
names = []
urls = []

for table in tables:
    rows = table.find_all('tr')
    
    for row in rows:
        cells = row.find_all('td')
        
        
        if len(cells) > 1:
            country = cells[1]
            
            urls.append(country.find_all('a',href=True)[0]['href'])
            names.append(country.text.strip())

names.pop()
urls.pop()
print(names)
print(urls)
print(len(names))
print(len(urls))

output = {}

for i in range(len(names)):
    print(i)
    print(names[i])
    player = {}
    url = 'https://en.wikipedia.org/' + urls[i]
    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html.parser')

    tables = soup.find_all('table')
    # print(len(tables))
    test_data = []

    rows = tables[1].find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        
        if len(cells) > 1:
            country = cells[0]
            
            test_data.append(country.text.strip())
    player['name'] = names[i]
    player['born'] = ""
    player['batting'] = ""
    player['bowling'] = ""
    player['description'] = ""
    player['career'] = ""
    if len(test_data) >= 11:
        player['stats'] = {'test': {'matches': test_data[0], 'runs': test_data[1], 'wickets': test_data[6],'top_score': test_data[4],'best_bowling':test_data[10]}}
    else:
        player['stats'] = 'no_stats'

    output[names[i]] = player

out_file = open("test_1.json", "w")
json_data = json.dump(output, out_file, indent = 4)
 

# print(json_data)
