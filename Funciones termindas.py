import random 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


class Paralelepipedo:
    def __init__(self,largo, ancho, alto, Myid):
        self.largo = largo
        self.ancho = ancho
        self.alto  = alto
        self.Myid = Myid
        self.Pos = (0,0,0)
        self.rotacion = 1
        self.Contenedor =  1
    
    def display(self):
        print(self.Myid,self.largo,self.ancho,self.alto)

#caja = Paralelepipedo(0,1,2)  
#print(caja.largo,caja.ancho,caja.alto)

MyRec = []
Puestos = []
nPLLPPD = []
cont = [0]
Contenedores = []#arreglo de arrglo de largo,ancho,alto,volumen
Respuestas = [] #no es la respuesta jsjs
cont = 0
Ulti = [0,0,0] # ultimas posiciones usadas x,y,z
def Ponido(ulti,cont):#basicamente algoritmo galvan // le pasas las ultimas coordenas de cada eje
    if len(MyRec) > cont[0]:
        #x
        if ulti[0] + MyRec[cont[0]].largo <= Contenedores[-1][0]:
            MyRec[cont[0]].Pos = (ulti[0] + MyRec[cont[0]].largo,ulti[1],ulti[2]) #ponido(x+Puesto[cont].largo,y,z,cont+1
            ulti[0] += MyRec[cont[0]].largo
        elif ulti[0] + MyRec[cont[0]].largo > Contenedores[-1][0]:
            ulti[0] = 0
            Ponido(ulti,cont)
        #y   
        elif ulti[1] + MyRec[cont].ancho <= Contenedores[-1][1]:
            MyRec[cont[0]].Pos  = (ulti[0],ulti[1] + MyRec[cont[0]].ancho,ulti[2])
            ulti[1] += MyRec[cont[0]].ancho
        elif ulti[1] + MyRec[cont[0]].ancho > Contenedores[-1][1]:
            ulti[1] = 0 
            Ponido(ulti,cont)
        #Z   
        elif ulti[2] + MyRec[cont].alto <= Contenedores[-1][2]:
            MyRec[cont[0]].Pos  = (ulti[0],ulti[1],ulti[2] + MyRec[cont[0]].alto)
            ulti[2] += MyRec[cont[0]].alto
        elif ulti[2] + MyRec[cont[0]].ancho > Contenedores[-1][2]:
            ulti[2] = 0
            Ponido(ulti,cont)
        else:
            ponido(x+Puesto[cont[0]].largo,y,z,cont+1)#cuidado con el cont+1 hmm


def leerTxD(cont):
    archivo = open("Entrada.txt","r")
    n = archivo.readlines() 
    for i in n:
        contenedor = i
        helpm = contenedor.split(" ")
        if cont == 0:
            la = int(helpm[0])
            an = int(helpm[1])
            al = int(helpm[2])
            
            volumen = la * an * al
            Contenedores.append([la,an, al, volumen])


        elif cont == 1:
            nPLLPPD.append(int(helpm[0]))
        else:
            MyRec.append([Paralelepipedo(int(helpm[2]),int(helpm[3]),int(helpm[4]),helpm[1]+str(0))])
            q = int(contenedor[0])
            if q > 1:
                for x in range(q-1):
                    MyRec[cont-2].append(Paralelepipedo(int(helpm[2]),int(helpm[3]),int(helpm[4]),helpm[1]+str(x+1)))
    
        cont +=1
    for i in range(len(MyRec)): ##se puede borrar despues
        for z in range(len(MyRec[i])):
            MyRec[i][z].Pos = (random.randint(0,1),random.randint(0,1),random.randint(0,1))


