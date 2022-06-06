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
    sin mayusculas ni acentos (palabra)
    Postcondición: Mostrar True si son palindromos, False si no lo son.
    """
    return str(texto) == str(texto)[::-1]


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
