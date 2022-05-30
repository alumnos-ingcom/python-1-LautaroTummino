################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
Escribir una función que indique con True si
un número entero es multiplo de otro, utilizando sumas y restas.
"""


def es_multiplo(numero, multiplo):
    """
    Esta función se encarga de determinar si un número es multiplo
    de otro número.
    Precondición: Ingresar un número y el multiplo deseado
    Postcondición : Muestra por pantalla True si es multiplo, False si no
    """
    while numero > 1:
        numero = numero - multiplo
    if numero == 0:
        resultado=True
    else:
        resultado=False
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    entrada : numero = 8  |  multiplo = 2
    multi = es_multiplo(numero, multiplo)
    salida : True
    """


if __name__ == "__main__":
    principal()