def Guardar():
    archivo = open("Archivo Salida", 'w+')
    n = len(MyRec) #Numero de cajas a transportar
    p = len(Contenedores) #Numero de contenedores usados
    vu = 0 #Volumen utilizado
    vd = Contenedores[0][3]*p #Volumen disponible
    
    for i in range(len(MyRec)):
        for x in range(len(MyRec[i])):
            vu += (MyRec[i][x].alto*MyRec[i][x].largo*MyRec[i][x].ancho)
        
    a = "Contenedores usados: " + str(p) + "\n" 
    b = "Volumen disponible: " + str(vd) + " m2 \n"
    c = "Volumen ocupado: " + str(vu)  + " m2 (" + str(vu*100/vd) + "%) \n"
    d = "Cajas a transportar: " + str(n) + "\n"
    
    archivo.write(a+b+c+d)
    archivo.write("Contenedor Formato Coordenadas Orientacion:\n")
    
    for i in range(n):
        for z in range(len(MyRec[i])):
            archivo.write("%d\t\t\t%s\t\t\t%d%d\t\t\t%d\n"%(MyRec[i][z].Contenedor,MyRec[i][z].Myid,MyRec[i][z].Pos[0],MyRec[i][z].Pos[1],MyRec[i][z].rotacion))
            
def GenerarArchivo():
    nombreArchivo = input("Ingrese el nombre del archivo: ")
    archivoGenerado = open(nombreArchivo, 'w+')
    n = random.randint(1,10) #Cantidad de cajas
    
    #Dimensiones del contenedor
    largo = random.randint(0,50)
    ancho = random.randint(0,50)
    alto = random.randint(0,50)
    
    #Convertir a string las variables para poder escribirlas en el archivo
    la = str(largo)
    an = str(ancho)
    al = str(alto)
    nn = str(n)
    
    archivoGenerado.write(la + " " + an + " "+ al + "\n")
    archivoGenerado.write(nn + "\n")
    
    #Generar las cajas 
    tipo = 65 #Tipo de la caja
    
    for i in range(n):        
        if i == 0:
            c = random.randint(1, n) #Cantidad de cajas del mismo tipo
        
        else: 
            if n - c > 0:
                g = n - c
                c = random.randint(1, g) #Cantidad de cajas del mismo tipo
            
            else:
                break
            
        x = random.randint(0,largo) #Largo de la caja
        y = random.randint(0, ancho) #Ancho de la caja
        z = random.randint(0, alto) #Alto de la caja
        
        #Convertir a string las variables para poder escribirlas en el archivo
        a = str(c)
        b = str(x)
        d = str(y)
        e = str(z)
        t = chr(tipo)
        
        tipo += 1
        archivoGenerado.write(a + " "+ t + " "+ b + " " + d + " " + e + "\n") 


def Display3D():
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection = '3d')
    
    xpos = []
    ypos = []
    zpos = []
    
    dx = []
    dy = []
    dz = []
    
    xCont = []
    yCont = []
    zCont = []
    
    dxCont = []
    dyCont = []
    dzCont = []
    
    for i in range(len(MyRec)):
        for y in range(len(MyRec[i])):
            xpos.append(MyRec[i][y].Pos[0])
            ypos.append(MyRec[i][y].Pos[1])
            zpos.append(MyRec[i][y].Pos[2])
            
            dx.append(MyRec[i][y].largo)
            dy.append(MyRec[i][y].ancho)
            dz.append(MyRec[i][y].alto)
            
    for i in range(len(Contenedores)):
        extra = Contenedores[i][0]*i
        #     0,0,0  x,0,0                      0,y,0             0,0,z                        x,y,0                      x,0,z                     0,y,z               x,y,z
        xCont += [0 ,Contenedores[i][0] + extra,0 +extra          ,0 + extra                  ,Contenedores[i][0] + extra,Contenedores[i][0] + extra,0 + extra         ,Contenedores[i][0]+extra,Contenedores[i][0] + extra,0                 ,0]  
        yCont += [0, 0                        ,Contenedores[i][1],0                          ,Contenedores[i][1]        ,0                         ,Contenedores[i][1],Contenedores[i][1]       ,0                         ,Contenedores[i][1],Contenedores[i][1]  ]
        zCont += [0, 0                        ,0                 ,Contenedores[i][2]         ,0                         ,Contenedores[i][2]        ,Contenedores[i][2],Contenedores[i][2]       ,0                         ,0                 ,Contenedores[i][2] ]
        
                 #0,0,0               x,0,0                 0,y,0                0,0,z                 x,y,0                x,0,z                0,y,z               x,y,z 
        dxCont += [0.1               ,(-Contenedores[i][0]),0.1                  ,(Contenedores[i][0]),0.1                 ,0.1                  ,0.1                 ,0.1    ,0.1               ,Contenedores[i][0],Contenedores[i][0]]
        dyCont += [0.0001,0.0001     ,(-Contenedores[i][1]),0.0001              ,0.0001              ,0.0001        ,(-Contenedores[i][1]),(-Contenedores[i][1]),Contenedores[i][1],0.0001            ,0.0001]
        dzCont += [Contenedores[i][2],0.1                  ,0.1                  ,0.1                 ,(Contenedores[i][2]),(-Contenedores[i][2]),0.1                 ,0.1    ,0.1               ,0.1               ,0.1]
                                      #Hasta este esta ok  ]
    
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color = '#00ceaa', alpha = '0.9')
    ax1.bar3d(xCont, yCont, zCont, dxCont, dyCont, dzCont, color = 'magenta', alpha = 0.5)

    plt.show()
    
    
