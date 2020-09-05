#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


tips=sns.load_dataset('tips')


# In[5]:


tips


# In[6]:


tips.head()


# In[9]:


# for categorical data

sns.barplot(x='sex',y='total_bill',data=tips)


# In[16]:


sns.countplot(x='time',data=tips)


# In[17]:


sns.countplot(x='sex',data=tips)


# In[34]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker',split=True)


# In[28]:


sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')


# In[22]:


tips.columns


# In[24]:


sns.boxplot(x='day',y='total_bill',data=tips)


# In[26]:


sns.pointplot(x='day',y='total_bill',data=tips)


# In[30]:


sns.stripplot(x='day',y='total_bill',data=tips)


# In[31]:


sns.boxenplot(x='day',y='total_bill',data=tips)


# In[39]:


# distribution plot

#it is a univariate


# In[43]:


sns.distplot(tips['total_bill'],kde=False,bins=40)


# In[45]:


sns.kdeplot(tips['total_bill'])


# In[56]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[52]:


sns.distplot(tips['tip'],kde=False)


# In[57]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[65]:


sns.pairplot(tips,hue='sex')


# In[66]:


sns.pairplot(tips,hue='smoker')


# In[67]:


sns.pairplot(tips)


# In[69]:


tips_corr=tips.corr()


# In[70]:


tips_corr


# In[73]:


sns.heatmap(tips_corr,annot=True)
# only with non categorical variables


# In[ ]:





# In[76]:


flights=sns.load_dataset('flights')


# In[77]:


flights.head()


# In[82]:


x=flights.pivot_table(index='month',columns='year',values="passengers")


# In[83]:


sns.heatmap(x)


# In[ ]:





# In[ ]:





# In[ ]:




