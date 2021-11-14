import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
url = 'https://en.wikipedia.org/wiki/Somachandra_de_Silva'
html = urlopen(url) 
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')
print(len(tables))
test_data = []

rows = tables[1].find_all('tr')

for row in rows:
    cells = row.find_all('td')
    
    if len(cells) > 1:
        country = cells[0]
        
        test_data.append(country.text.strip())
print(test_data)