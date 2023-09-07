# Import the beautifulsoup
# and request libraries of python.
import requests
import time
from collections import Counter
from nltk.util import ngrams 
import bs4
from collections import Counter
import csv
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from googlesearch import search

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only

import requests

chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
with open('serp_cat_door_enclosures.csv', 'w',newline='' , encoding="utf-8") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(["TERM","SV","COUNT","RESULT"])

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
import pandas as pd
url = 'batch_cats/unique_tags_cats/unique_tags_cat_door_enclosures.csv'
df1 = pd.read_csv(url ,encoding="utf-8" ,engine="python", error_bad_lines=False)
df1 =df1

# Dataset is now stored in a Pandas Dataframe
for TERM,SV,COUNT in zip(df1['Keyword'],df1['Avg. monthly searches'],df1['Count']):
    TERM =str(TERM)
    text= f"What is a {TERM}"
    url = 'https://google.com/search?q=' + TERM
    query = TERM
    links = []
    
        
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
    MAX_RETRY = 100
    retries = 0
    
    num = 0
    
    try:
       for j in search(query, num=10, stop=10, pause=3):
        num += 1
        if num < 4:
            links.append(j)

       
    except Exception as exception:
         if retries <= MAX_RETRY:
             print("ERROR=Method failed. Retrying ... #%s", retries)
             time.sleep(1)
             continue
            
         else:
           raise Exception(exception)
    
    
        
    with open('serp_cat_door_enclosures.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([TERM, SV, COUNT, links])