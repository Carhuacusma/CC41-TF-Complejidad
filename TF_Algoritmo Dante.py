#!/usr/bin/env python
# coding: utf-8

# In[3]:


# arreglo = [ ind,
#             ind ... ]
# indices = [ ['A', (size.x,size.y,size.z)], 
#             ['B', (size.x,size.y,size.z)], ...]
def kindaTetris(arreglo, indices, contenedor):
    n = len(arreglo)
    #        max med min
    # rot 1:  X   Y   Z
    # rot 2:  X   Z   Y
    # rot 3:  Y   X   Z
    # rot 4:  Y   Z   X
    # rot 5:  Z   X   Y
    # rot 6:  Z   Y   X
    def dentroContenedor(arr):
        nA = len(arr)
        waste = [[None]*6 for _ in range(nA)]
        # waste[rec i][orientacion] = menor desperdicio al guardar 
        #                             todas las cajas hasta la caja i
        #                             ( de arr )
        resp = []
        def aux(i,j): # caja i, en la orientacion j
            if i == 0:
                ind, size = indices[arr[i]]
                vol = size[0]*size[1]*size[2]
                for col in range(6):
                    waste[i][j] = (contenedor[0]*contenedor[1]*contenedor[2]) - vol


# In[ ]:




