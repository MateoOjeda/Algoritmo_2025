#  22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
#      el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
#      F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
#      Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#     
#      a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#     
#      b. mostrar los nombre de los superhéroes femeninos;
#    
#      c. mostrar los nombres de los personajes masculinos;
#   
#      d. determinar el nombre del superhéroe del personaje Scott Lang;
#    
#      e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S; 
#   
#      f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombrede superhéroes.

from ClaseCola import Queue


lista_personajes = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitan America", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
]
cola_personajes = Queue()

for personajes in lista_personajes:
    cola_personajes.arrive(personajes)

cola_aux = Queue()

#variables para respuestas
capinata_marvel = None
heroes_m = []
heroes_f = []
heroe_scott = None
nombres_s = []
personajes_carol = False
heroe_carol = None

while cola_personajes.size() > 0:
    datos = cola_personajes.attention()
    cola_aux.arrive(datos)

    if datos["superheroe"] == "Capitan America":
        capinata_marvel = datos["personaje"]

    if datos["genero"] == "F":
        heroes_f.append(datos["superheroe"])

    if datos["genero"] == "M":
        heroes_m.append(datos["superheroe"])

    if datos["personaje"] == "Scott Lang":
        superheroe_scott_lang = datos["superheroe"]

    # e. Nombres que empiezan con S
    if datos["personaje"].startswith("S") or datos["superheroe"].startswith("S"):
        nombres_s.append(datos)

    # f. Buscar Carol Danvers
    if datos["personaje"] == "Carol Danvers":
        carol_danvers_encontrada = True
        superheroe_carol = datos["superheroe"] 


while cola_aux.size() > 0:
    cola_personajes.arrive(cola_aux.attention())

# Mostramos las respuestas
print(f"- El nombre del personaje de Capitana Marvel es: {capinata_marvel}")
print(f"- Superheroes femeninos: {', '.join(heroes_f)}")
print(f"- Personajes masculinos: {', '.join(heroes_m)}")
print(f"- El superheroe de Scott Lang es: {heroe_scott}")
print(f"- Datos de nombres que comienzan con S:")
for d in nombres_s:
    print(f"- Personaje: {d['personaje']}, Superheroe: {d['superheroe']}, Genero: {d['genero']}")
if heroe_carol:
    print(f"- Carol Danvers se encuentra en la cola y su nombre de superheroe es: {heroe_carol}")
else:
    print("- Carol Danvers no se encuentra en la cola.")