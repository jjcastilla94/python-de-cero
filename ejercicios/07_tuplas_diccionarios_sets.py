"""
EJERCICIOS 07 - Tuplas, diccionarios y conjuntos
===============================================
Objetivo: agrupar datos con clave (diccionario), datos fijos (tupla) y
eliminar duplicados / comparar colecciones (set).

Ejecuta:  python 07_tuplas_diccionarios_sets.py
Solucion: soluciones/07_tuplas_diccionarios_sets_solucion.py
"""


# ==========================================================================
# PARTE A - TUPLAS (inmutables)
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def intercambio_tupla(a, b):
    """
    Intercambia dos valores usando una tupla y devuelve la tupla nueva.
    Entrada:  intercambio_tupla("x", "y") -> ("y", "x")
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def dimensiones(matriz):
    """
    Devuelve la tupla (filas, columnas) de una matriz de listas.
    Entrada:  dimensiones([[1, 2, 3], [4, 5, 6]]) -> (2, 3)
    Pista:    una tupla es inmutable: NO admite append ni asignacion por
              indice. Por eso sus elementos se calculan antes de crearla.
    """
    raise NotImplementedError("TODO 2")


# ==========================================================================
# PARTE B - DICCIONARIOS (clave: valor)
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def crear_contacto():
    """
    Crea un diccionario con estos datos:
        nombre  -> "Ana"
        edad    -> 25
        ciudad  -> "Madrid"
        email   -> "ana@mail.com"
    Devuelve el diccionario DESPUES de:
        - anadir la clave "telefono" con valor "600111222"
        - subir la edad a 26
        - eliminar la clave "ciudad"
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def buscar_contacto(contactos, nombre):
    """
    contactos es un diccionario {nombre: email}.
    Devuelve el email si existe y "No encontrado" si no.
    Usa .get() con valor por defecto (NO accedas con corchetes: darian error).
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def recorrer_contactos(contactos):
    """
    Devuelve DOS listas: los nombres ordenados alfabeticamente y una lista
    de textos "nombre <email>" ordenados por nombre.
    Usa .items(), .keys(), list() y sorted().
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def inventario():
    """
    Crea un inventario: {"camiseta": 10, "pantalon": 5, "gorra": 3}
    y devuelve un diccionario con:
        "agregar"   numero de productos distintos
        "total"     unidades totales
        "mas_stock" nombre del producto con mas unidades
        "agotados"  lista de productos con 0 unidades
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def fusionar_perfiles(perfil_base, perfil_extra):
    """
    Fusiona dos diccionarios en uno nuevo (sin modificar los originales)
    y devuelve el resultado. Las claves repetidas se quedan con el valor
    del segundo diccionario.
    Pista: {**dic1, **dic2}
    """
    raise NotImplementedError("TODO 7")


# ==========================================================================
# PARTE C - CONJUNTOS (sets)
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def operaciones_conjuntos(a, b):
    """
    a y b son listas. Conviertelas a sets y devuelve una tupla con cuatro
    listas ORDENADAS:
        interseccion   (a & b)   elementos comunes
        union          (a | b)   todos sin repetir
        diferencia     (a - b)   los de a que no estan en b
        solo_a         (a ^ b)   los que estan en uno solo
    """
    raise NotImplementedError("TODO 8")


# --------------------------------------------------------------------------
# EJERCICIO 9
# --------------------------------------------------------------------------
def quitar_duplicados(lista):
    """
    Elimina duplicados de una lista y devuelve una lista ordenada.
    Entrada:  quitar_duplicados([3, 1, 3, 2, 1]) -> [1, 2, 3]
    """
    raise NotImplementedError("TODO 9")


# --------------------------------------------------------------------------
# EJERCICIO 10
# --------------------------------------------------------------------------
def son_unicos(lista):
    """
    Devuelve True si la lista NO tiene elementos repetidos.
    Pista: compara la longitud de la lista con la de su set.
    """
    raise NotImplementedError("TODO 10")


# --------------------------------------------------------------------------
# EJERCICIO 11
# --------------------------------------------------------------------------
def tablero():
    """
    Usa una TUPLA como clave de un diccionario para representar las
    coordenadas de un tablero de ajedrez 2x2.
    Crea el diccionario:
        {(0,0): "T", (0,1): "P", (1,0): "P", (1,1): "T"}
        (T = torre, P = peon)
    Devuelve la tupla: (valor_de_(0,0), valor_de_(1,1), "libre" en (9,9))
    Salida:  ("T", "T", "libre")
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