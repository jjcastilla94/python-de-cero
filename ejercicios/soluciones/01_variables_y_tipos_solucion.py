"""
EJERCICIO 2 - Operadores
========================
Verifica la solucion ejecutando:
    python soluciones/01_variables_y_tipos_solucion.py
"""


def _main(ejercicios):
    import inspect

    for ej in ejercicios:
        print("=" * 62)
        print(ej.__name__, "->", (inspect.getdoc(ej) or "").strip())
        try:
            print("    ", ej())
        except Exception as exc:
            print(f"     [ERROR] {type(exc).__name__}: {exc}")


PI = 3.14159


# --- SOLUCION 1: f-string de presentacion -----------------------------------
def ejercicio_1(nombre, edad, altura, estudiante):
    """
    Devuelve la presentacion de una persona con f-string.

    Entrada:  ejercicio_1("Ana", 25, 1.75, True)
    Salida:   "Ana (25 anios, 1.75 m) - estudiante: True"
    """
    # f-string: permite meter variables directamente dentro del texto
    return f"{nombre} ({edad} anios, {altura} m) - estudiante: {estudiante}"


# --- SOLUCION 2: tipo de cada variable --------------------------------------
def ejercicio_2():
    """
    Crea 4 variables y devuelve sus tipos separados por comas.

    Salida:   "str,int,float,bool"
    """
    texto = "uno"
    numero = 1
    decimal = 1.0
    activo = True

    # type(x).__name__ devuelve el nombre del tipo como texto: "str", "int"...
    return ",".join(
        [
            type(texto).__name__,
            type(numero).__name__,
            type(decimal).__name__,
            type(activo).__name__,
        ]
    )


# --- SOLUCION 3: conversion de tipos ---------------------------------------
def ejercicio_3(entero="123", decimal="45.6"):
    """
    Convierte dos textos a numero y devuelve la suma.

    Entrada:  ejercicio_3()        -> 168.6
    """
    # input() siempre devuelve texto, hay que convertirlo con int() / float()
    return int(entero) + float(decimal)


# --- SOLUCION 4: veracidad de un valor --------------------------------------
def ejercicio_4(valor):
    """
    Devuelve "si" o "no" segun la veracidad del valor.

    Pista: una constante vacia, 0, None o "" son "falsos" en Python.
    """
    # without if/elif/else: el ternario elige el texto segun la condicion
    return "si" if valor else "no"


# --- SOLUCION 5: area de un circulo -----------------------------------------
def ejercicio_5(radio):
    """
    Devuelve el area de un circulo, redondeada a 2 decimales.

    Entrada:  ejercicio_5(2)   -> 12.57
    """
    # area = PI * radio ** 2   (el ** tiene mas prioridad que el *)
    return round(PI * radio ** 2, 2)


# --- SOLUCION 6: intercambio sin variable auxiliar --------------------------
def ejercicio_6(a, b):
    """
    Intercambia a y b sin variable auxiliar.

    Entrada:  ejercicio_6(1, 2)  -> (2, 1)
    """
    # empaquetado multiple: la derecha se evalua ANTES de asignar
    return b, a


# --- SOLUCION 7: f-string multilinea ----------------------------------------
def ejercicio_7(nombre, edad, ciudad):
    """
    Devuelve un texto de 3 lineas.
    """
    return f"Nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}"


# --- SOLUCION 8: variable magica __name__ ----------------------------------
def ejercicio_8():
    """
    Devuelve True si el archivo se ejecuta como programa principal.
    """
    # solo dentro de la funcion queda False; en el modulo principal da True
    return __name__ == "__main__"


EJERCICIOS = [
    lambda: ejercicio_1("Ana", 25, 1.75, True),
    ejercicio_2,
    lambda: ejercicio_3(),
    lambda: ejercicio_4("hola"),
    lambda: ejercicio_4(0),
    lambda: ejercicio_5(2),
    lambda: ejercicio_6(1, 2),
    lambda: ejercicio_7("Ana", 25, "Madrid"),
    ejercicio_8,
]

if __name__ == "__main__":
    _main(EJERCICIOS)