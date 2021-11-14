import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

pause = 10
url = 'https://www.espncricinfo.com/player/team/sri-lanka-8/caps/test-1?page=5'

# driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
# driver.get(url)
# #This code will scroll down to the end
# while True:
#     try:
#         # Action scroll down
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         break
#     except: 
#         pass
# x = driver.find_element_by_tag_name("body")
# print(x)
html = urlopen(url) 
soup = BeautifulSoup(html, 'html.parser')
player_div = soup.find_all("div", {"class": "d-flex px-4 player-row"})
# print(divTag[0])
# tables = soup.find_all('a')
# print(tables)
x = player_div[0].find_all('a', href=True)
print(x[0]['href'])
urls = []
for x in player_div:
    a = x.find_all('a', href=True)
    print(a[0]['href'])
# for a in divTag[0].find_all('a', href=True):
#     print (a['href'])