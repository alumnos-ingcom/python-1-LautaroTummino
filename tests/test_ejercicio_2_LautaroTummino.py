################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import signo


def test_signo_positivo():
    """
    Esta función se encarga de los testeos de la función del ejercicio 2 de
    signo
    """
    numero = 25
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado es una string"
    assert resultado == 1, "El resultado debe ser mayor a 0"


def test_signo_negativo():
    """
    Esta función se encarga de los testeos de la función del ejercicio 2 de
    signo
    """
    numero = -25
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado es una string"
    assert resultado == -1, "El resultado debe ser menor a 0"


def test_signo_cero():
    """
    Esta función se encarga de los testeos de la función del ejercicio 2 de
    signo
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado es una string"
    assert resultado == 0, "El resultado debe ser igual a 0"
