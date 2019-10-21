#!/usr/bin/env python
# coding: utf-8

# In[5]:


def inputTeclado(arrIDs):
    arrAux = []
    strAux = input("Dimensiones del contenedor: ")
    arrAux = strAux.split(" ")
    sizeCont = 0
    if len(arrAux) == 3:
        x = int(arrAux[0])
        y = int(arrAux[1])
        z = int(arrAux[2])
        sizeCont = (x,y,z)
    else:
        sizeCont = (15,25,20) #default
    nCajasF = int(input("Cantidad de formatos de cajas: "))
    sizeCajaAux = 0
    arrCajas = []
    arrIDs = [0]*nCajasF
    for i in range(nCajasF):
        strAux = input("Cantidad - ID - Dimensiones: ")
        arrAux = strAux.split(" ")
        if len(arrAux) == 5:
            nCF = int(arrAux[0])
            idC = arrAux[1]
            x = int(arrAux[2])
            y = int(arrAux[3])
            z = int(arrAux[4])
            arrIDs[i] = [(idC),(x,y,z)]
            for j in range(nCF):
                arrCajas.append([0, idC, (0,0,0), 0])
    return arrCajas
ejemplo = []
inputTeclado(ejemplo)


# In[3]:


print("Asgore makes %d and %d some other shirt"%(5,7))


# In[ ]:




