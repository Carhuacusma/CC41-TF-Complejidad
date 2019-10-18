#!/usr/bin/env python
# coding: utf-8

# In[2]:


#input

arrAux = []
strConte = input("Dimensiones del contenedor: ")
arrAux = strConte.split(" ")
sizeCont = 0
if len(arrAux) == 2:
    x = int(arrAux[0])
    y = int(arrAux[1])
    sizeCont = (x,y)
print(sizeCont)
# In[ ]:


print()

