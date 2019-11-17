#!/usr/bin/env python
# coding: utf-8

# In[20]:


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
            # caja = [idNum, (pos), rot]
            # aux waste = [(max x, " y, " z), ruta]
            idCaja, pos, rot = caja
            sizeCaja = sizeRotacion(idCaja, rot)
            maxSize, ruta = auxWaste
            f = open(ruta, "r+")
            auxString = f.readlines()
            for linea in auxString:
                # id pos.x pos.y pos.z size.x size.y size.z rot
                cajaF = linea.split(' ')
                _, lPx, lPy, lPz, lSx, lSy, lSz = caja
                posCajaF = int(lPx), int(lPy), int(lPz)
                sizeCajaF = int(lSx), int(lSy), int(lSz)
                if pos[0] + sizeCaja[0] <= posCajaF[0] + sizeCajaF[0] and pos[1] + sizeCaja[1] <= posCajaF[1] + sizeCajaF[1] and pos[2] + sizeCaja[2] <= posCaja[2] + sizeCajaF[2]:
                    f.close()
                    return False
                elif pos[0] + sizeCaja[0] > contenedor[0] or pos[1] + sizeCaja[1] > contenedor[1] or pos[2] + sizeCaja[2] > contenedor[2]:
                    f.close()
                    return False
            f.close()
            return True
        
        def aux(i,j): # caja i, en la orientacion j
            # el objetivo es que busque ordenar la nueva caja
            # en la opcion donde el desperdicio es mayor
            # waste[i][j] = [(Max x, Max y, Max z), ruta para leer ]
            # -> texto en formato
            # ------> [(id, pos), (id, pos), ...]
            # tamaño de la caja porque siempre es importante :) 
            sizeCaja = sizeRotacion(arr[i], j)
            if len(waste[i][j]) == 2:
                # ya se calculó, no hay pedo
                return True
            if waste[i][j] == None:
                #si no existe ruta = primera vez que se utiliza esta pila
                #entra: ? / funcion válida si tiene la ruta :( )
                strRuta = "aux" + str(i) + "rot" + str(j) + ".txt"
                # ejem: aux1rot0.txt
                waste[i][j] = [aux(i,j)]
                # se asume que no existe caja de mayores dimensiones que el contenedor
                # si no existe pila, es porque no se ha acomodado nada en ese caso hipotético ----------- BUT HAS IT????!!!!!
                waste[i][j] = [(contenedor[0] - sizeCaja[0], contenedor[1] - sizeCaja[1], contenedor[2] - sizeCaja[2]), strRuta]
                #pila:   idNum, (pos),  rot
                pila = [arr[i], (0,0,0), j]
                agregarFile(strRuta, pila)
            elif waste[i-1][j] != None:
                # ya hay una pila de cajas ordenadas en el caso hipotético hasta la caja anterior a la que
                # se quiere agregar
                maxSpace, strRuta = waste[i-1][j]
                pos = (0,0,0)
                for k in range(3):
                    if maxSpace[i] > sizeCaja[i]:
                        #x, y o z es candidato
                        #posiciona a la caja en el limite de x, y o z
                        # de forma kinda vectores canónicos
                        for k1 in range(3):
                            if k1 == k:
                                pos[k] = contenedor[k] - maxSpace[k]
                            else:
                                pos[k1] = 0
                        #posiciona a la caja en el limite de x o y o z
                        if entra(caja,waste[i][j]):
                            waste[i][j][0][k] -= sizeCaja[k]
                            for k1 in range(3):
                                if k1 != k:
                                    if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                        waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                            # redefinir los nuevos waste de ser necesario
                            return True     #--------------------------------------revisar qué debería retornar aux(i,j) ------- LLAMARLO
                        if k == 0:
                            # si está en x, toca mover en y
                            pos[1] = contenedor[1] - maxSpace[1]
                            if entra(caja,waste[i][j]):
                                waste[i][j][0][k] = contenedor[k] - sizeCaja[k] - pos[k] 
                                waste[i][j][0][1] = contenedor[1] - sizeCaja[1] - pos[1]
                                return True


# In[ ]:


# PSEUDOCÓDIGO DE LO QUE DEBERÍA HACER AUX SI BACKTRACKING
# PERO ÑÑÑ
arr = [] # cajas en el contenedor
def backtracking(caja, rotacion):
    if backtracking(caja + 1, rotacion):
        
backtracking(0, 0)


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


# In[23]:


waste = [[None]*6 for _ in range(5)]
if waste[0][1] == None:
    print("help")
aux = []
print(len(aux))

