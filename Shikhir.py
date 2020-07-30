#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import os


# In[3]:


os. getcwd()


# In[4]:


os.chdir("C:\\Users\\shikh\\Downloads")


# In[5]:


data = pd.read_csv('cfs_2012_pumf_csv.txt', sep=",")


# In[6]:


print(data.head())


# In[7]:


data.head()


# In[8]:


data.shape


# In[9]:


data.info()


# In[10]:


data.describe


# In[11]:


abcd =  data.isnull().sum()


# In[12]:


print(abcd)


# In[13]:


abc=data.agg(['nunique']).T


# In[14]:


print(abc)


# In[15]:


percentofunique=abc/4547661


# In[16]:


print(round(percentofunique,5))


# In[19]:


data.EXPORT_YN.value_counts()


# In[28]:


data.dtypes


# In[34]:


data['QUARTER']=  pd.get_dummies(data['QUARTER'])


# In[37]:


data.dtypes

