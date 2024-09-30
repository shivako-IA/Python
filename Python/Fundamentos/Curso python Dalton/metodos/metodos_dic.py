diccionario ={
    "nombre" :"Andres",
    "apellido" : "Velez",
    "day" : 273
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_krishna = diccionario.get("krishna")
print("Om el mundo esta lleno de sufrimiento, el programa continua")

#elimindando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)