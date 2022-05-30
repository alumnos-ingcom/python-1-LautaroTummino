################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados


def test_convertir_a_fahrrenheit():
    """
    Esta función se encarga de los testeos de la función del ejercicio 1 de
    centigrados a fahrenheit
    """
    centigrados = 15
    resultado = convertir_a_fahrrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser decimal o float"
    assert resultado > 0, "El resultado debe ser mayor a 0"
    assert resultado == 59.0, "El resultado es correcto"


def test_convertir_a_centigrados():
    """
    Esta función se encarga de los testeos de la función del ejercicio 1 de
    fahrenheit a centigrados
    """
    fahrenheit = 1
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser decimal o float"
    assert resultado < 0, "El resultado debe ser mayor a 0"
    assert resultado == -17.22222222222222, "El resultado es correcto"
