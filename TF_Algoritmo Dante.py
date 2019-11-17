#!/usr/bin/env python
# coding: utf-8

# In[3]:


# arreglo = [ ind,
#             ind ... ]
# indices = [ ['A', (size.x,size.y,size.z)], 
#             ['B', (size.x,size.y,size.z)], ...]
def agregarFile(ruta, arr):
    # arr formato:
    # [[id, (pos), rot],
    #  [id, (pos), rot], ...]
    # archivo:
    #  id pos.x pos.y pos.z size.x size.y size.z rot
    #  id pos.x ...
    f = open(ruta,"a+")
    for caja in arr:
        aux = str(caja[0]) + " " # id
        f.write(aux)
        posAux = caja[1]
        for i in range(3):
            aux = str(posAux[i]) + " "
            f.write(aux)
        aux = str(caja[2]) + "\n" # rot, salto de linea
        f.write(aux)
    f.close()

def kindaTetris(arreglo, indices, contenedor):
    n = len(arreglo)
    #        max med min
    # rot 0:  X   Y   Z
    # rot 1:  X   Z   Y
    # rot 2:  Y   X   Z
    # rot 3:  Y   Z   X
    # rot 4:  Z   X   Y
    # rot 5:  Z   Y   X
    def sizeRotacion(idCaja, rot):
            og1, og2, og3 = indices[idCaja][1]
            sizeOG = [ og1, og2, og3]
            sizeOG.sort()
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
    
    def dentroContenedor(arr):
        nA = len(arr)
        waste = [[None]*6 for _ in range(nA)]
        # waste[rec i][orientacion] = menor desperdicio al guardar 
        #                             todas las cajas hasta la caja i
        #                             ( de arr )
        #           = [(MAX espacio libre en X, " en Y, " en Z), "ruta" para archivo con pila de rectangulos]
        for j in range(nA):
            waste[0][j] = [(contenedor[0], contenedor[1], contenedor[2])]
            # inicializar para que sin cajas, el max es contenedor en sí
        dentro = []
        def entra(caja, auxWaste):
            # caja = [id, (pos), rot]
            # aux waste = [(max x, " y, " z), ruta]
            idCaja, pos, rot = caja
            sizeCaja = sizeRotacion(idCaja, rot)
            maxSize, ruta = auxWaste
            f = open(ruta, "a+")
            auxString = f.readlines()
            for linea in auxString:
                # id pos.x pos.y pos.z size.x size.y size.z rot
                cajaF = linea.split(' ')
                _, lPx, lPy, lPz, lSx, lSy, lSz = caja
                posCajaF = int(lPx), int(lPy), int(lPz)
                sizeCajaF = int(lSx), int(lSy), int(lSz)
                if pos[0] + sizeCaja[0] <= posCajaF[0] + sizeCajaF[0] and pos[1] + sizeCaja[1] <= posCajaF[1] + sizeCajaF[1] and pos[2] + sizeCaja[2] <= posCaja[2] + sizeCajaF[2]:
                    return False
                elif pos[0] + sizeCaja[0] > contenedor[0] or pos[1] + sizeCaja[1] > contenedor[1] or pos[2] + sizeCaja[2] > contenedor[2]:
                    return False
                else:
                    return True

        def aux(i,j): # caja i, en la orientacion j
            # el objetivo es que busque ordenar la nueva caja
            # en la opcion donde el desperdicio es mayor
            # waste[i][j] = [(Max x, Max y, Max z), ruta para leer ]
            # -> texto en formato
            # ------> [(id, pos), (id, pos), ...]
            if len(waste[i][j]) < 2:
                #si no existe ruta = primera vez que se utiliza esta pila
                #entra: ? / funcion válida si tiene la ruta :( )
                strRuta = "aux" + str(i) + "rot" + str(j)
                
                sizeCaja = sizeRotacion(i,j)
                waste[i][j] = [(contenedor[0] - sizeCaja, contenedor[1], contenedor[2])]
            else:
                ind, size = indices[arr[i]]
                


# In[4]:


def escribirFile(ruta, arr):
    f = open(ruta,"a+")
    for elem in arr:
        aux = str(elem)
        aux += " \n"
        f.write(aux)
    f.close()
ej = [5,4,3]
escribirFile("ejemplo.txt", ej)


# In[19]:


aux = [None]
aux = []
print(len(aux))

