
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup
import urllib
import urllib.request
import urlopen
import scrapy
import requests
import parser
import json
import csv
import time

import plotly.plotly as py
from plotly import tools
import plotly.offline as pyo
import plotly.graph_objs as go


# In[4]:


with open(r'urls-isolated.csv') as csv_file:
    lines = csv_file.read().splitlines()


# In[5]:


data = []
for url in lines:
    try:
        page_response = requests.get(url, timeout=5)
        soup = BeautifulSoup(page_response.content, "lxml") 
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:title":
                print (tag.get("content", None))
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:description":
                print (tag.get("content", None))
        data.append(tag)
        print(data)
    except:
        InvalidSchema
        ConnectionRefusedError
        MaxRetryError
        ConnectionError
        NewConnectError
        NameError
        pass
    print("mess")
    for item in data:
        print(item, '\n')
    print(data)
    print("-----------------------------------, ", + len(data))
sleep(5)
with open(r'C:\Users\john.mendez\Desktop\output_data.csv', 'w') as f:
    writer = csv.writer(f, delimiter-'\n')
    writer.writerows(data)


# In[9]:


# Cleaning Tasks
df2 = pd.read_csv(r'urls.csv')

# Rounding engagement rate to two decimal points
df2['engagementRate'] = df2['engagementRate']= df2['engagementRate'].round(2)

# Getting Descriptive Statistics
df2.describe()

# Visualization Data
# Loading the data into pandas
df2.head(1)

# Add traces
trace = []
engage = go.Bar(
    x = df2['engagements'],
    y = df2['engagementRate'],
    name = 'Engagements',
    text = ['Comparison of Engagement to Engagment Rate'],
    marker = dict(
        color='lightblue',
        opacity=0.6
    )
)
unique = go.Bar(
    x = df2['uniqueActors'],
    y = df2['uniqueViewers'],
    name = 'Unique Characters',
    text = ['Comparison of Unique Actors to Unique Viewers'],
    marker = dict(
        color='orange',
        opacity=0.6
    )
)
impress = go.Bar(
    x = df2['impressions'],
    y = df2['engagementRate'],
    name = 'Impressions',
    text = ['Comparison of Impressions to Engagements'],
    marker = dict(
        color='plum',
        opacity=0.6
    )
)

#Append to Subplots

fig = tools.make_subplots(rows=3, cols=3, specs=[[{'colspan': 2, 'rowspan' : 3}, None, {'colspan' : 1, 'rowspan' : 1}],

                                                [None, None, {'colspan' : 1, 'rowspan' : 1}],

                                                [None, None, {'colspan' : 1, 'rowspan' : 1}]],

                          

                          subplot_titles=('Word Cloud: Data', 'Engagements to Engagement Rate', 'Unique Actors and Viewers', 'Impressions to Engagements Rate'))

fig.append_trace(engage, 1, 3)
fig.append_trace(unique, 2, 3)
fig.append_trace(impress, 3, 3)

fig['layout'].update(title="Audience Integration and Measurement")

pyo.offline.iplot(fig, filename='Audience Integration and Measurement.html')

