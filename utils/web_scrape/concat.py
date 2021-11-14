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


with open('D:\/1 E drive\Sem 7\DM & IR\IR\IR project\car-eng.json') as f:
    career_data = json.load(f)

with open('D:\/1 E drive\Sem 7\DM & IR\IR\IR project\wiki_all_data.json') as f:
    wiki_all = json.load(f)

player_id_list = list(wiki_all.keys())

for player in player_id_list[::-1]:
    try:
        wiki_all[player]['career'] = career_data[player]
    except:
        wiki_all[player]['career'] = 'no career'

out_file = open("all_with_career.json", "w")
json_data = json.dump(wiki_all, out_file, indent = 4)