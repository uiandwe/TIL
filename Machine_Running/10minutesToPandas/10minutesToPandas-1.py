#!/usr/bin/env python
# coding: utf-8

# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# 
# https://dataitgirls2.github.io/10minutes2pandas/
# 
# https://www.youtube.com/watch?v=lspu830SzC8
# 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


s = pd.Series([1, 3, 4, np.nan, 6, 8])


# In[4]:


s


# In[5]:


dates = pd.date_range('20130101', periods=6)
dates


# In[6]:


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df


# In[8]:


df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })
df2


# In[9]:


df2.dtypes


# In[10]:


df = pd.DataFrame({"a": [4, 5, 6],
                  "b": [7, 8, 9],
                  "c": [10, 11, 12]},
                 index = [1, 2, 3])
df


# In[12]:


df = pd.DataFrame(
[[4, 7, 10],
[5, 8, 11],
[6, 9, 12]],
index=[1, 2, 3],
columns=['a', 'b', 'c'])
df


# In[17]:


df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]}, 
    index = pd.MultiIndex.from_tuples(
[('d',1),('d',2),('e',2)],
names=['n','v']))
df


# In[21]:


df[df.a < 7]


# In[23]:


df[df.b > 7]


# In[26]:


df.head(2)


# In[27]:


df.tail(2)


# In[28]:


df["b"] != 7


# In[36]:


df.a.isin([4])


# In[37]:


df = pd.DataFrame({'a': [1, 10, 8, 11, -1],
               'b': list('abcde'),
               'c': [1.0, 2.0, np.nan, 3.0, 4.0]})


# In[38]:


df


# In[39]:


df.nlargest(1, 'a')


# In[42]:


df.nlargest(2, 'c')


# In[43]:


df.nsmallest(2, 'a')


# In[45]:


import seaborn as sns


# In[ ]:


df = sns.load_dataset('iris')

