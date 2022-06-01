################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio9 import factores_primos


def test_factores_primos():
    """
    Esta función se encarga de los testeos de la función del ejercicio 9 identificar
    los factores primos de un número
    """
    numero = 15
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla con los factores primos"
    assert resultado == (3, 5), "El resultado es correcto"
