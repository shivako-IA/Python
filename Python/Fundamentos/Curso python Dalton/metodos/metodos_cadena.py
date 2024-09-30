cadena1 = "Hola soy Ako"
cadena2 = "Bienvenido Maquinola"

# Convierte a mayúsculas
mayusc = cadena1.upper()

# Convierte a minúsculas
minusc = cadena1.lower()

# Primera letra en mayúscula
primer_letra_mayusc = cadena1.capitalize()

# Buscamos una subcadena en cadena1, por ejemplo "soy"
busqueda_find = cadena1.find("soy")  # Pasa una subcadena como argumento

# Buscamos una subcadena en cadena1, por ejemplo "Ako"
busqueda_index = cadena1.index("Ako")  # Pasa una subcadena como argumento

# Si es numérico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

# Si es alfanumérico, devolvemos true, sino devolvemos false
# Aquí cadena1 contiene espacios, así que esto devolverá False
es_alfanumerico = cadena1.replace(" ", "").isalpha()  # Elimina espacios antes de verificar

# Contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("Hola")

#contamos cuantos caracteres tiene una cadena
contar_Caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("A")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasamos
cadena_separada = cadena1.split(",")

print(cadena_separada[0])
