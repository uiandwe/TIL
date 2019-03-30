#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


df = sns.load_dataset("mpg")
df.shape


# In[3]:


df.head(5)


# In[6]:


df.sort_values("mpg").head(5)


# In[7]:


df.sort_values("mpg", ascending=False).head(5)


# In[10]:


df.rename(columns = {'model_year':'year'}).head()


# In[11]:


df.drop(columns=['name'])


# In[ ]:




