# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 16:53:27 2017

@author: Nicolás Hurtado
"""
import math

#Agregar tree edges.
def addt(l,nodes):
    for i in range(len(nodes)-1):
        l.append([nodes[i],nodes[i+1]])
    return

#Agregar cross edges.
def addc(l,left,right,c):
    counter = 0
    for i in range(len(right)):
        for j in range(1,len(left)):
            l.append([right[i],left[j]])
            counter+=1
            if counter==c:
                return

#Agregar back edges.
def addb(l,nodes,b):
    for i in range(len(nodes)-1):
        for j in range(len(nodes)):
            if b==0:
                return b
            if (nodes[j]>nodes[i]):
                l.append([nodes[j],nodes[i]])
                b-=1
    return b

#Agregar forward edges.
def addf(l,nodes,f):
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if f==0:
                return f
            if (nodes[i]+2<=nodes[j]):
                f-=1
    return f

#Se abre archivo con datos.
archivo = raw_input("Nombre de archivo Input: ")
inp = open(archivo, "r")
datos = inp.read().split(' ')

#Se guardan valores en las variables correspondientes.    
t=int(datos[0]) #tree edges.
b=int(datos[1]) #back edges.
f=int(datos[2]) #forward edges.
c=int(datos[3]) #cross edges.
n=t+1 #cantidad de nodos.

edges=[] #lista con aristas
rnodes=[] #Nodos a la derecha.
lnodes=[] #Nodos a la izquierda.
error=True #Variable para identificar si el grafo es posible.
r=0

for i in range (int(math.floor(n/2))):
    #max c = (n-i-1)*i
    #max f =((n-i-1)*(n-i-2))/2 , ((i)*(i-1))/2
    #max b,((n-i)*(n-i-1))/2 , ((i+1)*(i))/2
    #Se verifica que sea posible la combinación.
    if ((n-i-1)*i>=c and ((((n-i-1)*(n-i-2))/2 + ((i)*(i-1))/2)>=f) and (((n-i)*(n-i-1))/2 , ((i+1)*(i))/2)>=b):
        error = False
        r=i
        break

#Si el grafo es factible, se crea.
if not error:
    #Se agregan los nodos iniciales a la derecha e izquierda.
    if (c==0):
        for i in range(n):
            lnodes.append(i+1)
    else:
        for i in range(n-r):
            lnodes.append(i+1)
        for i in range(r):
            rnodes.insert(0,n-i)
    #Se agregan los tree edges.
    addt(edges,lnodes)
    if c>0:
        edges.append([1,rnodes[0]])
        addt(edges,rnodes)
    
    #Se agregan los cross edges.
    addc(edges,lnodes,rnodes,c)
    
    #Se agregan los back edges.
    b=addb(edges,lnodes,b)
    if c>0 and b>0:
        for i in range(len(rnodes)):
            edges.append([rnodes[i],1])
            b-=1
            if b==0:
                break
    if b>0:
        b=addb(edges,rnodes,b)
    if b>0:
        error = True
        
    #Se agregan los forward edges.    
    f=addf(edges,lnodes,f)
    if c>0 and f>0:
        for i in range(1,len(rnodes)):
            edges.append([1,rnodes[i]])
            f-=1
            if f==0:
                break
    if f>0:
        f=addf(edges,rnodes,f)
    if f>0:
        error = True    

#Caso especial, Grafo con un solo nodo, sin aristas.        
if n == 1 and b == 0 and f == 0 and c==0:
    error=False

#Si es que se pudo crear el grafo, se escribe en el archivo output.txt
if not error:
    out  = open("output.txt", "w") 
    out.write(str(n))
    out.write("\n")
    for i in range (1,n+1):
        counter=0
        for j in range(len(edges)):
            if edges[j][0]==i:
                counter +=1
        out.write(str(counter))
        for j in range(len(edges)):
            if edges[j][0]==i:
                out.write(" ")
                out.write(str(edges[j][1]))
        out.write("\n")
    out.close() 

#En el caso de que no se pudiera crear, el archivo output dira que no se pudo generar el grafo.    
else:
    out  = open("output.txt", "w")
    out.write("No se puede generar el Grafo")
    out.close()
        