def inputTeclado():
    largo = int(input("Ingrese el largo del contenedor: "))
    ancho = int(input("Ingrese el ancho del contenedor: "))
    alto  = int(input("Ingrese el alto  del contenedor: "))
    
    Contenedores.append(largo)
    Contenedores.append(ancho)
    Contenedores.append(alto) 
    
    n = int(input("Cantidad de cajas: "))
    cont  = 0 #Validar la cantidad de cajas
    
    
    for i in range(n):
        print("Ingrese las dimensiones de la caja: ")
        
        x = int(input("Ingrese el largo de la caja: "))
        y = int(input("Ingrese el ancho de la caja: "))
        z = int(input("Ingrese el alto de la caja: "))
        Mid = input("Ingrese el tipo de la caja: ")
        d = int(input("Cuantos tipos de la misma caja hay: "))
        
        for j in range(d):
            MyRec.append(Paralelepipedo(x, y, z, Mid)) 
            cont += 1
            if cont == n:
                break
        
        if cont == n:
                break    
    

 cn = []     #Cajas que no entran en el contenedor
cc = []     #Cajas que están en el contenedor

def BuscarEspacioDisponible(PlanoAB, dimensionA, dimensionB):
    d = 0 #Espacio disponible
    for i in range(dimensionB):
        for j in range(dimensionA):
            if PlanoAB[i][j] == 0:
                d += 1
    return d

def ColocarCaja(PlanoAB, dimensionA, dimensionB, limiteA, limiteB):
    e = 0
    d = 0
    for i in range(dimensionB):
        for j in range(dimensionA):
            if PlanoAB[i][j] == 0:
                e = i
                d = j
                break
    
    r = e 
    k = d
    for r in range(limiteA):
        for k in range(limiteB):
            PlanoAB[r][k] = 1

def EspacioUtilizado(PlanoAB, DimensionA, DimensionB):
    d = 0
    
    for i in range(DimensionB):
        for j in range(DimensionA):
            if PlanoAB[i][j] == 1:
                d += 1
    return d

