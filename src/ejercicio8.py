################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
Escribir una función que indique con True si un numero indicado es primo.
"""


def es_primo(numero):
    """
    Esta función se encarga de determinar si el número ingresado
    es o no es primo.
    Precondición: Ingresar un número entero positivo
    Postcondición: Devolver True si es primo, False si no lo es
    """
    if numero > 1:
        contador=0
        divi=2
        while divi < numero and contador==0:
            resto = numero % divi
            if resto ==0:
                contador+=1
            divi+=1
        if contador ==0:
            primo=True
        else:
            primo=False
        return primo


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    entrada = 17
    num_primo = es_primo(numero)
    salida = "True"
    """


if __name__ == "__main__":
    principal()
