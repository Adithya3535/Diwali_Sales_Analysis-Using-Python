#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'/Users/adithyachigiri/Documents/Data Analysis/Diwali Sales analysis project/Python_Diwali_Sales_Analysis/Diwali Sales Data.csv',encoding= 'unicode_escape')


# # The dataset contains information about customers, their demographics, and details about the products they purchased, & below is the full analysis of Data in accordence with the available Data

# In[3]:


df.shape


# In[4]:


df.head()


# In[48]:


df


# In[5]:


df.info()


# In[9]:


df.shape


# In[11]:


df.head()


# In[12]:


df.info()


# In[13]:


pd.isnull(df).sum()


# In[19]:


df.dropna(inplace=True)


# In[20]:


df.shape


# In[21]:


df['Amount'] = df['Amount'].astype('int')


# In[22]:


df['Amount'].dtypes


# In[23]:


df.columns


# In[24]:


#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})


# In[25]:


df.describe()


# In[26]:


df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# In[27]:


df.columns


# In[28]:


ax = sns.countplot(x = 'Gender',data = df)


# In[29]:


## plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[31]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# ## From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# In[ ]:


#Age


# In[32]:


df.columns


# In[33]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')


# In[34]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[35]:


ax = sns.countplot(data = df, x = 'Age Group')


# In[36]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# ## From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# In[ ]:


# State


# In[37]:


df.columns


# In[38]:


# total orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[39]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# ## From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# In[ ]:


# Marital Status


# In[40]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[41]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# ## From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# In[ ]:


# Occupation


# In[42]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[43]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# ## From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# In[ ]:


# Product Category


# In[44]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[45]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# ## From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[46]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[47]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:
# 

# # Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:





# In[ ]:




