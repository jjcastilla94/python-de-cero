"""
EJERCICIOS 01 - Variables y tipos de datos
==========================================
Objetivo:.refresh de variables, tipos basicos, conversion de tipos y f-strings.

COMO USAR
---------
1. Ejecuta el archivo:            python 01_variables_y_tipos.py
2. Cada funcion tiene "raise NotImplementedError" como aviso de pendiente.
3. Lee el comentario de cada funcion: indica que debe devolver.
4. Al terminar compara con:       soluciones/01_variables_y_tipos_solucion.py
"""

# Constante: por convencion las constantes van en MAYUSCULAS
PI = 3.14159


# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def ejercicio_1(nombre, edad, altura, estudiante):
    """
    Devuelve la presentacion de una persona con f-string.

    Entrada:  ejercicio_1("Ana", 25, 1.75, True)
    Salida:   "Ana (25 anios, 1.75 m) - estudiante: True"
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def ejercicio_2():
    """
    Crea 4 variables (texto="uno", numero=1, decimal=1.0, activo=True) y devuelve
    sus tipos separados por comas usando type(x).__name__.

    Salida:   "str,int,float,bool"
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def ejercicio_3(entero="123", decimal="45.6"):
    """
    Convierte dos textos a numero y devuelve la suma.

    Entrada:  ejercicio_3()        -> 168.6
    Pista:    int("123") y float("45.6")
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def ejercicio_4(valor):
    """
    Devuelve "si" o "no" segun la VERACIDAD del valor (no compares con True).

    Pista:    una constante vacia, 0, None o "" son "falsos" en Python.
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def ejercicio_5(radio):
    """
    Devuelve el area de un circulo, redondeada a 2 decimales.
    Usa la constante global PI y el operador de potencia.

    Entrada:  ejercicio_5(2)   -> 12.57
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def ejercicio_6(a, b):
    """
    Intercambia los valores de a y b SIN usar una variable auxiliar.
    Devuelve una tupla con los valores ya intercambiados.

    Entrada:  ejercicio_6(1, 2)  -> (2, 1)
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def ejercicio_7(nombre, edad, ciudad):
    """
    Devuelve un texto de 3 lineas (usa f-string con saltos de linea).

    Salida:
        Nombre: Ana
        Edad: 25
        Ciudad: Madrid
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def ejercicio_8():
    """
    Devuelve un booleano que diga si este archivo esta siendo ejecutado
    como programa principal.

    Pista:    la variable magica __name__ vale "__main__" al ejecutar el archivo.
    """
    raise NotImplementedError("TODO 8")


# --------------------------------------------------------------------------
# RUNNER: ejecuta todos los ejercicios y muestra el resultado o el error
# --------------------------------------------------------------------------
def _main(ejercicios):
    import inspect

    for ej in ejercicios:
        print("=" * 62)
        print(ej.__name__, "->", (inspect.getdoc(ej) or "").strip())
        try:
            print("    ", ej())
        except NotImplementedError:
            print("     [PENDIENTE] aun no lo has escrito")
        except Exception as exc:
            print(f"     [ERROR] {type(exc).__name__}: {exc}")


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