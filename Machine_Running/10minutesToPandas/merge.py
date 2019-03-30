#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


adf = pd.DataFrame({"x1": ["A", "B", "C"], "x2": [1, 2, 3]})
adf


# In[7]:


bdf = pd.DataFrame({"x1": ["A", "B", "D"], "x3": ["T", "F", "T"]})
bdf


# In[8]:


pd.merge(adf, bdf, how='left', on='x1')


# In[9]:


pd.merge(bdf, adf, how='left', on='x1')


# In[10]:


pd.merge(adf, bdf, how='right', on='x1')


# In[11]:


pd.merge(adf, bdf, how='inner', on='x1')


# In[12]:


pd.merge(adf, bdf, how='outer', on='x1')


# In[14]:


adf.x1.isin(bdf.x1)


# In[15]:


adf[adf.x1.isin(bdf.x1)]


# In[16]:


~adf.x1.isin(bdf.x1)


# In[17]:


adf[~adf.x1.isin(bdf.x1)]


# In[ ]:




