#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow import keras
import numpy as np


# In[2]:


x_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y_data = [
    [0],
    [1],
    [1],
    [0],
]


# In[3]:


x_data = np.array(x_data)
y_data = np.array(y_data)


# In[4]:


x_data.shape


# In[6]:


y_data.shape


# In[9]:


from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD

model = Sequential()
model.add(Dense(8, activation="sigmoid", input_shape=(2,)))
model.add(Dense(1, activation="sigmoid"))

optimizer = SGD(lr=0.1)
model.compile(optimizer=optimizer, loss="binary_crossentropy", 
             metrics=['accuracy'])
model.summary()


# In[14]:


model.fit(x_data, y_data, batch_size=4, epochs=5000)


# In[15]:


predict = model.predict(x_data)
np.round(predict)


# In[ ]:





# In[ ]:




