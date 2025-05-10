# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe
# (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
# las siguientes actividades:
#     a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#        además mostrar el nombre de dichas películas;
#     
#     b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
#     
#     c. eliminar los modelos de los trajes destruidos mostrando su nombre; 
# 
#     d. un modelo de traje puede usarse en más de una película y en una película se pueden usar 
#        más de un modelo de traje, estos deben cargarse por separado;
# 
#     e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos 
#        repetidos en una misma película;
#    
#     f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
#        “Capitan America: Civil War”.

from ClasesPilas import Stack

lista_trajes = [
    {"modelo": "Mark I", "pelicula": "Iron Man ", "estado": "Destruido"},
    {"modelo": "Mark II", "pelicula": "Iron Man ", "estado": "Modificado (War Machine)"},
    {"modelo": "Mark III", "pelicula": "Iron Man ", "estado": "Danado"},
    {"modelo": "Mark IV", "pelicula": "Iron Man 2 ", "estado": "Impecable"},
    {"modelo": "Mark V", "pelicula": "Iron Man 2 ", "estado": "Danado"},
    {"modelo": "Mark VI", "pelicula": "Iron Man 2 / The Avengers", "estado": "Danado"},
    {"modelo": "Mark VII", "pelicula": "The Avengers ", "estado": "Danado"},
    {"modelo": "Mark XLII (42)", "pelicula": "Iron Man 3 ", "estado": "Destruido"},
    {"modelo": "Mark XLIII (43)", "pelicula": "Avengers: Age of Ultron ", "estado": "Impecable"},
    {"modelo": "Mark XLIV (44) - Hulkbuster", "pelicula": "Avengers: Age of Ultron ", "estado": "Danado"},
    {"modelo": "Mark XLVI (46)", "pelicula": "Captain America: Civil War ", "estado": "Danado"},
    {"modelo": "Mark L (50)", "pelicula": "Avengers: Infinity War ", "estado": "Destruido"},
    {"modelo": "Mark XLIV (44) - Hulkbuster", "pelicula": "Avengers: Infinity War", "estado": "Danado"},
    {"modelo": "Mark LXXXV (85)", "pelicula": "Avengers: Endgame ", "estado": "Destruido"},
]

pila_trajes = Stack()

for armaduras in lista_trajes:
    pila_trajes.push(armaduras)

print("- Armaduras de Iron man: ")
pila_trajes.show() # mostramos los elementos de la pila

# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas;
pila_hulk_arm = Stack()
pila_aux = Stack()
while pila_trajes.size() > 0:
    armadura = pila_trajes.pop()
    if armadura["modelo"] == "Mark XLIV (44) - Hulkbuster":
        pila_hulk_arm.push(armadura)
    pila_aux.push(armadura)

# Restaurar pila original
while pila_aux.size() > 0:
    pila_trajes.push(pila_aux.pop())

print("-----------------------------------------")

print(" A. Apariciones de la hulkbuster:")
pila_hulk_arm.show() # mostramos los elementos de la pila
print("-----------------------------------------")

# b. mostrar los modelos que quedaron dañados, sin perder información de la pila. (VER)

pila_danados = Stack()
pila_aux_2 = Stack()

while pila_trajes.size() > 0:
    estado_armadura = pila_trajes.pop()
    if estado_armadura ["estado"] == "Danado":
        pila_danados.push(estado_armadura)
    pila_aux_2.push(armadura)

# Restaurar pila original
while pila_aux_2.size() > 0:
    pila_trajes.push(pila_aux_2.pop())

print(" B. Armaduras Danadas:")
pila_danados.show()

print("-----------------------------------------")

# c. eliminar los modelos de los trajes destruidos mostrando su nombre; 

pila_trajes_destruidos = Stack()
pila_aux_3 = Stack()

while pila_trajes.size() > 0:
    arm_destruidas = pila_trajes.pop()
    if arm_destruidas["estado"] == "Destruido":
        pila_trajes_destruidos.push(arm_destruidas)
    else:
        pila_aux.push(armadura)

# Restaurar pila original sin los destruidos
while pila_aux_3.size() > 0:
    pila_trajes.push(pila_aux_3.pop())

print(" C. Armaduras Destruidas:")
pila_trajes_destruidos.show() # mostramos los elementos de la pila
print("-----------------------------------------")

# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, estos deben cargarse por separado;
vistos = set() # [ set() ]--> colección desordenada de elementos únicos. A diferencia de las listas o tuplas, los sets no permiten elementos duplicados y no conservan el orden de los elementos

for armadura in lista_trajes:
    clave = (armadura["modelo"], armadura["pelicula"].strip())
    if clave not in vistos:
        pila_trajes.push(armadura)
        vistos.add(clave)
    else:
        print(f"Modelo duplicado ignorado en misma película: {clave}")

# Mostrar pila después de aplicar la lógica del punto D
print(" D. Pila cargada (modelo/película únicos):")
pila_trajes.show()
print("-----------------------------------------")
# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
pila_aux_4 = Stack()
modelo_exist = False

print("PUNTO E.")
# agregar el nuevo traje
nuevo_traje = {
    "modelo": "Mark LXXXV (85)",
    "pelicula": "Avengers: Endgame ",
    "estado": "Impecable"
}

while pila_trajes.size() > 0:
    armadura = pila_trajes.pop()
    if armadura["modelo"] == "Mark LXXXV" and armadura["pelicula"].strip() == nuevo_traje["pelicula"].strip():
        modelo_exist = True
    pila_aux_4.push(armadura)
    
while pila_aux_4.size() > 0:
    pila_trajes.push(pila_aux_4.pop())

if not modelo_exist:
    pila_trajes.push(nuevo_traje)
    print("Se agregó el nuevo traje Mark LXXXV.")
else:
    print("El traje Mark LXXXV ya existe en una película. No se agregó.")
print("-----------------------------------------")

# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming”  “Capitan America: Civil War”.
pila_aux_5 = Stack()
pila_arm_peliculas = Stack()

while pila_trajes.size() > 0:
    armadura = pila_trajes.pop()
    pelicula_normalizada = armadura["pelicula"].strip()
    if pelicula_normalizada in ["Spider-Man: Homecoming", "Captain America: Civil War"]:
        pila_arm_peliculas.push(armadura)
    pila_aux_5.push(armadura)

while pila_aux_5.size() > 0:
    pila_trajes.push(pila_aux_5.pop())

print(" F. Trajes utilizados en las películas:")
print("-----------------------------------------")
pila_arm_peliculas.show() # mostramos los elementos de la pila