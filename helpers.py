import platform
import re
import os

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(long_min=0, long_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= long_min and len(texto) <= long_max:
            return texto

def dni_valido(dni, lista_consumidores):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI inválido, debe seguir el formato especificado.")
        return False
    for consumidor in lista_consumidores:
        if consumidor.dni == dni:
            print("DNI ya utilizado por otro consumidor.")
            return False
    return True
