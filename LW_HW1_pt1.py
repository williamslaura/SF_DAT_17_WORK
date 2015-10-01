
# coding: utf-8

# In[4]:

import pandas as pd


# In[5]:

cd /Users/lwilliams/Documents/SF_DAT_17


# In[6]:

killings = pd.read_csv('hw/data/police-killings.csv')
killings.head()


# In[ ]:




# In[ ]:




# In[7]:

cd /Users/lwilliams/Documents/SF_DAT_17_WORK


# In[ ]:




# In[8]:

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race
killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'},inplace=True)
## question: how to I "inplace" this ? I can't seem to make this stick. 


# In[20]:

# 2. Show the count of missing values in each column
killings.isnull().sum()


# In[21]:

# 3. replace each null value in the dataframe with the string "Unknown"
killings.fillna('Unknown', inplace = True)


# In[25]:

# 4. How many killings were there so far in 2015?
# killings[killings.year==2015].count
#killings.shape
#killings.year.count
# ans = 466 
killings[killings.year == 2015].shape
# ans = 467 -1 = 466


# In[30]:

# 5. Of all killings, how many were male and how many female?
killings[killings.gender == 'Male'].shape
#killings[killings.gender == 'Male'].count
#killings[killings.gender == 'Male'].sum
# ans = 445


## OR  ## 
killings_male = killings.gender == 'Male'
killing_male_count = killings_male.value_counts()
killing_male_count


# In[77]:

killings[killings.gender == 'Female'].shape
# ans = 22


# In[89]:

# 6. How many killings were of unarmed people?
killings[killings.armed =='No'].shape
#ans = 102


# In[92]:

# 7. What percentage of all killings were unarmed?
unarmed=killings[killings.armed =='No']
unarmed_percent = (unarmed.armed.value_counts()/killings.armed.shape[0]) * 100
unarmed_percent
# ans = 21.84 


# In[95]:

# 8. What are the 5 states with the most killings?
killings.sort_index(by='state')
killings.state.value_counts()
# ans = CA at 74


# In[96]:

# 9. Show a value counts of deaths for each race
killings.sort_index(by='gender')
killings.gender.value_counts()


# In[114]:

# 10. Display a histogram of ages of all killings
get_ipython().magic(u'matplotlib inline')
sorted_age=killings.sort_index(by='age')
# sorted_age.age.value_counts()
sorted_age.age.plot(kind='hist', 
                        color='b', 
                        title='Histogram of ages of all killings')
# sorted_age.age.value_counts()
# sorted_age.plot(tpye='hist',color = 'b',title = 'Hist of ages of all killings')


# In[9]:

# 11. Show 6 histograms of ages by race
get_ipython().magic(u'matplotlib inline')
killings['age'].hist(by=killings['race'])
## not gonna lie, needed help on this one. 
# race_grouped=killings.groupby('race')
# race_grouped.head()


# In[14]:

Islander = killings[killings.race == 'Asian/Pacific Islander']
Black    = killings[killings.race == 'Black']
Hispanic = killings[killings.race == 'Hispanic/Latino']
NativeA  = killings[killings.race == 'Native American']
Unknown  = killings[killings.race == 'Unknown']
White    = killings[killings.race == 'White']

print Islander.age.mean()
print Black.age.mean()   
print Hispanic.age.mean()
print NativeA.age.mean()  
print Unknown.age.mean() 
print White.age.mean() 

# Asian/Pacific Islander = 40.8
# Black                  = 34.0444444444
# Hispanic/Latino        = 31.7164179104
# Native American        = 27.75
# Unknown                = 43.5333333333
# White                  = 40.4661016949


# In[33]:

import matplotlib.pyplot as plt
killings.month.value_counts().plot(kind = 'bar',title = 'Killings per Month')
plt.ylabel('Month')
plt.xlabel('Number of Killings')

