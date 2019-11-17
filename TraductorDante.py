#!/usr/bin/env python
# coding: utf-8

# In[5]:


#--------------agregado como traductor a input de Dante .-. --------------------------
def TraductorDante(MyRec):
    ## myRec es como el arreglo de paralelepipedos definidos por
    arr = []
    uids = []
    # [ ['A', (size)], 
    #   ['B', (size)], ... ]
    unique = True
    contUids = -1
    for paralele in MyRec:
        for uid in uids:
            if paralele.Myid == uid[0]:
                unique = False
                break
        if unique:
            uids.append([paralele.Myid, (paralele.largo, paralele.ancho, paralele.alto)])
            contUids += 1
        arr.append(contUids)
    return arr, uids
        
inputTeclado()

