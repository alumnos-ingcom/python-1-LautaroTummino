################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################


"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables
de tipo entero retorne una tupla con dichos valores
ordenados de menor a mayor. Y Viceversa
"""


def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función se encarga de devolver los números ingresados,
    de mayor a menor.
    Precondición = Ingresar tres número a comparar
    Poscondición = Mostrar los números ordenados de mayor a menor
    """
    if uno > dos and dos > tres:
        resul=(uno,dos,tres)
    elif dos > uno and uno > tres:
        resul=(dos,uno,tres)
    elif tres > uno and uno > dos:
        resul=(tres,uno,dos)
    elif tres > dos and dos > uno:
        resul=(tres,dos,uno)
    elif uno > tres and tres > dos:
        resul=(uno,tres,dos)
    elif dos > tres and tres > uno:
        resul=(dos,tres,uno)
    else:
        resul="Todos o dos números son iguales"
    return resul


def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función se encarga de devolver los números ingresados,
    de menor a mayor.
    Precondición = Ingresar tres número a comparar
    Poscondición = Mostrar los números ordenados de menor a mayor
    """
    if uno < dos and dos < tres:
        resul=(uno,dos,tres)
    elif dos < uno and uno < tres:
        resul=(dos,uno,tres)
    elif tres < uno and uno < dos:
        resul=(tres,uno,dos)
    elif tres < dos and dos < uno:
        resul=(tres,dos,uno)
    elif uno < tres and tres < dos:
        resul=(uno,tres,dos)
    elif dos < tres and tres < uno:
        resul=(dos,tres,uno)
    else:
        resul="Todos o dos números son iguales"
    return resul


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print("Ordenar de Mayor A Menor")
    uno=int(input("Ingrese el primer número"))
    dos=int(input("Ingrese el segundo número"))
    tres=int(input("Ingrese el tercer número"))
    mayor_menor = ordenar_mayor_a_menor(uno, dos, tres)
    print(f"{mayor_menor}")
    
    print("Ordenar de Menor a Mayor")
    uno=int(input("Ingrese el primer número"))
    dos=int(input("Ingrese el segundo número"))
    tres=int(input("Ingrese el tercer número"))
    menor_mayor = ordenar_menor_a_mayor(uno, dos, tres)
    print(f"{menor_mayor}")


if __name__ == "__main__":
    principal()
