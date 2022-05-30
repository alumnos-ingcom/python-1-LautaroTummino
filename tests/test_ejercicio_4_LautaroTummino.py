################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio4 import suma_lenta


def test_suma_lenta_positivo():
    """
    Esta función se encarga de los testeos de la función del ejercicio 4 de
    suma lenta para números positivos
    """
    numero = 15
    otro_numero = 25
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser entero"
    assert resultado > 0, "El resultado debe ser mayor a 0"
    assert resultado == 40, "El resultado es correcto"


def test_suma_lenta_negativo():
    """
    Esta función se encarga de los testeos de la función del ejercicio 4 de
    suma lenta para números negativos
    """
    numero = -35
    otro_numero = 25
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser entero"
    assert resultado < 0, "El resultado debe ser menor a 0"
    assert resultado == -10, "El resultado es correcto"


def test_suma_lenta_ceros():
    """
    Esta función se encarga de los testeos de la función del ejercicio 4 de
    suma lenta para ceros
    """
    numero = 0
    otro_numero = 0
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser entero"
    assert resultado == 0, "El resultado debe ser igual a 0"
    