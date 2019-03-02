#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pathlib 


# In[2]:


import pandas as pd
import tensorflow as tf


# In[3]:


from pandas.api.types import CategoricalDtype
import numpy as np


# In[4]:


from plotnine import *


# In[5]:


get_ipython().run_line_magic('ls', '')


# In[6]:


petitions = pd.read_csv("petition.csv", index_col=0, parse_dates=['start', 'end'])


# In[7]:


petitions.shape


# In[8]:


petitions.head(3)


# In[9]:


petitions.tail(3)


# In[10]:


petitions.columns


# In[11]:


petitions.info()


# In[12]:


petitions.isnull().sum()


# In[13]:


petitions['answer'] = (petitions['votes'] > 200000) == 1
petitions.shape


# In[14]:


petitions.head()


# In[15]:


petitions['duration'] = petitions['end'] - petitions['start']
petitions.sort_values('duration', ascending=True).head(3)


# In[16]:


petitions['duration'].value_counts()


# In[17]:


petitions_60_answer = petitions.loc[(petitions['duration'] == '60 days') & (petitions['answer'] == 1)]
print(petitions_60_answer.shape)
petitions_60_answer.head()


# In[18]:


petitions_30_answer = petitions.loc[(petitions['duration'] == '30 days')                                     & (petitions['answer'] == 1)]
print(petitions_30_answer.shape)
petitions_30_answer.head()


# In[19]:


petitions_7_answer = petitions.loc[(petitions['duration'] == '7 days')                                    & (petitions['answer'] == 1)]
print(petitions_7_answer.shape)
petitions_7 = petitions.loc[(petitions['duration'] == '7 days')]
print(petitions_7.shape)
petitions_7_count = petitions_7['start'].value_counts().reset_index()
petitions_7_count.columns = ['start', 'count']
petitions_7_count.sort_values('start', ascending=True)


# In[21]:


category = pd.DataFrame(petitions['category'].value_counts()).reset_index()
category.columns = ['category', 'counts']
category


# In[22]:


start_df = pd.DataFrame(petitions['start'].value_counts()).reset_index()
start_df.columns = ['start', 'counts']
start_df = start_df.sort_values('counts', ascending=False)
print('청원 집계: {}일'.format(start_df.shape[0]))
start_df.head()


# In[23]:


petitions_unique = pd.pivot_table(petitions, index=['category'], aggfunc=np.sum)
petitions_best = petitions_unique.sort_values(by='votes', ascending=False).reset_index()
petitions_best


# In[24]:


petitions_start = pd.pivot_table(petitions, index=['start'], aggfunc=np.sum)
votes_df = petitions_start.sort_values(by='votes', ascending=False)
votes_df.loc[petitions_start['votes'] > 350000]


# In[25]:


votes_df = votes_df.reset_index()
votes_df.head()


# In[26]:


hottest_day_df = start_df.merge(votes_df, on='start', how='left')
hottest_day_df.sort_values('votes', ascending=False)[:5]


# In[27]:


answer_df = petitions.loc[petitions['votes'] > 200000]
answer_df.shape[0]


# In[28]:


answer_df.head()


# In[30]:


answer_df.sort_values('votes', ascending=False).head(10)


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




