################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import division_lenta


def test_division_lenta():
    """
    Esta función se encarga de los testeos de la función del ejercicio 5 de
    la division lenta
    """
    dividendo = 8
    divisor = 2
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado deben ser el cociente y el resto en una tupla"
    assert resultado == (4, 0), "El resultado es correcto"
