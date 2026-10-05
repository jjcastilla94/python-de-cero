"""
EJERCICIOS 02 - Operadores
==========================
Objetivo: operadores aritmeticos, de asignacion, de comparacion, logicos,
de pertenencia e identidad.

Ejecuta:  python 02_operadores.py
Solucion: soluciones/02_operadores_solucion.py
"""


# --------------------------------------------------------------------------
# EJERCICIO 1 - Aritmeticos
# --------------------------------------------------------------------------
def ejercicio_1(a, b):
    """
    Devuelve una tupla con TODOS los resultados aritmeticos entre a y b, en
    este orden: suma, resta, producto, division real, division entera,
    modulo (resto) y potencia.

    Entrada:  ejercicio_1(7, 2)  -> (9, 5, 14, 3.5, 3, 1, 49)
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2 - De asignacion
# --------------------------------------------------------------------------
def ejercicio_2():
    """
    Partiendo de x = 10 aplica, en este orden y sobre la MISMA variable:
        x += 5    x -= 3    x *= 2    x /= 4    x //= 2    x %= 2    x **= 3
    y devuelve el valor final de x.

    Salida:   1.0
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3 - De comparacion
# --------------------------------------------------------------------------
def ejercicio_3(a, b):
    """
    Devuelve una tupla con los 6 resultados de comparacion en este orden:
    igual (==), distinto (!=), mayor (>), mayor o igual (>=),
    menor (<), menor o igual (<=).

    Entrada:  ejercicio_3(5, 5) -> (True, False, False, True, False, True)
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4 - Logicos
# --------------------------------------------------------------------------
def ejercicio_4(edad, tiene_permiso):
    """
    Reglas de acceso a un club:
      - entra si es mayor de 18 Y tiene permiso
      - entra siempre si es mayor de 65 (pensionista)
    Devuelve True o False usando and / or / not.
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5 - Pertenencia
# --------------------------------------------------------------------------
def ejercicio_5(texto):
    """
    Devuelve una tupla con:
      - True si la letra "a" esta en el texto
      - True si "python" esta en el texto (comprueba sin distinguir mayusculas)
      - el numero de veces que aparece la letra "a" (minusculas)
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6 - Identidad
# --------------------------------------------------------------------------
def ejercicio_6():
    """
    Crea a = [1, 2]; b = a; c = [1, 2] y devuelve una tupla con:
      - (a is b)   -> misma referencia?
      - (a is c)   -> misma referencia?
      - (a == c)   -> mismo valor?
    Salida:   (True, False, True)
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7 - Prioridad de operadores
# --------------------------------------------------------------------------
def ejercicio_7():
    """
    Devuelve el resultado de:  2 + 3 * 4 ** 2 - (10 // 3) % 2
    No hagas el calculo a mano: escribe la expresion en Python y observa.
    Salida:   49
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8 - Cadena con operadores
# --------------------------------------------------------------------------
def ejercicio_8(nombre, veces=1):
    """
    Repite el nombre "nombre" el numero de veces indicado, separando las
    repeticiones con comas, usando el operador de multiplicacion de str.

    Entrada:  ejercicio_8("Ana", 3)  -> "Ana, Ana, Ana"
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
    lambda: ejercicio_1(7, 2),
    ejercicio_2,
    lambda: ejercicio_3(5, 5),
    lambda: ejercicio_4(70, False),
    lambda: ejercicio_4(20, False),
    lambda: ejercicio_5("Hola python"),
    ejercicio_6,
    ejercicio_7,
    lambda: ejercicio_8("Ana", 3),
]

if __name__ == "__main__":
    _main(EJERCICIOS)