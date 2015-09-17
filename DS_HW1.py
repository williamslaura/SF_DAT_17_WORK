
# coding: utf-8

# In[11]:

import csv


# In[ ]:




# In[12]:

import requests
r = requests.get('https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-ticket-prices/2014-average-ticket-price.csv')
data = [row for row in csv.reader(r.iter_lines())]
data = data[1:97]

events = [row[0] for row in data]       # grab the first element of each row

prices = [int(row[2]) for row in data]  # cast to an int before storing the price


# In[14]:

import numpy as np


# In[15]:

#Step #3
print np.mean(prices)


# In[103]:

#Step #4, step # 5
away_teams=[]
home_teams = []
for e in events:
    #print e[1:3]
    temp_home = e.find('Tickets')
    temp_away = e.find(' at ')
    away_teams.append(e[0:temp_away])
    home_teams.append(e[temp_away+3:temp_home-1])


# In[100]:

print away_teams
print home_teams


# In[102]:

#step 7
Moneys_home = []
zipped = zip(home_teams,prices)
for e in zipped:
    if e[0] == ' Arizona Cardinals':
        Moneys_home.append(e[1])
Avg_home=np.mean(Moneys_home)
print Moneys_home
print Avg_home


# In[99]:

Moneys_away = []
zipped = zip(away_teams,prices)
for e in zipped:
    if e[0] == 'Arizona Cardinals':
        Moneys_away.append(e[1])
Avg_away=np.mean(Moneys_away)
print Moneys_away
print Avg_away


# In[ ]:




# In[89]:

print events


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[23]:

practice_string=['apple','orange','pear']
'apple'.find('pl')



# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



