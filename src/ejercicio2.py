################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2.Números positivos y negativos
Escribir una función que reciba un número e indique si el
mismo es positivo, negativo o cero utilizando sumas y restas.
"""

def signo(numero):
    """
    Está función se encarga de determinar si un número es positivo(+), negavito(-) o
    si es cero (0).
    Precondición: Ingresé un número Real
    Postcondición: Mostrar si el número es: positvo (1), negativo (-1), o cero(0).
    """
    suma = numero + numero
    resta = numero - numero
    if suma > numero:
        signo_numerico = 1
    elif resta > numero:
        signo_numerico = -1
    else:
        signo_numerico = 0
    return signo_numerico


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número"))
    llamada_signo = signo(numero)
    print(f"El numero {numero} es {llamada_signo}")


if __name__ == "__main__":
    principal()
