################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o frase
ingresada se trata de un palindromo.
Palíndromo, es si se lee igual
de derecha a izquierda que de izquierda a derecha.
"""


def es_palindromo(texto):
    """
    Esta función se encarga de determinar si un texto ingresado es un palindromo
    o si no lo es.
    Precondición: Ingresar una cadena de caracteres
    sin mayusculas ni acentos.
    Postcondición: Mostrar True si es un palindromo, False si no.
    """
    texto_dos = ""
    n = 0
    neg = -1
    while n < len(texto):
        if texto[n] == texto[neg]:
            texto_dos = texto_dos + texto[neg]
        n += 1
        neg -= 1
    if texto == texto_dos:
        return True
    else:
        return False


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    texto = str(input("Ingrese una palabra: "))
    frase_palindro = es_palindromo(texto)
    print(f"{frase_palindro}")


if __name__ == "__main__":
    principal()
