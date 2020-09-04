#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[10]:


x=np.array([[1,2,3,4,5,1,2,3,4]])


# In[11]:


x


# In[12]:


x.T


# In[14]:


x.reshape(3,3)


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt


# In[23]:


x=np.arange(10)
y=x**2


# In[24]:


plt.plot(x,y)


# In[44]:


plt.plot(x,y,label='graph')
plt.plot(y,x,label='kiwi')
plt.xlabel('graph')
plt.ylabel('kiwi')
plt.legend()


# In[27]:


plt.style.available


# In[32]:


plt.style.use('seaborn')


# In[40]:


get_ipython().run_line_magic('pinfo', 'plt.plot')


# In[42]:


#scatter


# In[49]:


plt.figure(figsize=(5,5))
plt.scatter(x,y,label='graph',marker='o')
plt.scatter(y,x,label='kiwi',marker='^')
plt.xlabel('graph')
plt.ylabel('kiwi')
plt.legend()


# In[50]:


#bar graph


# In[57]:


plt.bar(x,y,width=0.4)


# In[66]:


plt.figure(figsize=(7,5))
x_coordinates=np.array([0,1,2])*2
plt.bar(x_coordinates,[10,20,15],width=0.5,label='Current year',tick_label=['Gold','Platinum','Diamond'])
plt.bar(x_coordinates+0.5,[20,10,12],width=0.5,label='Next year')
plt.legend()
plt.show()


# In[68]:


plt.style.available


# In[71]:


plt.style.use('fivethirtyeight')
plt.figure(figsize=(7,5))
x_coordinates=np.array([0,1,2])*2
plt.bar(x_coordinates,[10,20,15],width=0.5,label='Current year',tick_label=['Gold','Platinum','Diamond'])
plt.bar(x_coordinates+0.5,[20,10,12],width=0.5,label='Next year')
plt.legend()
plt.show()


# In[73]:


#pie


# In[81]:


plt.pie(x,explode=None)
plt.show()


# In[98]:


subjects='Maths','english','hindi','sanskrit'
marks=[20,25,45,64]
plt.pie(marks,labels=subjects,explode=(0,0,0.1,0),shadow=True,counterclock=True,autopct='%1.1f%%')
plt.show()


# In[96]:


get_ipython().run_line_magic('pinfo', 'plt.pie')


# In[99]:


#histogram


# In[118]:


xsn=np.random.randn(100)
sigma=8
u=70
X=np.round(xsn*sigma+u)
X2=np.round(xsn*15+40)
print(X)


# In[112]:


print(xsn)


# In[120]:


plt.style.use('seaborn')
plt.hist(X,alpha=0.8,label='Physics')
plt.hist(X2,alpha=0.9,label="Maths")


# In[ ]:




