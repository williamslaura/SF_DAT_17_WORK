
# coding: utf-8

# In[38]:

import pandas as pd
import numpy as np
get_ipython().magic(u'matplotlib inline')


# In[3]:

cd /Users/lwilliams/Documents/SF_DAT_17_WORK


# #### LESS MORBID #### 

# In[8]:

majors = pd.read_csv('college-majors.csv')
majors.head()


# In[5]:

majors.columns


# In[6]:

# 1. Delete the columns (employed_full_time_year_round, major_code)
del majors['Employed_full_time_year_round']
del majors['Major_code']


# In[7]:

majors.columns


# In[8]:

# 2. Show the cout of missing values in each column
majors.isnull().sum()


# In[11]:

# 3. What are the top 10 highest paying majors?
majors.sort_index(by='P75th',inplace = True) 
majors.Major.tail(10)


# In[31]:

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
highest_paid=majors[['Major','P75th']].tail(10)
highest_paid.plot(kind='bar',title='Top 10 Paying Majors')
plt.xlabel('Major')
plt.ylabel('P75th')
# plt.xticks('A','B','C','D','E','F','G','H','I','J')
# Still working on hwo to name the bars 
plt.show()


# In[9]:

# 5. What is the average median salary for each major category?


# In[46]:

majors.groupby(['Major_category'])['Median'].agg([np.mean])


# In[22]:

# 7. Plot a histogram of the distribution of median salaries
import matplotlib.pyplot as plt
majors.Median.plot(kind='hist', label = 'Histogram of Medians')
# plt.ylable('Median Salary')
# plt.xlabel('Count')


# In[50]:

# 8. Plot a histogram of the distribution of median salaries by major category
get_ipython().magic(u'matplotlib inline')
majors['Median'].hist(by=majors['Major_category'])
#majors.groupby(['Major_category'])['Median'].values


# In[24]:

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?
lowest_ten = majors.sort_index(by='Unemployed').tail(10)
lowest_ten


# In[25]:

# What are the unemployment rates?
lowest_ten.Unemployment_rate


# In[ ]:

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?


# In[29]:

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

majors['sample_employment_rate'] = majors['Employed']/majors['Total']
majors.head(5)


# In[30]:

pwd


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



