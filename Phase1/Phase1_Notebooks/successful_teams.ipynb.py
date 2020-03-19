#!/usr/bin/env python
# coding: utf-8

# In[2]:

# This code crawls basketball reference to retreive data about championship teams which we will later use to trends in successful teams

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


# URL to NBA championship teams by year 
year = 2019
url = "https://www.basketball-reference.com/playoffs/".format(year)
html = urlopen(url)
soup = BeautifulSoup(html)


# In[11]:


# findAll gets all columns
soup.findAll('tr', limit=3)
# finding all table headers
headers = [th.getText() for th in soup.findAll('tr', limit=3)[1].findAll('th')]
headers = headers[0:8]
headers


# In[9]:


#get data 
rows = soup.findAll('tr')[2:]
championship_teams = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]


# In[12]:


df = pd.DataFrame(championship_teams, columns = headers)
df.head(10)


# In[18]:


df.to_csv("successful_teams.csv", sep='\t')


# In[ ]:




