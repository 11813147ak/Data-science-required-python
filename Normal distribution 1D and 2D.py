#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Generate a ND(1-D)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[16]:


u=2
sigma=3
vals=u+sigma*np.random.randn(1000)
plt.hist(vals)
plt.show()


# In[17]:


vals=np.round(vals)
z=np.unique(vals,return_counts=True)
print(z)


# In[ ]:





# In[ ]:





# In[24]:


u=5
sigma=5
vals=u+sigma*np.random.randn(100)
plt.hist(vals)
plt.show()


# In[25]:


x=vals
y=np.zeros(x.shape)
plt.scatter(x,y)
plt.show()


# In[ ]:





# In[ ]:


# Generate a ND (MULTI VARIATE)


# In[36]:


mean=np.array([0.0,0.0])
cov=np.array([[1,0.8],[0.8,1]])
mean2=np.array([5.0,6.0])
cov2=np.array([[1.3,0.2],[0.2,1.1]])
dist=np.random.multivariate_normal(mean,cov,500)
dist2=np.random.multivariate_normal(mean2,cov2,500)
print(dist.shape)
plt.scatter(dist[:,0],dist[:,1])
plt.scatter(dist2[:,0],dist2[:,1])
plt.show()


# In[ ]:


b

