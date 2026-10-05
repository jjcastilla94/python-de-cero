"""
EJERCICIOS 05 - Cadenas de texto (strings)
=========================================
Objetivo: indexacion, rebanadas (slicing), metodos de str y f-strings.

Ejecuta:  python 05_cadenas.py
Solucion: soluciones/05_cadenas_solucion.py
"""


# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def normalizar(texto):
    """
    Limpia un texto: quita espacios sobrantes, pasa a minusculas y
    une las palabras con un solo espacio.
    Entrada:  normalizar("  Hola   MUNDO  ")  -> "hola mundo"
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def contar_palabras(texto):
    """
    Devuelve un DICCIONARIO {palabra: veces} sin distinguir mayusculas.
    Entrada:  contar_palabras("hola Hola mundo")
              -> {"hola": 2, "mundo": 1}
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def es_palindromo(texto):
    """
    Devuelve True si el texto se lee igual del derecho y del revés,
    ignorando espacios, mayusculas y signos.
    Entrada:  es_palindromo("Anita lava la tina") -> True
              es_palindromo("python") -> False
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def slug(texto):
    """
    Convierte un titulo en un "slug" para URL: minusculas, espacios por
    guiones y sin signos.
    Entrada:  slug("Python Basico 2026!")  -> "python-basico-2026"
    """
    raise NotImplementedError("TODO 4")


# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def capitalizar(texto):
    """
    Pone en mayuscula la primera letra de cada palabra.
    Entrada:  capitalizar("hola MUNDO")  -> "Hola Mundo"
    Pista:    existe el metodo title() ... pero solo con palabras minusculas.
              Si el texto llega en minusculas, title() vale.
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def separar(texto, n=3):
    """
    Parte el texto en trozos de "n" caracteres unidos por guiones.
    Entrada:  separar("abcdefgh", 3)  -> "abc-def-gh"
    Pista:    rebanada [inicio:fin:salto] y range(0, len(texto), n).
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def iniciales(nombre_completo):
    """
    Devuelve las iniciales en mayusculas.
    Entrada:  iniciales("juan perez gomez")  -> "JPG"
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def slicing(texto):
    """
    Devuelve una tupla con estos recortes de "texto":
        texto[0]      primera letra
        texto[-1]     ultima letra
        texto[:3]     las 3 primeras
        texto[-3:]    las 3 ultimas
        texto[::-1]   el texto invertido
        texto[1::2]   desde la 2a letra, de 2 en 2
    """
    raise NotImplementedError("TODO 8")


# --------------------------------------------------------------------------
# EJERCICIO 9
# --------------------------------------------------------------------------
def es_vocal(caracter):
    """
    Devuelve True si el caracter (mayuscula o minuscula) es una vocal.
    """
    raise NotImplementedError("TODO 9")


# --------------------------------------------------------------------------
# EJERCICIO 10
# --------------------------------------------------------------------------
def contiene(texto, palabra):
    """
    Devuelve una tupla con:
        - texto.startswith(palabra)        empieza por la palabra
        - texto.endswith(palabra)          termina con la palabra
        - palabra in texto                la contiene
        - texto.find(palabra)             indice de la palabra (-1 si no esta)
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
    lambda: normalizar("  Hola   MUNDO  "),
    lambda: contar_palabras("hola Hola mundo"),
    lambda: es_palindromo("Anita lava la tina"),
    lambda: es_palindromo("python"),
    lambda: slug("Python Basico 2026!"),
    lambda: capitalizar("hola mundo"),
    lambda: separar("abcdefgh", 3),
    lambda: iniciales("juan perez gomez"),
    lambda: slicing("Python"),
    lambda: es_vocal("a"),
    lambda: es_vocal("Z"),
    lambda: contiene("Python es guay", "guay"),
]

if __name__ == "__main__":
    _main(EJERCICIOS)