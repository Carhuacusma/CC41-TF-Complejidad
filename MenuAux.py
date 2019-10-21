#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
    elif op[0] == 2:
        print("Teclado")
        # LLAMAR A FUNCION QUE LEE POR TECLADO
    elif op[0] == 3:
        print("Random")
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
    
Menu()

