#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Importing the libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


#importing the database
data=pd.read_csv('image.csv')


# In[11]:


data.head()


# In[13]:


a=data.iloc[3,1:].values


# In[24]:


#reshaping the extracting data
a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[26]:


df_x=data.iloc[:,1:]
df_y = data.iloc[:,0]


# In[27]:


#creating test and train size of module
x_train,x_test,y_train,y_test= train_test_split(df_x,df_y,test_size=0.2, random_state=4)


# In[32]:


y_train.head()


# In[34]:


#calling the classifier
rf= RandomForestClassifier(n_estimators=100)


# In[35]:


#fit the model
rf.fit(x_train,y_train)


# In[36]:


pred=rf.predict(x_test)


# In[37]:


pred


# In[39]:


#checking prediction accuracy
s = y_test.values

#calculate number of correctly predict values
count=0
for i in range(len(pred)):
    if pred[i]==s[i]:
        count=count+1


# In[40]:


count


# In[41]:


# total alues for prediction given was
len(pred)


# In[42]:


#accuracy value
8080/8400


# In[ ]:




