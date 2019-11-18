#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
# arreglo = [ ind,
#             ind ... ]
# indices = [ ['A', (size.x,size.y,size.z)], 
#             ['B', (size.x,size.y,size.z)], ...]
def kindaTetris(arreglo, indices, contenedor):
    n = len(arreglo)
    print("Se desean ordenar los rectangulos: ")
    print(arreglo)
    print("Cuyos tipos son: ")
    print(indices)
    print("En un contenedor de: ")
    print(contenedor)
    #        max med min
    # rot 0:  X   Y   Z
    # rot 1:  X   Z   Y
    # rot 2:  Y   X   Z
    # rot 3:  Y   Z   X
    # rot 4:  Z   X   Y
    # rot 5:  Z   Y   X
    def sizeRotacion(idCaja, rot):
        og1, og2, og3 = indices[idCaja][1]
        print(og1)
        sizeOG = [ og1, og2, og3]
        sizeOG.sort()
        if rot == 0:
            print("Rotacion ")
            print(rot)
            print(sizeOG)
            return (sizeOG[2], sizeOG[1], sizeOG[0])
        elif rot == 1:
            print("Rotacion ")
            print(rot)
            print(sizeOG)
            return (sizeOG[2], sizeOG[0], sizeOG[1])
        elif rot == 2:
            print("Rotacion ")
            print(rot)
            print(sizeOG)
            return (sizeOG[1], sizeOG[2], sizeOG[0])
        elif rot == 3:
            print("Rotacion ")
            print(rot)
            print(sizeOG)
            return (sizeOG[0], sizeOG[2], sizeOG[1])
        elif rot == 4:
            print("Rotacion ")
            print(rot)
            print(sizeOG)
            return (sizeOG[1], sizeOG[0], sizeOG[2])
        elif rot == 5:
            print("Rotacion ")
            print(rot)
            print(sizeOG)
            return (sizeOG[0], sizeOG[1], sizeOG[2])
        print("Se mandó una rotación inexistente... por defecto se retorna rot 5")
        return (sizeOG[0], sizeOG[1], sizeOG[2])
    # =============================== FILES ===============================================
    # arr formato:
    # [[id, (pos), rot],
    #  [id, (pos), rot], ...]
    # archivo:
    #  idNum pos.x pos.y pos.z size.x size.y size.z rot
    #  idNum pos.x ...
    def copiarFile(rutaOG, rutaN):
        print("... Copiar archivo")
        print(rutaOG)
        print(rutaN)
        fO = open(rutaOG,"r+")
        fN = open(rutaN,"w+")
        lineas = fO.readlines()
        for linea in lineas:
            print(linea)
            fN.write(linea)
        fO.close()
        fN.close()

    def agregarFile(ruta, arr):
        print("Agregando")
        print(arr)
        print("a " + ruta)
        f = open(ruta,"a+")
        for caja in arr:
            aux = str(caja[0]) + " " # id
            f.write(aux)
            posAux = caja[1]
            for i in range(3):
                aux = str(posAux[i]) + " "
                f.write(aux)
                #escrito: pos.x pos.y pos.z
            size = sizeRotacion(int(caja[0]), int(caja[2]))
            for dim in size:
                aux = str(dim) + " "
                f.write(aux)
                #guarda el tamaño
            aux = str(caja[2]) + "\n" # rot, salto de linea
            f.write(aux)
        f.close()
    # ================================ FILES ===============================================
    
    def dentroContenedor(arr, actCont):
        # ordenar el "arr" dentro del actCont 
        nA = len(arr)
        waste = [[[0]]*6 for _ in range(nA)]
        # waste[rec i][orientacion] = menor desperdicio al guardar 
        #                             todas las cajas hasta la caja i
        #                             ( de arr )
        #           = [(MAX espacio libre en X, " en Y, " en Z), "ruta" para archivo con pila de rectangulos]
        for j in range(nA):
            waste[0][j] = [(contenedor[0], contenedor[1], contenedor[2])]
            # inicializar para que sin cajas, el máximo es el contenedor en sí
        def entra(caja, auxWaste):
            # caja = [idNum, (pos), rot]
            # aux waste = [(max x, " y, " z), ruta]
            idCaja, pos, rot = caja
            sizeCaja = sizeRotacion(idCaja, rot)
            _, ruta = auxWaste # maxSize, ruta = auxWaste
            f = open(ruta, "r+")
            auxString = f.readlines()
            for linea in auxString:
                # id pos.x pos.y pos.z size.x size.y size.z rot
                cajaF = linea.split(' ')
                _, lPx, lPy, lPz, lSx, lSy, lSz = cajaF
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
        
        # aux retorna (False/True, waste[i][j])
        # ------------(¿Problema?,       tabla)
        def aux(i,j): # caja i, en la orientacion j
            # el objetivo es que busque ordenar la nueva caja
            # en la opcion donde el desperdicio es mayor
            # waste[i][j] = [(Max x, Max y, Max z), ruta para leer ]
            # -> texto en formato
            # ------> [(id, pos), (id, pos), ...]
            # tamaño de la caja porque siempre es importante :) 
            sizeCaja = sizeRotacion(arr[i], j)
            print(sizeCaja)
            strRuta = "aux" + str(i) + "rot" + str(j) + "cont" + str(actCont) + ".txt"
            # ejem: aux1rot0.txt
            if len(waste[i][j]) == 2:
                # ya se calculó, no hay pedo
                return True, waste[i][j]
            if i == 0:
                # se asume que no existe caja de mayores dimensiones que el contenedor
                # si no existe pila, es porque no se ha acomodado nada en ese caso hipotético (garantizado por i = 0)
                print(type(sizeCaja[1]))
                print(type(strRuta))
                waste[i][j] = [(contenedor[0] - sizeCaja[0], contenedor[1] - sizeCaja[1], contenedor[2] - sizeCaja[2]), strRuta]
                #pila:   idNum, (pos),  rot
                caja = [arr[i], (0,0,0), j]
                agregarFile(strRuta, [caja])
                return True, waste[i][j]
            # ---------- revisar si existe un arreglo acomodado de cajas hasta antes de la que queremos
            maxSpace = 0
            jAux = 0 # rotacion calculada para caja i - 1
            for k in range(6):
                #por cada una las rotaciones en las que pudo entrar la caja anterior
                if waste[i-1][j] != None and waste[i-1][j][0] != False:
                    # si ya hay una pila de cajas ordenadas en el caso hipotético hasta la caja anterior, usamos esa
                    maxSpace, _ = waste[i-1][j]
                    jAuxCalc = j
                    break
            if maxSpace == 0:
                # si no hay cálculos wich is weird but ok,
                bien = False
                while not fine and jAux < 7:
                    bien, _ = aux(i-1,jAux)
                    #si nunca entró al if != None -> jAux = 0
                    jAux += 1
                jAux -= 1
                if not fine:
                    waste[i-1][jAux] = [False]
                    return False, waste[i-1][jAux]
            maxSpace, strRutaPrevia = waste[i-1][jAux]
            
            pos = (0,0,0)
            waste[i][j] = [pos, strRuta]
            #INICIALIZAR WASTE[i][j] PORQUE DE AQUÍ NO SALE SIN RESPUESTA >:) 
            copiarFile(strRutaPrevia, strRuta)
            # poner en waste[i][j][1] los que ya están dentro
            for k in range(3):
                #Las dimensiones en las que podría entrar
                if maxSpace[k] > sizeCaja[k]:
                    #x, y o z (defined by k) es candidato
                    # posiciona a la caja en el limite de x, y o z
                    ## -- de forma kinda vectores canónicos
                    for k1 in range(3):
                        if k1 == k:
                            pos[k] = contenedor[k] - maxSpace[k]
                        else:
                            pos[k1] = 0
                    #posiciona a la caja en el limite de x o y o z
                    caja = [arr[i], pos, j]
                    if entra(caja,waste[i-1][jAux]):
                        waste[i][j][0][k] -= sizeCaja[k]
                        #Waste en k disminuye el tamaño de la nueva caja en k
                        for k1 in range(3):
                            #Redefenir los waste en las demás dimensiones
                            if k1 != k:
                                #no se hace en k porque ya se hizo antes
                                if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                    waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                        #si entra, agregarlo oficialmente a la pila
                        #formato de agregarFile :!
                        agregarFile(strRuta, [caja])
                        return True, waste[i][j]
                    if k == 0:
                        # si está en x, toca mover en y
                        pos[1] = contenedor[1] - maxSpace[1]
                        #posiciona a la caja en el limite de x o y o z
                        caja[1] = pos
                        if entra(caja,waste[i][j]):
                            #como siempre se hace con los límites... :'c ....................DEFECTO DEL ALGORITMO
                            #................................................................OPCION: fuerza bruta y
                            #................................................................un arreglo + calculo waste
                            #................................................................kinda Skylines
                            for k1 in range(3):
                                #Redefenir los waste en las demás dimensiones
                                if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                    waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                            #formato de agregarFile :!
                            agregarFile(strRuta, [caja])
                            return True, waste[i][j]
                        # no entró en la esquina max X, max Y... toca elevar
                        pos[2] = contenedor[2] - maxSpace[2]
                        #posiciona a la caja en el limite de x o y o z
                        caja[1] = pos
                        if entra(caja, waste[i][j]):
                            for k1 in range(3):
                                #Redefenir los waste en las demás dimensiones
                                if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                    waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                            agregarFile(strRuta, [caja])
                            return True, waste[i][j]
                    if k == 1:
                        #está en y, so toca mover el x
                        pos[0] = contenedor[0] - maxSpace[0]
                        caja[1] = pos
                        if entra(caja, waste[i][j]):
                            for k1 in range(3):
                                #Redefenir los waste en las demás dimensiones
                                if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                    waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                            agregarFile(strRuta, [caja])
                            return True, waste[i][j]
                        #no entró, toca elevar (snoop inu)
                        pos[2] = contenedor[2] - maxSpace[2]
                        caja[1] = pos
                        if entra(caja, waste[i][j]):
                            for k1 in range(3):
                                #Redefenir los waste en las demás dimensiones
                                if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                    waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                            agregarFile(strRuta, [caja])
                            return True, waste[i][j]
                    if k == 2:
                        #está en z, so... mover en x
                        pos[0] = contenedor[0] - maxSpace[0]
                        caja[1] = pos
                        if entra(caja, waste[i][j]):
                            for k1 in range(3):
                                #Redefenir los waste en las demás dimensiones
                                if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                    waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                            agregarFile(strRuta, [caja])
                            return True, waste[i][j]
                        #no entró, toca TELL ME Y !!!!!!!!!!1 (AIN'T NOTHING BUT A HEARTACHE!)
                        pos[1] = contenedor[1] - maxSpace[1]
                        caja[1] = pos
                        if entra(caja, waste[i][j]):
                            for k1 in range(3):
                                #Redefenir los waste en las demás dimensiones
                                if sizeCaja[k1] > contenedor[k1] - maxSpace[k1]:
                                    waste[i][j][0][k1] = contenedor[k1] - sizeCaja[k1] - pos[k1]
                            agregarFile(strRuta, [caja])
                            return True, waste[i][j]
                    #fin del if sobre candigatos
                #ultima posible instruccion para el for iria con esa tabulacion
            #pasaste por todo, nunca entró :'|
            waste[i][j] = [False]
            return False, waste[i][j]
        #over here - fin de def aux
        #estamos en la (sub)función dentroContenedor(arr, actCont):
        # que busca:                   ordenar el "arr" dentro del actCont
        # so... toca aplicar aux hasta que veamos que algo malo pasa
        # RECORDANDO:
        #  arr formato:
        #    [[id, (pos), rot],
        #     [id, (pos), rot], ...]
        nice = False
        dejados = []
        rutaFin = "Mistake.txt"
        #------- Moment of truth INSIDE CONTAINER ----------------------
        for i in range(nA):
            #por i desde 0 hasta nA(len de arr)
            for j in range(6):
                nice, ruta = aux(i,j)
                # colocar la caja num i en orientacion j 
                if nice:
                    #si entró, no busca cambiar de orientación, va a la siguiente caja
                    print(ruta)
                    rutaFin = ruta # guarda la última ruta que funciona
                    break
            if not nice:
                #si no entró, sáltalo
                dejados.append(arr[i])
                # NO VA PODER PORQUE EN AUX SE BUSCA AL AUX(i-1,j)
                continue
        # ------------------------------------------------------ CONTINGENCIA ----------------------------------------
        if rutaFin == "Mistake.txt":
            print("No encontró nada de nada... ")
            return False
        if actCont > 10:
            print("ERROR CRÍTICO!!!!!!!!!!!!! GARBAGE OVERFLOW")
            return False
        # ------------------------------------------------------ CONTINGENCIA ----------------------------------------
        rutaCont = "cajasContenedor" + str(actCont) + ".txt"
        fAux = open(rutaCont, "w+")
        fAux.close()
        copiarFile(rutaCont,rutaFin)
        #pasamos por cada que se deba borrar
        for i in range(nA):
            for j in range(6):
                # borrar archivos:
                if len(waste[i][j]) == 2:
                    os.remove(waste[i][j][1])
        return rutaCont, dejados
    arrRutas = [] #se va a guardar las rutas de los contenedores
    fiambre = arreglo # aun no se ha colocado nada, todos en fiambre :) 
    contFunc = 1
    while len(fiambre) > 0:
        auxRuta, fiambre = dentroContenedor(fiambre, contFunc)
        print(auxRuta)
        arrRutas.append(auxRuta)
        contFunc += 1
    # =========================================== PASAR A RESPUESTA OFICIAL ===========================================
    volDisp = contFunc * contenedor[0] * contenedor[1] * contenedor[2]
    volTA = 0
    for auxInd in arreglo:
        _, size = indices[auxInd]
        volTA += size[0]*size[1]*size[2]
    porcUsado = (volDisp - volTA)/volDisp
    porcUsado = (round(porcUsado, 2)) * 100
    #------------------------ Escribir en txt Respuesta
    rutaRes = "resultadoAlgoritmoDante.txt"
    fR = open(rutaRes,"w+")
    auxToWrite = "Contenedores usados: " + str(contFunc) + "\n" + "Volumen disponible: " + str(volDisp) + "m2 "
    auxToWrite += "(" + str(porcUsado) + "%) \n" + "Cajas a transportar: " + str(n)
    auxToWrite += "Contenedor   Formato   Coordenadas   Orientacion"   
    fR.write(auxToWrite)
    contFunc = 1
    for auxRuta in arrRutas:
        f = open(auxRuta,"r+")
        auxLineas = f.readlines()
        for linea in auxLineas:
            idNum, posX, posY, posZ, _, _, _, rot = linea.split(" ")
            auxToWrite = str(contFunc) + "            " + str(indices[idNum][0]) + "         " + "("
            auxToWrite += str(posX) + ";" + str(posY) + ";" + str(posZ) + ")" + "       " + str(rot)
            fR.write(auxToWrite)
        contFunc += 1
        # ya lo leyó, so... let's erase it
        os.remove(auxRuta)
    return
indicesEjem = [['A', (5,4,3)],['B', (2,2,3)]]
contenedorEj = [10,10,10]
arregloEjem = [0,0,1]
kindaTetris(arregloEjem, indicesEjem, contenedorEj)

