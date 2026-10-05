"""
SOLUCION 07 - Tuplas, diccionarios y conjuntos
==============================================
Verifica tu resultado ejecutando:
    python soluciones/07_tuplas_diccionarios_sets_solucion.py
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


# ==========================================================================
# PARTE A - TUPLAS
# ==========================================================================

def intercambio_tupla(a, b):
    """
    Intercambio con tupla (sin variable auxiliar).
    """
    # la tupla de la derecha se construye antes de desempaquetar
    return b, a


def dimensiones(matriz):
    """
    Devuelve (filas, columnas).
    """
    # len() de la lista exterior = filas; de la primera fila = columnas
    return len(matriz), len(matriz[0])


# ==========================================================================
# PARTE B - DICCIONARIOS
# ==========================================================================

def crear_contacto():
    """
    Crea y modifica un diccionario de contacto.
    """
    contacto = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Madrid",
        "email": "ana@mail.com",
    }
    contacto["telefono"] = "600111222"   # anadir clave
    contacto["edad"] = 26                # modificar valor
    del contacto["ciudad"]               # eliminar clave
    return contacto


def buscar_contacto(contactos, nombre):
    """
    Busca un email con .get() y valor por defecto.
    """
    # con [] saltaria KeyError si la clave no existe; .get() es seguro
    return contactos.get(nombre, "No encontrado")


def recorrer_contactos(contactos):
    """
    Devuelve (nombres ordenados, lista de "nombre <email>").
    """
    # items() devuelve pares (clave, valor) que se pueden desempaquetar
    datos = sorted(contactos.items())
    nombres = [nombre for nombre, _ in datos]
    tarjetas = [f"{nombre} <{email}>" for nombre, email in datos]
    return nombres, tarjetas


def inventario():
    """
    Resumen de un inventario.
    """
    stock = {"camiseta": 10, "pantalon": 5, "gorra": 3}

    # max() con key elige la clave (producto) con mayor valor (unidades)
    con_mas = max(stock, key=stock.get)

    return {
        "agregar": len(stock),                       # nº de productos
        "total": sum(stock.values()),                # unidades totales
        "mas_stock": con_mas,
        "agotados": [
            nombre
            for nombre, unidades in stock.items()
            if unidades == 0
        ],
    }


def fusionar_perfiles(perfil_base, perfil_extra):
    """
    Fusiona dos diccionarios en uno nuevo.
    """
    # {**a, **b} crea un diccionario nuevo; si una clave se repite,
    # gana el valor del segundo (b)
    return {**perfil_base, **perfil_extra}


# ==========================================================================
# PARTE C - CONJUNTOS
# ==========================================================================

def operaciones_conjuntos(a, b):
    """
    Operaciones entre conjuntos.
    """
    conjunto_a = set(a)
    conjunto_b = set(b)
    return (
        sorted(conjunto_a & conjunto_b),   # interseccion
        sorted(conjunto_a | conjunto_b),   # union
        sorted(conjunto_a - conjunto_b),   # diferencia
        sorted(conjunto_a ^ conjunto_b),   # simetrica
    )


def quitar_duplicados(lista):
    """
    Elimina duplicados y ordena.
    """
    return sorted(set(lista))


def son_unicos(lista):
    """
    True si no hay repetidos.
    """
    # el set no puede tener dos elementos iguales, asi que compara longitudes
    return len(lista) == len(set(lista))


def tablero():
    """
    Tuplas como claves de diccionario.
    """
    # (0, 0) es una tupla: sirve como clave porque es inmutable
    casillas = {
        (0, 0): "T",
        (0, 1): "P",
        (1, 0): "P",
        (1, 1): "T",
    }
    return (
        casillas[(0, 0)],
        casillas[(1, 1)],
        casillas.get((9, 9), "libre"),
    )


EJERCICIOS = [
    lambda: intercambio_tupla("x", "y"),
    lambda: dimensiones([[1, 2, 3], [4, 5, 6]]),
    crear_contacto,
    lambda: buscar_contacto({"Ana": "ana@mail.com"}, "Ana"),
    lambda: buscar_contacto({"Ana": "ana@mail.com"}, "Luis"),
    lambda: recorrer_contactos({"Luis": "l@mail.com", "Ana": "a@mail.com"}),
    inventario,
    lambda: fusionar_perfiles({"a": 1, "b": 2}, {"b": 3, "c": 4}),
    lambda: operaciones_conjuntos([1, 2, 3, 4], [3, 4, 5, 6]),
    lambda: quitar_duplicados([3, 1, 3, 2, 1]),
    lambda: son_unicos([1, 2, 3]),
    lambda: son_unicos([1, 2, 2]),
    tablero,
]

if __name__ == "__main__":
    _main(EJERCICIOS)