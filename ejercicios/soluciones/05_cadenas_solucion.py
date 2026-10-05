"""
SOLUCION 05 - Cadenas de texto (strings)
========================================
Verifica tu resultado ejecutando:
    python soluciones/05_cadenas_solucion.py
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
def normalizar(texto):
    """
    Limpia un texto.
    """
    # split() sin argumentos parte por cualquier cantidad de espacios
    # join() vuelve a unir con un unico espacio
    return " ".join(texto.lower().split())


# --- SOLUCION 2 -------------------------------------------------------------
def contar_palabras(texto):
    """
    Diccionario {palabra: veces} en minusculas.
    """
    conteo = {}
    for palabra in texto.lower().split():
        # si la palabra no existe, dict.get la crea con valor 0
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


# --- SOLUCION 3 -------------------------------------------------------------
def es_palindromo(texto):
    """
    Palindromo ignorando espacios, mayusculas y signos.
    """
    # isalpha() filtra solo letras: asi se ignoran espacios, signos y numeros
    limpio = "".join(c for c in texto.lower() if c.isalpha())
    return limpio == limpio[::-1]   # comparar con su inverso


# --- SOLUCION 4 -------------------------------------------------------------
def slug(texto):
    """
    Convierte un titulo en slug.
    """
    limpio = texto.lower()
    # reemplaza cada caracter no alfanumerico por un guion
    limpio = "".join(c if c.isalnum() else "-" for c in limpio)
    # si quedaron guiones seguidos o al principio/final, se limpian
    while "--" in limpio:
        limpio = limpio.replace("--", "-")
    return limpio.strip("-")


# --- SOLUCION 5 -------------------------------------------------------------
def capitalizar(texto):
    """
    Mayuscula en cada palabra.
    """
    return texto.lower().title()


# --- SOLUCION 6 -------------------------------------------------------------
def separar(texto, n=3):
    """
    Trocea el texto en trozos de n caracteres unidos por guiones.
    """
    trozos = [texto[i:i + n] for i in range(0, len(texto), n)]
    return "-".join(trozos)


# --- SOLUCION 7 -------------------------------------------------------------
def iniciales(nombre_completo):
    """
    Iniciales en mayusculas.
    """
    # comprehension: coge la primera letra de cada palabra y la pasa a mayuscula
    return "".join(palabra[0].upper() for palabra in nombre_completo.split())


# --- SOLUCION 8 -------------------------------------------------------------
def slicing(texto):
    """
    Todos los recortes pedidos.
    """
    return (
        texto[0],       # 1er caracter
        texto[-1],      # ultimo (los negativos cuentan desde atras)
        texto[:3],      # desde el inicio hasta 3 (sin incluir el 3)
        texto[-3:],     # los 3 ultimos
        texto[::-1],    # paso -1 => invertido
        texto[1::2],    # desde 1, de 2 en 2
    )


# --- SOLUCION 9 -------------------------------------------------------------
def es_vocal(caracter):
    """
    True si es vocal (mayuscula o minuscula).
    """
    return caracter.lower() in "aeiou"


# --- SOLUCION 10 ------------------------------------------------------------
def contiene(texto, palabra):
    """
    Busquedas basicas dentro de un texto.
    """
    return (
        texto.startswith(palabra),
        texto.endswith(palabra),
        palabra in texto,
        texto.find(palabra),   # -1 si no la encuentra
    )


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