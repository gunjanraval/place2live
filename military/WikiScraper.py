#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:33:15 2019

@author: gunjanrawal
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_number_of_military_and_paramilitary_personnel').text
soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

ListTable = soup.find('table',{'class':'wikitable sortable'})
rows = ListTable.findAll('tr')

countryList = []
active_per_capita = []
total_per_capita = [] 

for i in rows[1:]:
    dataList = i.findAll('td')
    countryList.append(dataList[1].find('a').contents[0])
    active_per_capita.append(dataList[-1].contents[0])
    total_per_capita.append(dataList[-2].contents[0])
    #print(country,active_per_capita,total_per_capita)
    

df['Country'] = countryList
df['Per 1000 capita (active)'] = active_per_capita
df['Per 1000 capita (total)'] = total_per_capita


df.to_csv('CountryListOutput.csv',index=False)