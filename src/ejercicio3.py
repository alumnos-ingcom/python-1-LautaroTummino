################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:
Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""


def compara(numero, otro_numero):
    """
    Esta función se encargar de determinar, cual de los números ingresados
    es mayor, o sin son iguales.
    Precondicion: Ingresar dos números enteros para comparar
    Postcondición: Mostrar cual de esos números es mayor, o mostrar igualdad en
    el caso en que ambos sean 0
    """
    resta = numero - otro_numero
    suma = otro_numero + (numero * -1)
    if resta > suma:
        salida = "1" + " " + "El primero es mayor"
    elif suma > resta:
        salida = "-1" + " " + "El segundo es mayor"
    else:
        salida = "0" + " " + "Son iguales"
    return salida


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    numero = 25
    otro_numero = 15
    compara_numeros = compara(numero, otro_numero)
    salida = print(f"El número mayor es {salida}")
    """


if __name__ == "__main__":
    principal()
