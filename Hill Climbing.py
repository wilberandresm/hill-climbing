import template as t
import numpy as np
import random as r

def ObjetiveFunction(pos,matriz):
    d = 0
    for i in range(len(pos)-1):
        d += matriz[pos[i]][pos[i+1]]#suma de la distancias anterior con la siguiente
    return d

def NewPosition(x):#creacion de rutas aleatorias
    x1 = r.randint(1,len(x)-2)
    x2 = r.randint(1,len(x)-2)
    while(x2==x1):#verificacion de no revisar el mismo punto
        x2 = r.randint(1,len(x)-2)
    aux = x[x1]
    x[x1] = x[x2]
    x[x2] = aux
    return x

if __name__ == "__main__":
    coor = t.distancesFromCoords() #coordenadas
    x = [] 
    pos = r.randint(0,len(coor)-1) #primera posicion random 
    x.append(pos) #posicion inicial cualquiera
    for i in range(len(coor)):
        if(i!=pos):
            x.append(i) 
    x.append(pos) #guardar el resto de posiciones
    new_d = 0 #nueva distancia
     #Numero de iteraciones ideal para encontrar la mejor ruta
    i = 44000

    while(i>0):
        d = ObjetiveFunction(x,coor)#distancia actual
        new_x = NewPosition(x[:]) #generador de nueva posición aleatoria
        new_d = ObjetiveFunction(new_x,coor)#generador de nueva distancia
        if(new_d<d): #entonces comparamos , sí la nueva distancia es menos a la anterior
            x = new_x #sí es así , la posición anterior cambiaría por la nueva
        i -= 1 #decremento 

    print("Route:",x)
    print("Final distance:",new_d)