def AlgoritmoNatalia(MyRec, cc, cn):
    Ancho = Contenedores[1]
    Largo = Contenedores[0]
    Alto = Contenedores[2]
    
    #Representación del contenedor y su espacio disponible
    PlanoXY = [[0] * Ancho for _ in range(Largo)]
    PlanoXZ = [[0] * Ancho for _ in range(Alto)]
    PlanoYZ = [[0] * Largo for _ in range(Alto)]
        
    #Variables:
    v = int(Ancho) * int(Alto) * int(Largo)     #volumen del contenedor
    vo = int(0)                                 #volumen ocupado del contenedor
    vd = int(v)                                 #volumen disponible del contenedor
    c = 1                                       #Cantidad de contenedores usados
    m = len(cc)                                 #Cantidad de cajas a transportar/encuentran en el contenedor
    dxy = 0                                     #Cantidad de espacio disponible en el plano xy
    dxz = 0                                     #Cantidad de espacio disponible en el plano xz
    dyz = 0                                     #Cantidad de espacio disponible en el plano yz
    vc = int(0)                                 #Volumen de la caja a evaluar
    avc = int(0)                                #Volumen de la caja del vector cn a evaluar
    
    
    print("Volumen del contenedor: ", v)
    #Colocar las cajas: Aquí no sé muy bien qué hacer todavia 
    for i in range(len(MyRec)):
        #Se ha puesto esto para ver qué se está multiplicando y que los valores sean los correctos
        print("Largo: ", MyRec[i].largo)
        print(type(MyRec[i].largo))
        
        print("Ancho: ", MyRec[i].ancho)
        print(type(MyRec[i].ancho))
        
        print("Alto: ", MyRec[i].alto)
        print(type(MyRec[i].alto))
        
        print("Volumen disponible: ", vd)

        vc = int(MyRec[i].largo * MyRec[i].alto * MyRec[i].ancho) #Volumen de la caja
        
        #Validar que se está realizando el cálculo:
        print("Volumen caja: ", vc)
        
        if vc <= vd:
            dxy = BuscarEspacioDisponible(PlanoXY, Ancho, Largo)
            dyz = BuscarEspacioDisponible(PlanoYZ, Largo, Alto)
            dxz = BuscarEspacioDisponible(PlanoXZ, Ancho, Alto)
            
            if MyRec[i].ancho <= dxy and MyRec[i].largo <= dyz and  MyRec[i].alto <= dxz:
                ColocarCaja(PlanoXY, Ancho, Largo, MyRec[i].ancho, MyRec[i].largo)
                ColocarCaja(PlanoYZ, Largo, Alto, MyRec[i].largo, MyRec[i].alto)
                ColocarCaja(PlanoXZ, Ancho, Largo, MyRec[i].ancho, MyRec[i].alto)
                cc.append(MyRec[i])
                vd -= vc
                print("Volumen disponible: ", vd)
        
        else:
            for j in range(len(cn)):
                avc = cn[j].ancho * cn[j].alto * cn[j].largo
                print("Volumen caja auxiliar: ", avc)
                if avc <= vd:
                    if cn[i].ancho <= dxy and cn[j].largo <= dyz and cn[i].alto <= dxz:
                        ColocarCaja(PlanoXY, Ancho, Largo, cn[i].ancho, cn[j].largo)
                        ColocarCaja(PlanoYZ, Largo, Alto, cn[i].largo, cn[j].largo)
                        ColocarCaja(PlanoXZ, Ancho, Alto, cn[i].ancho, cn[j].alto)
                        cc.append(cn[i])
                        del cn[i]
                        vd -= avc
                        print("Volumen disponible: ", vd)
                
                else:
                    print("no entró")
                    cn.append(MyRec[i])
        print("iteración #: ", i)
    
    #Forma 3 de obtener el vo
    print("V:", v)
    print("VD: ", vd)
    vo = v - vd
    
    
    print("El volumen utilizado es: ", vo)
    print("El volumen disponible es: ", vd)
    print("La cantidad de contenedores usados es: ", c)
    print("La cantidad de cajas a transportar son: ", m)
    print("Las cajas a transportar son: ", cc)
    
    return vo, c, vd, m   
    
    
    
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
        print("dentroContenedor() ordenando ")
        print(arr)
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
                if len(cajaF) != 7:
                    print("SOMETHINGS WROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONG")
                _, lPx, lPy, lPz, lSx, lSy, lSz,_ = cajaF
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
            print("Dentro de aux, para ingresar lo de arriba, que es: ")
            print(sizeCaja)
            strRuta = "aux" + str(i) + "rot" + str(j) + "cont" + str(actCont) + ".txt"
            # ejem: aux1rot0.txt
            if len(waste[i][j]) == 2:
                # ya se calculó, no hay pedo
                print("Ya estaba listo")
                return True, waste[i][j]
            if i == 0:
                print("Acomodando la primera caja")
                # se asume que no existe caja de mayores dimensiones que el contenedor
                # si no existe pila, es porque no se ha acomodado nada en ese caso hipotético (garantizado por i = 0)
                print("Garantía: ¿int y string? ")
                print(type(sizeCaja[1]))
                print(type(strRuta))
                waste[i][j] = [(contenedor[0] - sizeCaja[0], contenedor[1] - sizeCaja[1], contenedor[2] - sizeCaja[2]), strRuta]
                #pila:   idNum, (pos),  rot
                caja = [arr[i], (0,0,0), j]
                agregarFile(strRuta, [caja])
                print("En el caso hipotético caja " + str(i) + " en orientacion " + str(j) + " SE PUDO")
                return True, waste[i][j]
            # ---------- revisar si existe un arreglo acomodado de cajas hasta antes de la que queremos
            maxSpace = 0
            jAux = 0 # rotacion calculada para caja i - 1
            for k in range(6):
                print("Revisando si entró la caja anterior en rot " + str(k))
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
            
            pos = [0,0,0]
            #Python con todo lo que dice... NO SOPORTA ASIGNACIONES EN TRIPLETAS (N-etas)
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
                print("dentroContenedor() llama a aux. Ordenar la ")
                print(i)
                print("caja de su arr, con rotación: ")
                print(j)
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
    #Ejecución para KindaTetris ------------------------------------------------
    arrRutas = [] # va a guardar las rutas de los contenedores
    fiambre = arreglo # aun no se ha colocado nada, todos en fiambre :) 
    contFunc = 1
    while len(fiambre) > 0:
        print("En el contenedor")
        print(contFunc)
        print("KindaTetris va a llamar a dentroContenedor")
        auxRuta, fiambre = dentroContenedor(fiambre, contFunc)
        print("Regresó de dentroContenedor, nueva ruta: ")
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
    #------------------------ Escribir en txt Respuesta-------------------------------------------
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
    
