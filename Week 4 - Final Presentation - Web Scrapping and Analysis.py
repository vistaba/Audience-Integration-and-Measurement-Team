
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup
import urllib.request
import requests
import json

import plotly
from plotly import tools
import plotly.plotly as py
import plotly.offline as pyo
import plotly.graph_objs as go


# In[3]:


url_list = pd.read_csv(r'urls.csv').astype(str)
url_list.head(1)


# In[4]:


url = list(url_list['URL'])


# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True
# 
# 
# def text_from_html(body):
#     soup = BeautifulSoup(body, 'html.parser')
#     texts = soup.findAll(text=True)
#     visible_texts = filter(tag_visible, texts)  
#     return u" ".join(t.strip() for t in visible_texts)
# 
# html = urllib.request.urlopen('https://blog.kinaxis.com/2018/10/unparalleled-customer-affinity-on-full-display-at-kinexions-18/').read()
# print(text_from_html(html))

# pages = []
# for i in range(1, 265):
#     url = requests.get('https://blog.kinaxis.com/2018/10/unparalleled-customer-affinity-on-full-display-at-kinexions-18/') +=
#     pages.append(url)

# In[5]:


# Looping through the http links.
count = 0
url_loop = []
for i in url:
    count += 1
    url_loop.append(i)


# Using Beautiful Soup in a loop.
df_list = []
folder = 'data_html'
for data_html in os.listdir(folder):
    with open(os.path.join(folder, data_html)) as file:
        page_link = 'url_loop'
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        soup = BeautifulSoup(file, 'lxml')
        title = page_content.find_all("h1")[i].text
        df_list.append({'title' : title})


# In[6]:


# Creating traces.



# Creating subplots.
fig = tools.make_subplots(rows=3, cols=3, specs=[[{'colspan': 2, 'rowspan' : 3}, None, {'colspan' : 1, 'rowspan' : 1}],
                                                [None, None, {'colspan' : 1, 'rowspan' : 1}],
                                                [None, None, {'colspan' : 1, 'rowspan' : 1}]],
                          
                          subplot_titles=('Word Cloud: Title Data', 'Unique Actors and Viewers (total)', 'Engagements and Impressions to Engagement Rate'))

# Adjusting the layout of the subplots.


# Appending the traces to the subplots

