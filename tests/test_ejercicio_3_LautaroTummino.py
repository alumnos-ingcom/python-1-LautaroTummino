################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio3 import compara


def test_compara_mayor():
    """
    Esta función se encarga de los testeos de la función del ejercicio 3 de
    comparación de números mayores
    """
    numero = 25
    otro_numero = 15
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, str), "El resultado es una string"
    assert resultado == "1 - El primero es mayor", "El resultado debe indicar el número mayor, menor o cero"


def test_compara_menor():
    """
    Esta función se encarga de los testeos de la función del ejercicio 3 de
    comparación de números menores
    """
    numero = 15
    otro_numero = 25
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, str), "El resultado es una string"
    assert resultado == "-1 - El segundo es mayor", "El resultado debe indicar el número mayor, menor o cero"


def test_compara_iguales():
    """
    Esta función se encarga de los testeos de la función del ejercicio 3 de
    comparación de números menores
    """
    numero = 15
    otro_numero = 15
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, str), "El resultado es una string"
    assert resultado == "0 - Son iguales", "El resultado debe indicar el número mayor, menor o cero"
