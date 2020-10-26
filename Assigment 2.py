#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


# In[66]:


ruter = pd.read_csv('https://raw.githubusercontent.com/umaimehm/Intro_to_AI/master/assignment1/Ruter_data.csv', sep=';');


# In[67]:


ruter.head()


# In[68]:


ruter.Linjenavn.unique()


# In[69]:


linje31 = ruter[ruter.Linjenavn == '31']


# In[70]:


linje31 = linje31.drop(columns = ['TurId','Fylke','Område','Kommune','Holdeplass_Fra','Holdeplass_Til','Linjetype','Linjefylke','Linjeretning','Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra','Tidspunkt_Faktisk_Avgang_Holdeplass_Fra','Tidspunkt_Planlagt_Ankomst_Holdeplass_Fra','Tidspunkt_Planlagt_Avgang_Holdeplass_Fra','Kjøretøy_Kapasitet'])


# In[71]:


linje31.Dato = pd.to_datetime(linje31.Dato)


# In[72]:


linje31.head()


# In[73]:


linje31.Dato.dt.year.unique()


# In[74]:


linje31.Dato = linje31.Dato.dt.dayofyear


# In[75]:


linje31['Dag']=linje31.Dato


# In[76]:


linje31.drop(columns = ['Dato'])


# In[77]:


plt.scatter(linje31.Dag,linje31.Passasjerer_Ombord)


# In[78]:


thresold_min = linje31['Passasjerer_Ombord'] >= 0


# In[79]:


thresold_min


# In[80]:


nylinje = linje31[thresold_min]


# In[81]:


nylinje.Passasjerer_Ombord.unique()


# In[82]:


nylinje = nylinje.drop_duplicates()


# In[83]:


plt.scatter(nylinje.Dag,nylinje.Passasjerer_Ombord)


# In[84]:


thresold_max = nylinje['Passasjerer_Ombord'] <= 25


# In[89]:


nylinje.Passasjerer_Ombord.unique()


# In[92]:


nylinje.Passasjerer_Ombord = nylinje.Passasjerer_Ombord[thresold_max]


# In[93]:


plt.scatter(nylinje.Dag,nylinje.Passasjerer_Ombord)


# In[113]:


nylinje = nylinje.dropna()


# In[114]:


input = nylinje.drop(columns = ['Linjenavn','Passasjerer_Ombord','Dato'])
input.head()


# In[115]:


input_2 = nylinje.Passasjerer_Ombord
input_2.astype(int)


# In[116]:


regObj = linear_model.LinearRegression()
regObj.fit(input,input_2)


# In[118]:


plt.xlabel('Dag',fontsize=16)
plt.ylabel('Antall Passasjerer',fontsize=16)
plt.scatter(nylinje.Dag,nylinje.Passasjerer_Ombord,color='blue')
plt.plot(nylinje.Dag,regObj.predict(nylinje[['Dag']]),color='red')


# In[122]:


regObj.predict([[120]])


# Prediction på dag 120.
