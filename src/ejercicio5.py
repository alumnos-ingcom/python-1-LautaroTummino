################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
Escribir una función que mediante restas sucesivas,
obtenga el valor del cociente y resto de dos números enteros.
"""


def division_lenta(dividendo, divisor):
    """
    Esta función se encarga de realizar una division lenta entre los
    dos números ingresados (SOLO NÚMEROS POSITIVOS :/ ).
    Precondición: Ingrese dos números positivos
    Postcondicion: Muestrar el cociente y resto de la division. 
    """
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    return(cociente, dividendo)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = int(input("Ingrese el dividendo"))
    divisor = int(input("Ingrese el divisor"))
    div_lenta = division_lenta(dividendo, divisor)
    print(f"{div_lenta}")


if __name__ == "__main__":
    principal()
