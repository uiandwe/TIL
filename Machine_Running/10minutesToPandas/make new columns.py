#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[13]:


df = pd.DataFrame({'A': range(1,11), 'B': np.random.randn(10)})
df.head(5)


# In[17]:


df.assign(ln_A=lambda x: np.log(x.A)).head()


# In[20]:


df["ln_A"] = np.log(df.A)
df


# In[23]:


pd.qcut(df.A, 3, labels=["good", "medium", "bad"])


# In[24]:


pd.qcut(df.B, 3, labels=["good", "medium", "bad"])


# In[ ]:





# In[ ]:




