#creando una lista con list 
lista = list([24,9,29,True,False])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(777)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,777)

#agregando varios elementos a la lista
lista.extend([True,2030])

#eliminando un elemento de la lista (con su indice)
lista.pop(-2) # -1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove(777)

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el prametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemeno_encontrado = lista.index(24)

print(elemeno_encontrado)