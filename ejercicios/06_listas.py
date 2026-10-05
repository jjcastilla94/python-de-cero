"""
EJERCICIOS 06 - Listas
======================
Objetivo: crear, modificar, recorrer y transformar listas; metodos utiles;
comprensiones de listas; copia vs referencia.

Ejecuta:  python 06_listas.py
Solucion: soluciones/06_listas_solucion.py
"""


# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def construir_notas():
    """
    Devuelve la lista resultante de esta secuencia de pasos:
        1. lista vacia
        2. anade 5, 7, 3      (append)
        3. inserta 9 al inicio (insert)
        4. anade 8 al final
        5. elimina el 7        (remove)
        6. quita el ultimo elemento con pop() y guardalo en una variable
    Salida esperada: la tupla ([9, 5, 3], 8)
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def estadisticas(lista):
    """
    Devuelve un diccionario con las claves "suma", "media", "minimo",
    "maximo", "ordenada" (de menor a mayor) y "longitud".
    Si la lista esta vacia, "media" debe ser 0.
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def sin_duplicados(lista):
    """
    Elimina duplicados CONSERVANDO EL ORDEN de la primera aparicion.
    Entrada:  sin_duplicados([3, 1, 3, 2, 1]) -> [3, 1, 2]
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def comprensiones():
    """
    Devuelve una tupla con tres listas creadas con COMPRENSION:
        pares      -> [0, 2, 4, 6, 8]           (numeros pares de 0 a 9)
        cuadrados  -> [0, 1, 4, 9, 16, 25]     (cuadrados de 0 a 5)
        dobles     -> ["ABAB", "CDCD"]          (cada texto repetido 2 veces)
                      a partir de ["ab", "cd"]
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def fusionar_ordenadas(a, b):
    """
    Fusiona dos listas YA ORDENADAS en una sola lista ordenada, sin usar
    sort(). Pista: dos indices que avanzan comparando elementos.
    Entrada:  fusionar_ordenadas([1, 3, 5], [2, 4]) -> [1, 2, 3, 4, 5]
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def transponer(matriz):
    """
    Convierte una matriz de filas en una de columnas.
    Entrada:  transponer([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def copia_vs_referencia():
    """
    Demuestra la diferencia entre COPIAR y REFERENCIAR:
        original = [1, 2, 3]
        copia    = original.copy()
        misma    = original            # misma referencia
        anade 4 a las tres
    Devuelve la tupla (original, copia, misma)
    Salida:  ([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4])
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def procesar(notas):
    """
    Devuelve una lista con las notas aprobadas (>= 5) expressadas como
    texto ("Aprobado: 7"), usando enumerate y una comprension.
    Entrada:  procesar([3, 7, 5.5, 2]) -> ["Aprobado: 7", "Aprobado: 5.5"]
    """
    raise NotImplementedError("TODO 8")


# --------------------------------------------------------------------------
# EJERCICIO 9
# --------------------------------------------------------------------------
def segundo_mayor(lista):
    """
    Devuelve el segundo valor mas alto (sin repetir). Si no hay al menos
    dos valores distintos, devuelve None.
    Entrada:  segundo_mayor([3, 9, 9, 1]) -> 3
    """
    raise NotImplementedError("TODO 9")


# --------------------------------------------------------------------------
# EJERCICIO 10
# --------------------------------------------------------------------------
def aplanar(lista):
    """
    Convierte una lista de listas en una lista plana (una sola dimension).
    Entrada:  aplanar([[1, 2], [3], [4, 5]]) -> [1, 2, 3, 4, 5]
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
    construir_notas,
    lambda: estadisticas([4, 8, 2]),
    lambda: estadisticas([]),
    lambda: sin_duplicados([3, 1, 3, 2, 1]),
    comprensiones,
    lambda: fusionar_ordenadas([1, 3, 5], [2, 4]),
    lambda: transponer([[1, 2, 3], [4, 5, 6]]),
    copiar_vs_referencia,
    lambda: procesar([3, 7, 5.5, 2]),
    lambda: segundo_mayor([3, 9, 9, 1]),
    lambda: aplanar([[1, 2], [3], [4, 5]]),
]

if __name__ == "__main__":
    _main(EJERCICIOS)