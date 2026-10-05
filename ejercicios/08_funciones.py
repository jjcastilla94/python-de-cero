"""
EJERCICIOS 08 - Funciones
=========================
Objetivo: definir funciones, parametros por defecto, *args, **kwargs,
retornos multiples, recursividad, lambdas, map/filter/reduce y ambito.

Ejecuta:  python 08_funciones.py
Solucion: soluciones/08_funciones_solucion.py
"""


# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def saludar(nombre, saludo="Hola"):
    """
    Devuelve un saludo.
    Entrada:  saludar("Ana")                 -> "Hola, Ana!"
              saludar("Ana", saludo="Buenas") -> "Buenas, Ana!"
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def sumar_todos(*numeros):
    """
    Suma todos los numeros recibidos (pueden ser 0, 1 o muchos).
    Entrada:  sumar_todos(1, 2, 3)  -> 6
              sumar_todos()         -> 0
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def construir_usuario(nombre, **campos):
    """
    Devuelve un diccionario con "nombre" mas todos los campos extra
    que se pasen por palabra clave.
    Entrada:  construir_usuario("Ana", email="a@b.com", edad=25)
              -> {"nombre": "Ana", "email": "a@b.com", "edad": 25}
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def minimo_y_maximo(lista):
    """
    Devuelve los dos valores en una sola llamada mediante un retorno
    multiple (se desempaquetan con  a, b = minimo_y_maximo(...) ).
    Entrada:  minimo_y_maximo([4, 9, 2]) -> (2, 9)
    Si la lista esta vacia devuelve (None, None).
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def factorial(n):
    """
    Factorial con RECURSION: la funcion se llama a si misma.
    factorial(5) -> 120
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def fibonacci(cantidad):
    """
    Devuelve una lista con los "cantidad" primeros numeros de Fibonacci.
    fibonacci(7) -> [0, 1, 1, 2, 3, 5, 8]
    Pista: un solo bucle es mas eficiente, pero aqui se pide recursion.
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def con_funciones_de_orden_superior():
    """
    Devuelve un diccionario con:
        "dobles"     -> [2, 4, 6]          con map()
        "mayores_10" -> [12, 15]           con filter()
        "suma"       -> 10                 con reduce()
    Partiendo siempre de la lista [1, 2, 3, 4, 5] y usando lambdas.
    Importa reduce de functools.
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def dividir(a, b):
    """
    Devuelve la division de a entre b, pero:
        - si b es 0, lanza ZeroDivisionError con un mensaje claro
        - si a o b no son numeros, lanza TypeError
    """
    raise NotImplementedError("TODO 8")


# --------------------------------------------------------------------------
# EJERCICIO 9
# --------------------------------------------------------------------------
def promedio(notas):
    """
    Devuelve la media de las notas; si la lista esta vacia devuelve 0.
    """
    raise NotImplementedError("TODO 9")


# --------------------------------------------------------------------------
# EJERCICIO 10
# --------------------------------------------------------------------------
def contador(texto):
    """
    Devuelve un diccionario con cuantas veces sale cada letra (sin contar
    los espacios).
    Entrada:  contador("hola") -> {"h": 1, "o": 1, "l": 1, "a": 1}
    """
    raise NotImplementedError("TODO 10")


# --------------------------------------------------------------------------
# EJERCICIO 11
# --------------------------------------------------------------------------
def aplicar_funcion(funcion, valores):
    """
    funcion de orden superior: recibe OTRA funcion y la aplica a cada
    elemento de "valores", devolviendo una lista con los resultados.
    """
    raise NotImplementedError("TODO 11")


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
    lambda: saludar("Ana"),
    lambda: saludar("Ana", saludo="Buenas"),
    lambda: sumar_todos(1, 2, 3),
    lambda: sumar_todos(),
    lambda: construir_usuario("Ana", email="a@b.com", edad=25),
    lambda: minimo_y_maximo([4, 9, 2]),
    lambda: minimo_y_maximo([]),
    lambda: factorial(5),
    lambda: fibonacci(7),
    con_funciones_de_orden_superior,
    lambda: dividir(10, 2),
    lambda: promedio([8, 6]),
    lambda: promedio([]),
    lambda: contador("hola"),
    lambda: aplicar_funcion(lambda x: x ** 2, [1, 2, 3]),
]

if __name__ == "__main__":
    _main(EJERCICIOS)