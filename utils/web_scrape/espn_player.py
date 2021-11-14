import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import json
from googletrans import Translator
translator = Translator()
import sys


with open('D:\/1 E drive\Sem 7\DM & IR\IR\IR project\espn_data\id.json') as f:
    data = json.load(f)

player_list = list(data.values())
player_id_list = list(data.keys())
description_list = {}
for player in player_id_list[::-1]:
    print(player)
    s = ""
    try:
        url = "https://www.espncricinfo.com/sl/content/player/" + player + ".html"
        html = urlopen(url) 
        soup = BeautifulSoup(html, 'html.parser')

        player_div = soup.find_all("div", {"class": "more-content-gradient-content"})
        # print(player_div)

    
        for p in player_div[0].find_all('p'):
            # print(p.get_text())
            # o = translator.translate(p.get_text(),dest='si')
            # print(o.text)
            # s = s + str(o.text)
            s = s + str(p.get_text())
        description_list[data[player]] = s
    except:
        description_list[data[player]] = s
print(len(description_list))
# out_file = open("des-eng.json", "w", encoding='utf-8')
# json_data = json.dump(description_list, out_file, indent = 4, ensure_ascii=False)
out_file = open("des-eng.json", "w")
json_data = json.dump(description_list, out_file, indent = 4)