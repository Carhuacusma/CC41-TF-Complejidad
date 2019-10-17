#!/usr/bin/env python
# coding: utf-8

# In[54]:


class Paralelepipedo:
    def __init__(self,largo, ancho, alto, Myid):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.Myid = Myid

caja = Paralelepipedo(0,1,2)  
print(caja.largo,caja.ancho,caja.alto)


# In[48]:


contenedor_Largo = 0
contenedor_Ancho = 0
contenedor_Alto  = 0
MisParalelepipedos = []
archivo = open("Pete.txt","r")
n = archivo.readlines()
cont = 0
for i in n:
    contenedor = i
    if cont == 0:
        print(contenedor)
        contenedor_Largo = contenedor[0]
        contenedor_Ancho = contenedor[2]
        contenedor_Alto  = contenedor[4]
    if cont == 1:
        n = contenedor[0]
        MisParalelepipedos = [None]*n
    else:
        for x in int(contenedor[0]):
            
    
    
    cont +=1
print(contenedor_Largo, contenedor_Ancho, contenedor_Alto)

