import urllib
import json
import numpy as np
from urlparse import urlparse
from bs4 import BeautifulSoup

def searchengine(examplesearch):
  encoded = urllib.quote(examplesearch)
  rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encoded).read()
  jsonData = json.loads(rawData)
  searchResults = jsonData['responseData']['results']
  links = np.empty([4, 1], dtype="S25")
  i = 0
  for er in searchResults:
    link = er['url']
    link1 = urlparse(link).netloc 
      links[i,0]=link1
           i = i + 1
      target = "No Match found" 
      if links[0,0] == links[1,0] or links[0,0] == links[2,0] or links[0,0] == links[3,0]:
         target = links[0,0] 
      if links[1,0] == links[2,0] or links[1,0] == links[3,0]:
         target = links[1,0] 
      if links[2,0] == links[3,0] :
         target = links[2,0] 
      return [target]

import numpy as np
import pandas as pd
import pylab as pl 
import os
os.chdir(r"C:\Users\Tavish\Desktop")
Transaction_details = pd.read_csv("Descriptions.csv")
Transaction_details["match"] = "blank"
Transaction_details

for i in range(0,11):
  descr = Transaction_details['Descriptions'][i]
  Transaction_details["match"][i] = searchengine(descr)
Transaction_details