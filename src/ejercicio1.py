################
# Lautaro Tummino - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################


"""
1.Conversión de temperaturas
Se quiere transformar temperaturas en grados
fahrenheit a gradoscentígrados y viceversa.
Escribir las funciones para convertir la temperatura
en grados centigrados en fahrenheit como un número
decimal, utilice esta formula para calcular los grados
centígrados y retorne el resultado obtenido. Y viceversa.
"""


def convertir_a_fahrrenheit(centigrados):
    """
    Esta función se encarga de transformar un número expresado en centigrados
    a grados fahrenheit
    Precondición = Ingresar un número decimal
    Postcondición = Mostrar la conversion de ese número a grados fahrenheit
    """
    centi = (centigrados * 1.8) + 32
    return centi


def convertir_a_centigrados(fahrenheit):
    """
    Esta función se encarga de transformar un número expresado en fahrenheit
    a grados centigrados.
    Precondición = Ingresar un número decimal
    Postcondición = Mostrar la conversiion de ese número a grados centigrados
    """
    fahre = (fahrenheit - 32) / (1.8)
    return fahre


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    entrada1 = float(input("Ingrese los grados centigrados que quiere transformar
    a grados fahrenheit
    convert = convertir_a_fahrrenheit(centigrados)
    salida= print(f"El número {entrada1} corresponde a {centi} grados centigrados")
    entrada2 = float(input("Ingere los grados fahrenheit que quiere transoformar a
    grados centigrados
    convertor = convertir_a_centigrados(fahrenheit)
    salida = print("El número {entrada2} corresponde a {fahre} grados fahrenheit")
    """


if __name__ == "__main__":
    principal()
    