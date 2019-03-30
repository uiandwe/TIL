#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns


# In[3]:


df = sns.load_dataset("mpg")
df.head()


# In[4]:


df.groupby(by="origin").size()


# In[6]:


df["origin"].value_counts()


# In[9]:


pd.DataFrame(df.groupby(["model_year","origin"])["cylinders"].mean())


# In[10]:


df2 = pd.DataFrame(
[[4, 7, 10],
[5, 8, 11],
[6, 9, 12]],
index=[1, 2, 3],
columns=['a', 'b', 'c'])


# In[11]:


df2


# In[16]:


df2['b'].shift(1)


# In[17]:


df2['b'].shift(2)


# In[18]:


df2['b'].shift(3)


# In[19]:


df2.cummax()


# In[ ]:




