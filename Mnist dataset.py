#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


read=pd.read_csv('C:/Users/HP/Desktop/train.csv')


# In[6]:


read.shape


# In[7]:


read.head()


# In[13]:


print(type(read))


# In[37]:


data=read.values
np.random.shuffle(data)


# In[17]:


print(type(data))


# In[18]:


data.shape


# In[19]:


X=data[:,1:]
Y=data[:,0]


# In[20]:


print(X.shape,Y.shape)


# In[21]:


print(X)


# In[23]:


print(Y)


# In[24]:


#to visualise one image


# In[25]:


X[0].shape


# In[40]:


def drawimg(X,Y,i):
    plt.imshow(X[i].reshape(28,28),cmap='gray')
    plt.title("Label "+str(Y[i]))
    plt.show()



for i in range(5):
    drawimg(X,Y,i)


# In[34]:


split=int(0.80*X.shape[0])
print(split)


# In[48]:


from sklearn.model_selection import train_test_split
XT,Xt,YT,Yt=train_test_split(X,Y,test_size=0.2,random_state=5)
print(XT.shape,YT.shape)
print(Xt.shape,Yt.shape)


# In[47]:


plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.imshow(XT[i].reshape(28,28))
    plt.title(YT[i])
    plt.axis("off")


# In[ ]:




