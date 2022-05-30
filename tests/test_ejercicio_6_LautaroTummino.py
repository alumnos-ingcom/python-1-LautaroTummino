################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor


def test_ordenar_mayor_a_menor():
    """
    Esta función se encarga de los testeos de la función del ejercicio 6 de
    ordenar un número de mayor a menor
    """
    uno = 10
    dos = 5
    tres = 25
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla de valores ordenados de mayor a menor"
    assert resultado == (25,10,5), "El resultado deben ser los números ordenados de mayor a menor"


def test_ordenar_menor_a_mayor():
    """
    Esta función se encarga de los testeos de la función del ejercicio 6 de
    ordenar un número de menor a mayor
    """
    uno = 10
    dos = 5
    tres = 25
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla de valores ordenados de menor a mayor"
    assert resultado == (5,10,25), "El resultado deben ser los números ordenados de menor a mayor"
