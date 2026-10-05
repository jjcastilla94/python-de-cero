"""
SOLUCION 06 - Listas
====================
Verifica tu resultado ejecutando:
    python soluciones/06_listas_solucion.py
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


# --- SOLUCION 1 -------------------------------------------------------------
def construir_notas():
    """
    Construye y modifica una lista paso a paso.
    """
    notas = []
    notas.append(5)          # [5]
    notas.append(7)          # [5, 7]
    notas.append(3)          # [5, 7, 3]
    notas.insert(0, 9)       # [9, 5, 7, 3]
    notas.append(8)          # [9, 5, 7, 3, 8]
    notas.remove(7)          # [9, 5, 3, 8]
    ultimo = notas.pop()     # pop() quita y DEVUELVE el ultimo
    return notas, ultimo     # ([9, 5, 3], 8)


# --- SOLUCION 2 -------------------------------------------------------------
def estadisticas(lista):
    """
    Diccionario con los datos basicos de una lista.
    """
    # sorted() devuelve una copia ordenada (NO modifica la original)
    # min()/max() de una lista vacia dan error, por eso se comprueba antes
    return {
        "suma": sum(lista),
        "media": round(sum(lista) / len(lista), 2) if lista else 0,
        "minimo": min(lista) if lista else 0,
        "maximo": max(lista) if lista else 0,
        "ordenada": sorted(lista),
        "longitud": len(lista),
    }


# --- SOLUCION 3 -------------------------------------------------------------
def sin_duplicados(lista):
    """
    Quita duplicados conservando el orden (sin usar set).
    """
    resultado = []
    for elemento in lista:
        if elemento not in resultado:   # "not in" evita el duplicado
            resultado.append(elemento)
    return resultado


# --- SOLUCION 4 -------------------------------------------------------------
def comprensiones():
    """
    Tres comprensiones de lista.
    """
    # sintaxis: [expresion for variable in secuencia if condicion]
    pares = [i for i in range(10) if i % 2 == 0]
    cuadrados = [i ** 2 for i in range(6)]
    dobles = [texto * 2 for texto in ["ab", "cd"]]
    return pares, cuadrados, dobles


# --- SOLUCION 5 -------------------------------------------------------------
def fusionar_ordenadas(a, b):
    """
    Fusiona dos listas ordenadas con dos indices.
    """
    resultado = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        # se mete el menor de los dos y se avanza solo en esa lista
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    # lo que quede de cada lista se anade al final (extend)
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


# --- SOLUCION 6 -------------------------------------------------------------
def transponer(matriz):
    """
    Cambia filas por columnas.
    """
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]


# --- SOLUCION 7 -------------------------------------------------------------
def copia_vs_referencia():
    """
    copy() crea una lista nueva; sin copy() se comparte la misma referencia.
    """
    original = [1, 2, 3]
    copia = original.copy()   # lista independiente
    misma = original           # MISMA referencia

    copia.append(4)
    # al hacer append en "misma" tambien cambia "original" (son el mismo objeto)
    misma.append(4)

    return original, copia, misma


# --- SOLUCION 8 -------------------------------------------------------------
def procesar(notas):
    """
    Notas aprobadas con su indice.
    """
    return [
        f"Aprobado: {nota}"
        for nota in notas
        if nota >= 5
    ]


# --- SOLUCION 9 -------------------------------------------------------------
def segundo_mayor(lista):
    """
    Segundo valor mas alto sin repetir.
    """
    distintos = sorted(set(lista), reverse=True)   # set quita repetidos
    if len(distintos) < 2:
        return None
    return distintos[1]


# --- SOLUCION 10 ------------------------------------------------------------
def aplanar(lista):
    """
    Aplana una lista de listas en una sola dimension.
    """
    return [elemento for sublista in lista for elemento in sublista]
    # dos for seguidos: primero recorre las sublistas, luego sus elementos


EJERCICIOS = [
    construir_notas,
    lambda: estadisticas([4, 8, 2]),
    lambda: estadisticas([]),
    lambda: sin_duplicados([3, 1, 3, 2, 1]),
    comprensiones,
    lambda: fusionar_ordenadas([1, 3, 5], [2, 4]),
    lambda: transponer([[1, 2, 3], [4, 5, 6]]),
    copia_vs_referencia,
    lambda: procesar([3, 7, 5.5, 2]),
    lambda: segundo_mayor([3, 9, 9, 1]),
    lambda: aplanar([[1, 2], [3], [4, 5]]),
]

if __name__ == "__main__":
    _main(EJERCICIOS)