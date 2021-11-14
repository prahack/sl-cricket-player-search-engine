import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import json

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

    spans = soup.find_all('span', {'class' : 'bday'})
    try:
        print(spans[0].text)
    except:
        print("no date")
    spans = soup.find_all('span', {'class' : 'fn'})
    try:
        print(spans[1].text)
    except:
        print("no name")
    awards = [a.text for a in soup.select('th:-soup-contains("Batting") + td')]
    try:
        print(awards[0])
    except:
        print("no batting")
    awards = [a.text for a in soup.select('th:-soup-contains("Bowling") + td')]
    try:
        print(awards[0])
    except:
        print("no bowling")