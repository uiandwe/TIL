#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[3]:


df = sns.load_dataset("iris")
df.head()


# In[5]:


df[['sepal_width','sepal_length','species']]


# In[6]:


df['sepal_width']


# In[10]:


df.filter(regex='width')


# In[17]:


df.loc[2:5, ['sepal_length', 'petal_width']]


# In[21]:


df.iloc[2:5, [1, 2, 4]]


# In[ ]:




