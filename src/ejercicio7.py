################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7.Transformación de un número
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
"""


def sexadecimal_a_decimal(horas,minutos,segundos):
    """
    Está función se encarga de transformar un número expresado en horas, minutos
    y segundos, a segundos.
    Precondición: Ingresar tres numeros para transformarlo en segundos
    Postcondicion: Muestra la cantidad de segundos equivalente a la hora ingresada
    """
    segundo = 0
    while horas > 0:
        horas = horas -1
        minutos = minutos + 60
    while minutos > 0:
        minutos = minutos -1
        segundo = segundo + 60
    segundos = segundos + segundo
    return segundos


def decimal_a_sexadecimal(numero):
    """
    Está función se encarga de transformar un numero ingresado en segundos
    a horas, minutos y segundos.
    Precondición: Ingresé un número para transformar en horas 
    Postcondición: Mostrar cantidad de horas, minutos, segundos.
    """
    minutos = 0
    horas = 0
    while numero > 59:
        minutos = minutos + 1
        numero = numero - 60
    while minutos > 59:
        horas = horas + 1
        minutos = minutos - 60
    return horas, minutos, numero


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    entrada=(1,0,0)
    llamada_sexa_a_deci=sexadecimal_a_decimal(horas,minutos,segundos)
    salida=print(f"La cantidad de segundos es {segundos}")
  
    entrada=3600
    llamada_deci_a_sexa=decimal_a_sexadecimal(numero)
    salida=print(f"La cantidad es {horas} horas, {minutos} minutos
    y {numero} segundos")
    """


if __name__ == "__main__":
    principal()
