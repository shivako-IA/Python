#Tipos de datos Simples

#Definiendo una variable
nombre = "Ako"

#Definiendo una variable con snake_case
nombre_completo = "Andres Velez"

#Concatenar con +
bienvenida = "Hola " + " ¿Como estas?"

#Concatenar con f-strings
bienvenida = f"Hola {nombre} ¿Como estas?"

print(bienvenida)
print(nombre_completo)


#Operadores de pertenencia (int / not in)

print("Ako" in bienvenida) #True
print("Ako" not in bienvenida) #False

#Alcance de las variables (Scope)

#Variable global

x = "Shiva"

def my_function():
    global x
    
    #x = 777 # cambiar el valor de la variable global
    
    print(f"Variable global modificada dentro de la funcion: {x}")
    
my_function()
print(f"Variable global despues de la funcion: {x}")

    # variable local 
    
x = "Shivako"

print(f"variable local x: {x}")

#variable global          
my_function()

print(f"Variable global x: {x}")

#Ejercicio Practico

"""Crea una función que calcule el área de un círculo. Usa variables locales dentro de la función y también variables globales para el radio del círculo.

python
"""

import math
 
 #Variable global
radio = 7
 
# Funcion para calcular el area y modificar la variable global

def calculate_area():
    global radio # Declaramos que queremos modificar la variable global
    radio = 10 # Modificamos el valor de la variable global
    area = math.pi * radio** 2 #Usamos el nuevo valor de "radio"
    print(f"El area del circulo es: {area}")
     
 # Llamamos a la funcion 
calculate_area()
print(f"El valor del radio despues de la funcion es: {radio}")