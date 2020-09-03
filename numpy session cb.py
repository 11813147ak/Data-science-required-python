#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np
np.random.seed(1)


# In[68]:


np.random.randint(1,100,(5,5))


# In[69]:


x=np.array([1,2,4])


# In[70]:


x


# In[71]:


x.shape


# In[72]:


a=np.zeros((3,3))


# In[73]:


a


# In[74]:


b=np.ones((1,2))


# In[75]:


b


# In[76]:


np.full((3,2),5)


# In[77]:


x1=np.eye(4)


# In[78]:


x1


# In[79]:


x1[1,:]=5


# In[80]:


x1


# In[81]:


x=np.array([[1,2],[1,2]])
y=np.array([[1,2],[1,2]])


# In[82]:


np.add(x,y)


# In[83]:


np.subtract(x,y)


# In[84]:


np.divide(x,y)


# In[85]:


np.multiply(x,y)


# In[86]:


np.dot(x,y)


# In[87]:


xe=np.arange(10)+5


# In[88]:


np.random.shuffle(xe)
xe


# In[89]:


a=np.random.randn(2,3)


# In[90]:


a


# In[91]:


b=np.random.randint(5,10,2)


# In[92]:


b


# In[93]:


c=np.arange(66)+1
element=np.random.choice(c)
element


# In[ ]:





# In[97]:


a=np.array([[1,2,5,23,54,658],[65,67,657,7,87]])


# In[101]:


print(np.min(a,axis=0))


# In[104]:


print(np.max(a,axis=0))


# In[109]:


b=np.array([1,2,3,4,5,5,6,7,8,6,5,5,5,5])
m=sum(b)/5


# In[110]:


int(m)


# In[112]:


np.median(b)


# In[115]:


np.std(b)


# In[116]:


np.mean(b)


# In[117]:


np.average(b)


# In[118]:


np.var(b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