def Menu():
    print("---------- EMPAQUETAMIENTO ----------")
    print("Seleccionar método de entrada:       ")
    print(" 1. Leer archivo                     ")
    print(" 2. Ingresar datos                   ")
    print(" 3. Generar archivo aleatorio        ")
    op = [0]
    while op[0] > 2 or op[0] < 1:
        op[0] = int(input())
    if op[0] == 1:
        # LLAMAR A FUNCION QUE LEE ARCHIVO
        print("Leer")
        leerTxD(cont)
        
    elif op[0] == 2:
        print("Teclado")
        intpurTeclado()
        # LLAMAR A FUNCION QUE LEE POR TECLADO
    elif op[0] == 3:
        print("archivo aleatorio: ")
        GenerarArchivo()
        # LLAMAR A FUNCION GENERAR ARCHIVO ALEATORIO
    def selecAlgo():
        print("Seleccionar algoritmo:               ")
        print(" 1. Método Maury                     ")
        print(" 2. Método Galván                    ")
        print(" 3. Metodo Carhuacusma               ")
        print(" 4. Salir                            ")
        op[0] = 0
        while op[0] < 1 or op[0] > 4:
            op[0] = int(input())
        # IMPRIMIR RESULTADOS SOBRE RECURSOS UTILIZADOS Y TIEMPO DEL ALGORITMO
        if op[0] == 1:
            print("Implementar Maury")
            AlgoritmoNatalia(MyRec, cc, cn)
            # LLAMAR AL ALGORITMO MAURY
        elif op[0] == 2:
            print("Implementar Galván")
            # LLAMAR AL ALGORITMO GALVÁN
        elif op[0] == 3:
            print("Implementar Moreno")
            # ACOMODAR PARÁMETROS
            # LLAMAR AL ALGORITMO MORENO
        elif op[0] == 4:
            print("Bais")
        return
    
    while op[0] != 4:
        selecAlgo()
    
leerTxD(cont)
Guardar()
Display3D()
