"""
EJERCICIOS 03 - Condicionales
=============================
Objetivo: if / elif / else, el operador ternario y la validacion de datos.

Ejecuta:  python 03_condicionales.py
Solucion: soluciones/03_condicionales_solucion.py
"""


# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def signo(numero):
    """
    Devuelve "positivo", "negativo" o "cero" segun el numero.
    Ojo: elif solo se evalua si la condicion anterior fue FALSA.
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def calificar(nota):
    """
    Convierte una nota numerica en letra:
        >= 90 -> "A"    >= 80 -> "B"    >= 70 -> "C"
        >= 60 -> "D"    en otro caso -> "F"
    Si la nota no esta entre 0 y 100 devuelve "nota invalida".
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def es_bisiesto(anio):
    """
    Un anio es bisiesto si es divisible entre 4 y NO entre 100,
    o si es divisible entre 400. Devuelve True o False.
    (2000 bisiesto, 1900 no, 2024 si, 2023 no)
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def paridad(numero):
    """
    Devuelve "par" o "impar" usando el operador TERNARIO (una sola linea):
        "resultado_si_true" if condicion else "resultado_si_false"
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def validar_password(password):
    """
    Devuelve la LISTA de requisitos que NO cumple la contrasena:
        - al menos 8 caracteres
        - al menos una mayuscula
        - al menos una minuscula
        - al menos un digito
    Si no falla nada devuelve [] (una contrasena valida).
    Entrada:  validar_password("abc")      -> ["longitud", "mayuscula", "digito"]
              validar_password("Abcdefg1") -> []
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def fizzbuzz(n):
    """
    Devuelve una lista de strings con los numeros del 1 al n, aplicando:
        - divisible por 3 y 5 -> "FizzBuzz"
        - divisible por 3     -> "Fizz"
        - divisible por 5     -> "Buzz"
        - en otro caso        -> el numero como texto
    Importante: el "if" del caso mas especifico va PRIMERO.
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def tipo_triangulo(a, b, c):
    """
    Devuelve:
        "no es triangulo"  si no cumple la desigualdad triangular (a+b>c, etc.)
        "equilatero"        si los 3 lados son iguales
        "isosceles"         si exactamente 2 lados son iguales
        "escaleno"          si todos son distintos
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def clasificar_valor(valor):
    """
    Clasifica un valor usando un if-elif-else SOLO, sin operadores logicos
    (and, or). Devuelve:
        "vacio"    si el valor es "" , [] , {} o None
        "numero"   si es int o float
        "texto"    si es str con contenido
        "otro"     en cualquier otro caso
    Pista: un "in" con una tupla de valores vacios te permite evitar el "or".
    """
    raise NotImplementedError("TODO 8")


def _main(ejercicios):
    import inspect

    for ej in ejercicios:
        print("=" * 62)
        print(getattr(ej, "__name__", "lambda"), "->", (inspect.getdoc(ej) or "").strip())
        try:
            print("    ", ej())
        except NotImplementedError:
            print("     [PENDIENTE] aun no lo has escrito")
        except Exception as exc:
            print(f"     [ERROR] {type(exc).__name__}: {exc}")


EJERCICIOS = [
    lambda: signo(7),
    lambda: signo(0),
    lambda: calificar(85),
    lambda: calificar(120),
    lambda: es_bisiesto(2024),
    lambda: es_bisiesto(1900),
    lambda: paridad(4),
    lambda: validar_password("abc"),
    lambda: validar_password("Abcdefg1"),
    lambda: fizzbuzz(15),
    lambda: tipo_triangulo(3, 3, 3),
    lambda: tipo_triangulo(3, 3, 5),
    lambda: tipo_triangulo(1, 2, 10),
    lambda: clasificar_valor(""),
    lambda: clasificar_valor(5),
    lambda: clasificar_valor("hola"),
]

if __name__ == "__main__":
    _main(EJERCICIOS)