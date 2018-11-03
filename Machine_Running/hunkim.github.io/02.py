#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
print(tf.__version__)


# In[4]:


hello = tf.constant("hello, tensorflow!")

sess = tf.Session()

print(sess.run(hello))


# In[7]:



node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1:", node1, "node2:", node2)
print("node3:", node3)


# In[9]:


sess = tf.Session()
print("sess.run(nod1, node2):", sess.run([node1, node2]))
print("sess.run(node3):", sess.run(node3))


# In[10]:



a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a+b

print(sess.run(adder_node, feed_dict={a:3, b:4.5}))
print(sess.run(adder_node, feed_dict={a:[1,3], b:[2,4]}))




# In[ ]:




