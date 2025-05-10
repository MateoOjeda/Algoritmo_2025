# 10.Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# 
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# 
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# 
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

from ClaseCola import Queue
from ClasesPilas import Stack
from random import choice, randint
from datetime import datetime

# a
def eliminar_not_cola(cola):
    cola_aux = Queue()

    while cola.size() > 0:
        notificaciones = cola.attention()
        if  notificaciones["aplicacion"] != "Facebook":
            cola_aux.arrive(notificaciones)

    return cola_aux

# b
def montrar_not_cola(cola):
    resultado = []
    for _ in range(cola.size()):
        notif = cola.attention()
        if notif["aplicacion"] == "Twitter" and "python" in notif["mensaje"].lower():
            resultado.append(notif)
        cola.arrive(notif)
    return resultado

apps = ["Facebook", "Twitter", "Instagram", "WhatsApp"]
mensajes = [
    "Nueva publicacion", "Python es genial", "Mira este video",
    "No te lo pierdas!", "Aprende Python", "Mensaje privado", "Recordatorio"
]

def generador_hora():
    hora = randint(0, 23)
    minutos = randint(0, 59)
    return f"{hora:02}:{minutos:02}"

#cola de notificaciones
notificaciones_cola = Queue()

for i in range(10):
    notificaciones_cola.arrive({
        "hora" : generador_hora(),
        'aplicacion': choice(apps),
        'mensaje': choice(mensajes)
    })

def notificaciones_en_rango(cola: Queue, hora_inicio="11:43", hora_fin="15:57"):
    pila = Stack()
    fmt = "%H:%M"
    h_inicio = datetime.strptime(hora_inicio, fmt)
    h_fin = datetime.strptime(hora_fin, fmt)

    for _ in range(cola.size()):
        notif = cola.attention()
        hora_notif = datetime.strptime(notif["hora"], fmt)
        if h_inicio <= hora_notif <= h_fin:
            pila.push(notif)
        cola.arrive(notif)
    return pila, pila.size()

# Mostrar la cola de notificaciones
cola_sin_fb = eliminar_not_cola(notificaciones_cola)
twitter_python = montrar_not_cola(notificaciones_cola)
pila_rango, cantidad_rango = notificaciones_en_rango(notificaciones_cola)

# --- Mostrar resultados ---
print("- Cola sin notificaciones de Facebook:")
cola_sin_fb.show()

print("- Notificaciones de Twitter con 'Python':")
for notif in twitter_python:
    print(notif)

print("- Notificaciones entre 11:43 y 15:57:")
pila_rango.show()
print("Total:", cantidad_rango)