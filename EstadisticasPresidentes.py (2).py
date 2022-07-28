#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importar la libreria pndas
import pandas as pd


# In[2]:


# Datos de los presidentes de Mexico del 2000 al 2022
vfq = ['Vicente Fox',2000-2006, 42 ,2.0]
fch = ['Felipe Calderon', 2006-2012, 51 , 1.8]
epn = ['Enrique Peña', 2012-2018, 38.1 , 2.4]
amlo = ['Andres Lopez', 2018-2024, 53.19, 4.0]

# lista con datos
lista_rrss = [vfq, fch, epn, amlo]

# crear dataframe a partir de listas
df_rrss=pd.DataFrame(lista_rrss, 
                     columns = ['Nombre', 'Duracion del Sexenio','Votos obtenidos por %','Crecimiento PIB en %'])
df_rrss


# In[3]:


# importar matplotlib
import matplotlib.pyplot as plt


# In[4]:


#Este apartado mostrara los datos de votos obtenidos de 2 maneras graficas 

#Grafica Lineal
plt.plot(df_rrss['Nombre'], df_rrss['Votos obtenidos por %'])
plt.show()


# In[30]:


#Grafica de Barras
plt.bar(df_rrss['Nombre'], df_rrss['Votos obtenidos por %'],
       color=['b', 'r', 'g', 'm'])
plt.show()


# In[32]:


#crecimiento del pib
plt.bar(df_rrss['Nombre'], df_rrss['Crecimiento PIB en %'],
       color=['b', 'r', 'g', 'm'])
plt.show()


# In[33]:


#Grafica Lineal
plt.plot(df_rrss['Nombre'], df_rrss['Crecimiento PIB en %'])
plt.show()


# In[10]:


import pandas as pd


# In[13]:


vfq = ['Vicente Fox',2000-2006, 1061 , 14646 , 13.80]
fch = ['Felipe Calderon', 2006-2012, 1151 , 23032 , 20]
epn = ['Enrique Peña', 2012-2018, 1253 , 20678 , 16.50]

# lista con datos
lista_rrss = [vfq, fch, epn]

# crear dataframe a partir de listas
df_rrss=pd.DataFrame(lista_rrss, 
                     columns = ['Nombre', 'Duracion del Sexenio','Poblacion 100M hab.','Pobreza Alim. 100M hab.', '% poblacion Pobreza Alim.'])
df_rrss


# In[14]:


import matplotlib.pyplot as plt


# In[15]:


plt.plot(df_rrss['Nombre'], df_rrss['Poblacion 100M hab.'])
plt.show()


# In[16]:


plt.plot(df_rrss['Nombre'], df_rrss['Pobreza Alim. 100M hab.'])
plt.show()


# In[17]:


plt.bar(df_rrss['Nombre'], df_rrss['% poblacion Pobreza Alim.'],
       color=['b', 'r', 'g'])
plt.show()


# In[ ]:




