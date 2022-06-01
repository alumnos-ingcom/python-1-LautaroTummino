################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio8 import es_primo


def test_es_primo():
    """
    Esta función se encarga de los testeos de la función del ejercicio 8 identificar
    si un número, es o no primo
    """
    numero = 5
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser booleano (Verdadero o Falso)"
    assert resultado == True, "El resultado es correcto"
