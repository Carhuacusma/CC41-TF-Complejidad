#!/usr/bin/env python
# coding: utf-8

# In[50]:


class Paralelepipedo:
    def __init__(self,largo, ancho, alto, Myid):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.Myid = Myid
    
    def display(self):
        print(self.Myid,self.largo,self.ancho,self.alto)

#caja = Paralelepipedo(0,1,2)  
#print(caja.largo,caja.ancho,caja.alto)


contenedor_Largo = 0
contenedor_Ancho = 0
contenedor_Alto  = 0
MyRec = []
nPLLPPD = 0
archivo = open("Entrada.txt","r")
n = archivo.readlines()
cont = 0


for i in n:
    contenedor = i
    if cont == 0:
        contenedor_Largo = contenedor[0]

        contenedor_Alto  = contenedor[4]
    elif cont == 1:
        nPLLPPD = contenedor[0]
    else:
        MyRec.append([Paralelepipedo(contenedor[4],contenedor[6],contenedor[8],contenedor[2]+str(0))])
        q = int(contenedor[0])
        if q > 1:
            for x in range(q-1):
                MyRec[cont-2].append(Paralelepipedo(contenedor[4],contenedor[6],contenedor[8],contenedor[2]+str(x+1)))
    
    cont +=1

for x in range(len(MyRec)):
    for i in range(len(MyRec[x])):
        MyRec[x][i].display()


# In[ ]:




