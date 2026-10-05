"""
EJERCICIOS 04 - Bucles
======================
Objetivo: for, while, range(), enumerate, zip, break, continue y for-else.

Ejecuta:  python 04_bucles.py
Solucion: soluciones/04_bucles_solucion.py
"""


# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def sumar_hasta(n):
    """
    Suma los numeros del 1 al n con un bucle for y devuelve el total.

    Entrada:  sumar_hasta(100) -> 5050
    Pista:    range(1, n + 1) para incluir el n.
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def tabla_multiplicar(n, limite=10):
    """
    Devuelve una lista de strings con la tabla de multiplicar de n
    (hasta "limite"), en formato "3 x 1 = 3", "3 x 2 = 6"...
    Usa bucles anidados (un for dentro de otro).
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def cuenta_atras_saltando(n):
    """
    Devuelve una lista con los numeros desde n hasta 1, pero SALTANDO los
    multiplos de 3 (usa continue).
    Entrada:  cuenta_atras_saltando(10) -> [10, 8, 7, 5, 4, 2, 1]
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def primer_primo(desde):
    """
    Devuelve el primer numero primo MAYOR O IGUAL que "desde", usando
    for + break. Si no hay ninguno en los siguientes 100 numeros,
    devuelve None.
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def variantes_de_range():
    """
    Devuelve una tupla con tres listas:
        list(range(0, 10, 2))   -> pares del 0 al 8
        list(range(5, 0, -1))   -> 5,4,3,2,1
        list(range(2, 6))       -> 2,3,4,5
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def numerar_elementos(lista):
    """
    Devuelve una lista de strings "1. Ana", "2. Luis"... usando enumerate.
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def buscar_elemento(lista, objetivo):
    """
    Devuelve True si encuentra "objetivo" en la lista usando la estructura
    for ... else (el else se ejecuta solo si el bucle NO se rompio con break).
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def suma_digitos(numero):
    """
    Suma las cifras de un numero entero usando while y la division entera.
    Ejemplo: suma_digitos(1234) -> 10
    """
    raise NotImplementedError("TODO 8")


# --------------------------------------------------------------------------
# EJERCICIO 9
# --------------------------------------------------------------------------
def cruzar_listas(nombres, edades):
    """
    Devuelve una lista de textos "Ana:25" combinando dos listas con zip.
    Si las listas tienen distinta longitud, se queda con la mas corta.
    """
    raise NotImplementedError("TODO 9")


# --------------------------------------------------------------------------
# EJERCICIO 10
# --------------------------------------------------------------------------
def piramide(altura):
    """
    Devuelve una lista de strings con una piramide de asteriscos:
    piramide(4) -> ["*", "**", "***", "****"]
    (se puede hacer multiplicando "*" por i)
    """
    raise NotImplementedError("TODO 10")


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
    lambda: sumar_hasta(100),
    lambda: tabla_multiplicar(3, 4),
    lambda: cuenta_atras_saltando(10),
    lambda: primer_primo(14),
    variantes_de_range,
    lambda: numerar_elementos(["Ana", "Luis", "Eva"]),
    lambda: buscar_elemento(["a", "b", "c"], "b"),
    lambda: buscar_elemento(["a", "b", "c"], "z"),
    lambda: suma_digitos(1234),
    lambda: cruzar_listas(["Ana", "Luis"], [25, 30]),
    lambda: piramide(4),
]

if __name__ == "__main__":
    _main(EJERCICIOS)