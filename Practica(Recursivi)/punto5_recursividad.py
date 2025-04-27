'''
Desarrollar una función que permita convertir un número romano en un número decimal
'''

def num_romanos(romanos):
    valores = { 
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    total = 0 # acumula el valor decimal final
    previo = 0 # guarda el valor anterior

    for letra in reversed(romanos.upper()): # upper hace que el valor en romano que imgresemos esto lo combierte en mayuscula
      
       #Buscamos el valor decimal de la letra romana. Si no la encuentra, devuelve 0 (eso evita errores si hay una letra inválida, aunque después podríamos mejorar eso).
        valor = valores.get(letra, 0)
        if valor < previo:
            total -= valor
        #Si no es menor, entonces simplemente **sumamos** y actualizamos `prev` con el valor actual.
        else:
            total += valor
            previo = valor
    
    return total

numero_ingre = input('ingrese un numero en romano: ')
print(num_romanos(numero_ingre))    


