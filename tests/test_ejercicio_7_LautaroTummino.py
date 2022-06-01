################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal


def test_sexadecimal_a_decimal():
    """
    Esta función se encarga de los testeos de la función del ejercicio 7 de
    pasar de sexadecimal a decimal
    """
    horas = 1
    minutos = 5
    segundos = 10
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero, que representa los segundos"
    assert resultado == 3910, "El resultado debe ser el horas,minutos,segundos pasado a segundos"


def test_decimal_a_sexadecimal():
    """
    Esta función se encarga de los testeos de la función del ejercicio 7 de
    pasar de decimal a sexadecimal
    """
    numero = 3800
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla de valores ordenados en horas,minutos,segundos"
    assert resultado == (1,3,20), "El resultado deben ser los números ordenados en horas, segundos minutos"
