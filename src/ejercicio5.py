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
    dos números ingresados.
    Precondición: Ingrese dos números
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
    dividendo = 8
    divisor = 2
    div_lenta = division_lenta(dividendo, divisor)
    salida = print("El cociente de la division es {cociente} y el resto {dividendo}
    """


if __name__ == "__main__":
    principal()
