from typing import Any


def una_funcion(a,b):
    """comentario con una descripcion de la funcion"""
    print("Soy la funcion una_funcion con argumentos")
    print(a+b)

def sentenciaif(a,b):
    if(a!=b):
        print("es distinto, amigo")
    else:
        print("son jodidamente clavados")

def sentenciafor():
    lista_numeros = range(10)  # lista del 0 al 9
    for numero in lista_numeros:
        # verifica si numero pertecene a una tupla
        if numero in (1, 3, 5, 7, 9):
            printf("es impar")
        elif numero in (2, 4, 6, 8):
            print("es par")
        else:
            print("debe ser el 0")

def sentenciawhile(a):
    while a !=20:
        a+=1
        print(a)