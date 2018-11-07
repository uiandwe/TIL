#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist

(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()

print("%d" % X_train.shape[0])
print("%d" % X_test.shape[0])


# In[3]:


import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap='Greys')
plt.show()


# In[6]:


import sys

for x in X_train[0]:
    for i in  x:
        sys.stdout.write('%d  ' % i)
    sys.stdout.write('\n')


# In[7]:


from keras.utils import np_utils
import numpy
import tensorflow as tf

seed = 0
numpy.random.seed(seed)
tf.set_random_seed(seed)

X_train = X_train.reshape(X_train.shape[0], 784)
X_train = X_train.astype('float64')
X_train = X_train / 255

X_test = X_test.reshape(X_test.shape[0], 784).astype('float64') / 255

print("class : %d" %(Y_class_train[0]))

Y_train = np_utils.to_categorical(Y_class_train, 10)
Y_test = np_utils.to_categorical(Y_class_test, 10)

print(Y_train[0])


# In[ ]:




