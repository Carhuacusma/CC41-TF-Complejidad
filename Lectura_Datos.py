#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
nPLLPPD = 0
cont = 0
Contenedores = []
volumen = 0

def leerTxD(cont):
    archivo = open("Entrada.txt","r")
    n = archivo.readlines()
    for i in n:
        contenedor = i
        if cont == 0:
            contenedor.split(" ")
            contenedor_Ancho = contenedor[0]
            contenedor_Largo = contenedor[2]
            contenedor_Alto  = contenedor[4]
            print("entra")
            a[0] = int(contenedor_Ancho)
            a[1] = int(contenedor_Largo)
            a[2] = int(contenedor_Alto)
            
            
            volumen = int(contenedor_Ancho) * int(contenedor_Largo) * int(contenedor_Alto)
            Contenedores.append([contenedor_Ancho,contenedor_Largo, contenedor_Alto, volumen])


        elif cont == 1:
            nPLLPPD = contenedor[0]
        else:
            MyRec.append([Paralelepipedo(contenedor[4],contenedor[6],contenedor[8],contenedor[2]+str(0))])
            q = int(contenedor[0])
            if q > 1:
                for x in range(q-1):
                    MyRec[cont-2].append(Paralelepipedo(contenedor[4],contenedor[6],contenedor[8],contenedor[2]+str(x+1)))
    
        cont +=1
        
        
leerTxD(cont)
print(contenedor_Ancho,contenedor_Largo,contenedor_Alto)
for x in range(len(MyRec)):
    for i in range(len(MyRec[x])):
        MyRec[x][i].display()
        

    


# In[47]:


MyRec = []
Contenedores = []



def Guardar():
    archivo = open("Archivo Salida", 'w+')
    n = len(MyRec) #Numero de cajas a transportar
    p = len(Contenedores) #Numero de contenedores usados
    vu = 0 #Volumen utilizado
    vd = 0 #Volumen disponible
    
    a = "Contenedores usados: " + str(p) + "\n" 
    b = "Volumen disponible: " + str(vd) + "m2 \n"
    c = "Volumen ocupado: " + str(vu) + "m2 \n"
    d = "Cajas a transportar: " + str(n) + "\n"
    
    archivo.write(a+b+c+d)
    archivo.write("Contenedor Formato Coordenadas Orientacion:")
    for i in my
    print("hola")
    
    #for i in range(n):
        
Guardar()

