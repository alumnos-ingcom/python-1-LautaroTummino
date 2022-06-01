################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio11 import es_multiplo


def test_es_multiplo():
    """
    Esta función se encarga de los testeos de la función del ejercicio 11 determinar
    si un número es multiplo de otro.
    """
    numero = 2 
    multiplo = 5
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano, Verdadero o Falso"
    assert resultado == False, "El resultado es correcto, el texto es un palindromo"
