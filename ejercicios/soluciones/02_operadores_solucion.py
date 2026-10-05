"""
SOLUCION 02 - Operadores
========================
Verifica tu resultado ejecutando:
    python soluciones/02_operadores_solucion.py
"""


def _main(ejercicios):
    import inspect

    for ej in ejercicios:
        print("=" * 62)
        print(getattr(ej, "__name__", "lambda"), "->", (inspect.getdoc(ej) or "").strip())
        try:
            print("    ", ej())
        except Exception as exc:
            print(f"     [ERROR] {type(exc).__name__}: {exc}")


# --- SOLUCION 1: aritmeticos ------------------------------------------------
def ejercicio_1(a, b):
    """
    Todos los resultados aritmeticos entre a y b.

    Entrada:  ejercicio_1(7, 2)  -> (9, 5, 14, 3.5, 3, 1, 49)
    """
    # OJO: / siempre da float (7/2 = 3.5); // es division entera (7//2 = 3)
    #      % es el resto; ** es potencia (7 ** 2 = 49)
    return (a + b, a - b, a * b, a / b, a // b, a % b, a ** b)


# --- SOLUCION 2: asignacion -------------------------------------------------
def ejercicio_2():
    """
    x = 10 y todas las asignaciones en cadena.

    Salida:   1.0
    """
    x = 10
    x += 5    # 15
    x -= 3    # 12
    x *= 2    # 24
    x /= 4    # 6.0
    x //= 2   # 3.0
    x %= 2    # 1.0
    x **= 3   # 1.0
    # desde x /= 4 en adelante x es float, por eso el resultado es 1.0
    return x


# --- SOLUCION 3: comparacion ------------------------------------------------
def ejercicio_3(a, b):
    """
    Los 6 operadores de comparacion.

    Entrada:  ejercicio_3(5, 5) -> (True, False, False, True, False, True)
    """
    # Cada comparacion devuelve un bool, y una tupla puede contener bools
    return (a == b, a != b, a > b, a >= b, a < b, a <= b)


# --- SOLUCION 4: logicos ----------------------------------------------------
def ejercicio_4(edad, tiene_permiso):
    """
    Acceso: mayor de 18 con permiso, o siempre mayor de 65.
    """
    # se agrupa con parentesis para dejar claro el orden de evaluacion
    return (edad >= 18 and tiene_permiso) or edad >= 65


# --- SOLUCION 5: pertenencia ------------------------------------------------
def ejercicio_5(texto):
    """
    Pertenencia con in / not in y conteo con .count().
    """
    minusculas = texto.lower()
    return (
        "a" in minusculas,          # True si esta contenida
        "python" in minusculas,     # comparacion sin mayusculas
        minusculas.count("a"),      # cuantas veces aparece
    )


# --- SOLUCION 6: identidad --------------------------------------------------
def ejercicio_6():
    """
    is compara identidad (referencia), == compara valor.

    Salida:   (True, False, True)
    """
    a = [1, 2]
    b = a      # b APUNTA al mismo objeto que a
    c = [1, 2]  # c es otro objeto con el mismo valor
    return (a is b, a is c, a == c)


# --- SOLUCION 7: prioridad --------------------------------------------------
def ejercicio_7():
    """
    Prioridad: **  >  //, %  >  *  >  +, -
    """
    # 2 + 3*16 - 1 = 2 + 48 - 1 = 49
    return 2 + 3 * 4 ** 2 - (10 // 3) % 2


# --- SOLUCION 8: multiplicacion de cadenas ---------------------------------
def ejercicio_8(nombre, veces=1):
    """
    "Ana" * 3 = "AnaAnaAna" -> solo hay que unir con comas.

    Entrada:  ejercicio_8("Ana", 3)  -> "Ana, Ana, Ana"
    """
    # join convierte la tupla/lista de partes en un unico string
    return ", ".join([nombre] * veces)


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