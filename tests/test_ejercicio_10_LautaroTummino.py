################
# Lautaro  - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio10 import es_palindromo


def test_es_palindromo():
    """
    Esta función se encarga de los testeos de la función del ejercicio 10 identificar
    si una cadena/texto es un palindromo o no. Esta función sirve solo para letras minusculas y sin acentuación
    """
    texto = "neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano, Verdadero o Falso"
    assert resultado == True, "El resultado es correcto, el texto es un palindromo"
