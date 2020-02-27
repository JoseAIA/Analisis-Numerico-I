#--------------------------------------------------------------
#   Programa que utiliza el metodo de Biseccion para el calculo
#   de raices de un polinomio de n grado
#
#   PROGRAMA        :       Biseccion.py
#   PROGRAMADOR     :       
#   LENGUAJE        :       Python
#   FECHA           :       03 de Marzo de 2012
#---------------------------------------------------------------


import os       
import math


#---------------------------------------------------------------
# Funcion que muestra el titulo del programa
#---------------------------------------------------------------
def titulo():
    os.system("CLS")
    print ("Metodo de biseccion\n")


#---------------------------------------------------------------
# Funcion que define f(x)
#---------------------------------------------------------------
def f(x):
    return x**2 -2

  
#---------------------------------------------------------------
# FUNCION QUE CALCULA Mx
#---------------------------------------------------------------
def Mx(a, b):
    return (a + b) / 2


#---------------------------------------------------------------
# METODO DE BISECCION
#---------------------------------------------------------------
def biseccion(iInicial, iFinal):
    a = iInicial
    b = iFinal
    nIteraciones = math.ceil((math.log(b - a) - math.log(0.00001)) / math.log(2))


    titulo()


    print ("{0}\t{1}\t{2}\t{3}\t{4}".format('n iter ', 'a', 'b', 'Mx', 'f(Mx)f(a)'))


    i = 1
    while(i <= nIteraciones):
        x = Mx(a, b)
        Fx = f(x)
        Fa = f(a)


        condicion = Fx * Fa


        print (i, "\t{:.4}\t{:.4}\t{:.4}\t{:.4}".format(a, b, x, condicion))


        if(condicion > 0):
            a = x
        elif(condicion < 0):
            b = x
        else:
            x = x


        i += 1
    print ("\nLa raiz encontrada es: {0}\n".format(x))


#---------------------------------------------------------------
#Programa principal
#---------------------------------------------------------------


consulta = '1'
while(consulta != '0'):
    os.system("COLOR F0")
    titulo()


    print                                                  
    iInicial = float(input("Intervalo inicial: "))      
    iFinal = float(input("Intervalo final: "))         


    titulo()


    
    biseccion(iInicial, iFinal)


    print
    consulta = input("Para salir presiona 0, sino otra tecla: ")
