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

    # player bio
    spans = soup.find_all('span', {'class' : 'bday'})
    bd = "no date"
    if len(spans) > 0:
        bd = spans[0].text
    
    spans = soup.find_all('span', {'class' : 'fn'})
    fn = "no name"
    if len(spans) > 1:
        fn = spans[1].text
    
    spans = [a.text for a in soup.select('th:-soup-contains("Batting") + td')]
    batting = "no batting"
    if len(spans) > 0:
        batting = spans[0]
    
    spans = [a.text for a in soup.select('th:-soup-contains("Bowling") + td')]
    bowling = "no bowling"
    if len(spans) > 0:
        bowling = spans[0]


    # player description
    pTags = soup.find_all('p')
    des = ''
    if pTags[0].text.strip() == '':
        des = pTags[1].text.strip()
    else:
        des = pTags[0].text.strip()


    # stats
    tables = soup.find_all('table')    
    test_data = []

    rows = tables[1].find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        
        if len(cells) > 1:
            stats = cells[0]
            
            test_data.append(stats.text.strip())
    player['name'] = fn
    player['born'] = bd
    player['batting'] = batting
    player['bowling'] = bowling
    player['description'] = des
    player['career'] = ""
    if len(test_data) >= 11:
        player['stats'] = {'test': {'matches': test_data[0], 'runs': test_data[1], 'wickets': test_data[6],'top_score': test_data[4],'best_bowling':test_data[10]}}
    else:
        player['stats'] = 'no_stats'

    output[names[i]] = player

out_file = open("test_all_1.json", "w")
json_data = json.dump(output, out_file, indent = 4)