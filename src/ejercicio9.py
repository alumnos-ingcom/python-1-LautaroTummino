################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
Escribir una función que retorne una tuple
con factores primos de un numero entero positivo.
"""


def factores_primos(numero):
    """
    Esta función se encarga de determinar los factores primos de un número
    Precondición : Ingrese un número
    Postcondición : Muestra una tupla con los factores primos del número
    """
    divisor = 2
    conta = ()
    while numero != 1:
        if numero % divisor == 0:
            result = (divisor)
            conta = conta + (result,)
            numero = numero // divisor
        else:
            divisor = divisor + 1
    return conta


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    entrada = 48
    factores_num = factores_primos(numero)
    salida = (2, 2, 2, 2, 3)
    """


if __name__ == "__main__":
    principal()
