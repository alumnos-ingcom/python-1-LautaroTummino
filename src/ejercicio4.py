################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
Escribir una función que haga la suma entre dos números
enteros sin hacer la operación de manera directa.
Esto quiere decir que para hacer la suma entre
4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero
entero positivo y negativo.
"""


def suma_lenta(numero, otro_numero):
    """
    Esta funcón se encargar de realizar una suma lenta, entre los
    dos números ingresados.
    Precondición: Ingresar dos números
    Postcondición: Mostrar el resultado de la suma de ambos números.
    """
    if otro_numero >= 0:
        while otro_numero > 0:
            numero = (numero) + 1
            otro_numero = (otro_numero) - 1
    elif otro_numero <= 0:
        while otro_numero < 0:
            numero = (numero) - 1
            otro_numero = (otro_numero) + 1
    return numero 


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    numero = int(input("Ingrese el primer número")
    otro_numero = int(input("Ingrese el segundo número")
    sumando = suma_lenta(numero, otro_numero)
    salida = print(f"El resultado de la suma de ambos números es: {numero}
    """


if __name__ == "__main__":
    principal()
