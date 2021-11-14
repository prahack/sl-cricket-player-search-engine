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

    tables = soup.find_all('p')
    des = ''
    if tables[0].text.strip() == '':
        des = tables[1].text.strip()
    else:
        des = tables[0].text.strip()
    output[names[i]] = des

out_file = open("descrip.json", "w")
json_data = json.dump(output, out_file, indent = 4)