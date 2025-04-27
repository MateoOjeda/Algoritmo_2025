# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos 
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con 
# ayuda de la fuerza” realizar las siguientes actividades:
#       
#       a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#       queden más objetos en la mochila;
# 
#       b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
#       para encontrarlo;
# 
#       c. Utilizar un vector para representar la mochila.

def usar_fuerza(mochila, objetos_sacados=0):
    # Si la mochila esta vacia y no encontramos el sable
    if not mochila:
        return False, objetos_sacados

    # Sacamos el primer objeto
    objeto = mochila.pop(0)
    objetos_sacados += 1

    # Verificamos si es un sable de luz
    if objeto == "sable de luz":
        return True, objetos_sacados

    # Si no era, seguimos buscando recursivamente
    return usar_fuerza(mochila, objetos_sacados)

# Ejemplo de uso:
mochila = ["comida", "botiquin", "comunicador", "sable de luz", "capa"]

# Clonamos la mochila para no destruir la original durante la busqueda
mochila_copia = mochila.copy()
encontro_sable, objetos_extraidos = usar_fuerza(mochila_copia)

if encontro_sable:
    print(f" Sable de luz encontrado tras sacar {objetos_extraidos} objetos.")
else:
    print(" No se encontro el sable de luz en la mochila.")