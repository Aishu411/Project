#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.read_csv("Online Retail Data Set.csv")


# In[3]:


tata=pd.read_csv("Online Retail Data Set.csv")


# In[4]:


tata.drop('Unnamed: 3',axis=1,inplace=True)


# In[5]:


tata.head()


# In[6]:


tata.isnull().sum()


#  Here we can see there are 133359 null customer id and description 592

# In[7]:


tata['Description'].mode()[0]


# **filling null values in description by mode**

# In[8]:


tata.Description= tata.Description.fillna(tata['Description'].mode()[0])


# In[9]:


tata.isnull().sum()


# In[10]:



purchases=tata.groupby('CustomerID')['InvoiceNo'].count()


# In[11]:


purchases


# In[12]:


df=tata.groupby('CustomerID')['InvoiceNo'].count()


# In[14]:


df1=tata['CustomerID']


# In[15]:


df1


# In[16]:


df


# In[20]:


cust_info=pd.read_csv('cust_info.csv')


# In[21]:


cust_info.head()


# **creating a new colum called customer type**

# In[28]:


cust_info['Customer_Type']=0

cust_info.loc[(cust_info['Purchases']<=100,'Customer_Type')]="look out buyer"

cust_info.loc[((cust_info['Purchases']<=500)&(cust_info['Purchases']>100),'Customer_Type')]="Occasional Customer"

cust_info.loc[((cust_info['Purchases']<=2000)&(cust_info['Purchases']>500),'Customer_Type')]="Potential to be best customer"

cust_info.loc[((cust_info['Purchases']<=4000)&(cust_info['Purchases']>2000),'Customer_Type')]="best customer"

cust_info.loc[((cust_info['Purchases']<=5500)&(cust_info['Purchases']>4000),'Customer_Type')]="loyal customer"

cust_info.loc[(cust_info['Purchases']>5500,'Customer_Type')]="big spenders"


# In[29]:


cust_info


# In[30]:


cust_info.to_excel(r'C:\Users\DELL\OneDrive\Desktop\data analysis material\resume projects\tata\cust_info.xlsx',index=False)

