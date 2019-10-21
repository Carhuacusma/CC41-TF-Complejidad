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

a = [None]*3
a = [1,1,1]
MyRec = []
nPLLPPD = []
cont = 0
Contenedores = []

def leerTxD(cont):
    archivo = open("Entrada.txt","r")
    n = archivo.readlines()
    for i in n:
        contenedor = i
        helpm = contenedor.split(" ")
        if cont == 0:
            a[0] = int(helpm[0])
            a[1] = int(helpm[1])
            a[2] = int(helpm[2])
            
            volumen = a[0] * a[1] * a[2]
            Contenedores.append([a[0],a[1], a[2], volumen])


        elif cont == 1:
            nPLLPPD.append(int(helpm[0]))
        else:
            MyRec.append([Paralelepipedo(int(helpm[2]),int(helpm[3]),int(helpm[4]),helpm[1]+str(0))])
            q = int(contenedor[0])
            if q > 1:
                for x in range(q-1):
                    MyRec[cont-2].append(Paralelepipedo(int(helpm[2]),int(helpm[3]),int(helpm[4]),helpm[1]+str(x+1)))
    
        cont +=1
        
        
leerTxD(cont)
print(a)
print(nPLLPPD)
#print(contenedor_Ancho,contenedor_Largo,contenedor_Alto)
for x in range(len(MyRec)):
    for i in range(len(MyRec[x])):
        MyRec[x][i].display()

def Guardar():
    archivo = open("Archivo Salida", 'w+')
    n = len(MyRec) #Numero de cajas a transportar
    p = len(Contenedores) #Numero de contenedores usados
    vu = 0 #Volumen utilizado
    vd = 0 #Volumen disponible
    
    a = "Contenedores usados: " + str(p) + "\n" 
    b = "Volumen disponible: " + str(vd) + " m2 \n"
    c = "Volumen ocupado: " + str(vu) + " m2 \n"
    d = "Cajas a transportar: " + str(n) + "\n"
    
    archivo.write(a+b+c+d)
    archivo.write("Contenedor Formato Coordenadas Orientacion:\n")
    
    for i in range(n):
        for z in range(len(MyRec[i])):
            archivo.write("%d\t\t\t%s\t\t\t%d%d\t\t\t%d\n"%(MyRec[i][z].Contenedor,MyRec[i][z].Myid,MyRec[i][z].Pos[0],MyRec[i][z].Pos[1],MyRec[i][z].rotacion))
            print("salio")
        
Guardar()


