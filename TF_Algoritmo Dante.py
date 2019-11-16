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
        #           = [(MAX espacio libre en X, " en Y, " en Z), [pila de rec (id, pos)]]
        waste[0][j] = [(contenedor[0], contenedor[1], contenedor[2])]
        dentro = []
        
        def sizesPorRotacion(idCaja, rot):
            og1, og2, og3 = indices[idCaja][1]
            sizeOG = [ og1, og2, og3]
            sizeOG.sort()
            #de menor a mayor en sizeOG
            #        max med min
            # rot 1:  X   Y   Z
            # rot 2:  X   Z   Y
            # rot 3:  Y   X   Z
            # rot 4:  Y   Z   X
            # rot 5:  Z   X   Y
            # rot 6:  Z   Y   X
            if rot == 1:
                return (sizeOG[2], sizeOG[1], sizeOG[0])
            elif rot == 2:
                return (sizeOG[2], sizeOG[0], sizeOG[1])
            elif rot == 3:
                return (sizeOG[1], sizeOG[2], sizeOG[0])
            elif rot == 4:
                return (sizeOG[0], sizeOG[2], sizeOG[1])
            elif rot == 5:
                return (sizeOG[1], sizeOG[0], sizeOG[2])
            elif rot == 6:
                return (sizeOG[0], sizeOG[1], sizeOG[2])
            
        def entra(caja, auxWaste):
            # caja = (id, pos, rot)
            idCaja, posX, posY, posZ, rot = caja
            for c in auxWaste:
                if pos[0] + size[0]
                # comparar pos + size si entra dentro del contenedor (arreglo dentro)
        def aux(i,j): # caja i, en la orientacion j
            # el objetivo es que busque ordenar la nueva caja
            # en la opcion donde el desperdicio es mayor
            # waste[i][j] = [(Max x, Max y, Max z), [(id, pos), (id, pos), ...] ]
            if waste[i][j] != None:
                return
            if i == 0:
                waste[i][j] = [(contenedor[0], contenedor[1], contenedor[2]),[]]
            else:
                ind, size = indices[arr[i]]


# In[8]:


ejemplo = [['A', (5,9,3)]]
print(ejemplo)
aux1, aux2, aux3 = ejemplo[0][1]
arr = [aux1,aux2,aux3]
arr.sort()
print(arr)

