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
    Precondición : Ingrese un número entero positivo
    Postcondición : Muestra una tupla con los factores primos del número
    """
    divisor = 2
    contar = ()
    while numero != 1:
        if numero % divisor == 0:
            result = (divisor)
            contar = contar + (result,)
            numero = numero // divisor
        else:
            divisor = divisor + 1
    return contar


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número: "))
    llamada_factores_primos = factores_primos(numero)
    print(f"{llamada_factores_primos}")


if __name__ == "__main__":
    principal()
