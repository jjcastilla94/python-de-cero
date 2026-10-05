"""
SOLUCION 04 - Bucles
====================
Verifica tu resultado ejecutando:
    python soluciones/04_bucles_solucion.py
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
def sumar_hasta(n):
    """
    Suma del 1 al n con for.
    """
    # sum() es un atajo, pero aqui se pide el bucle: se acumula a mano
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# --- SOLUCION 2 -------------------------------------------------------------
def tabla_multiplicar(n, limite=10):
    """
    Tabla de multiplicar con dos for anidados.
    """
    lineas = []
    for i in range(1, limite + 1):
        lineas.append(f"{n} x {i} = {n * i}")
    return lineas


# --- SOLUCION 3 -------------------------------------------------------------
def cuenta_atras_saltando(n):
    """
    Cuenta atras saltando multiplos de 3.
    """
    numeros = []
    for i in range(n, 0, -1):
        if i % 3 == 0:
            continue      # continue: salta a la siguiente vuelta
        numeros.append(i)
    return numeros


# --- SOLUCION 4 -------------------------------------------------------------
def es_primo(n):
    """Auxiliar: True si n es primo."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def primer_primo(desde):
    """
    Primer primo >= desde usando break.
    """
    for candidato in range(desde, desde + 100):
        if es_primo(candidato):
            return candidato   # break implicito con return
    return None


# --- SOLUCION 5 -------------------------------------------------------------
def variantes_de_range():
    """
    Las tres formas de range().
    """
    # range(inicio, fin, salto): el fin NUNCA se incluye
    return (list(range(0, 10, 2)), list(range(5, 0, -1)), list(range(2, 6)))


# --- SOLUCION 6 -------------------------------------------------------------
def numerar_elementos(lista):
    """
    enumerate() da (indice, valor) en el bucle.
    """
    resultado = []
    for indice, elemento in enumerate(lista, start=1):
        resultado.append(f"{indice}. {elemento}")
    return resultado


# --- SOLUCION 7 -------------------------------------------------------------
def buscar_elemento(lista, objetivo):
    """
    for ... else: el else se ejecuta si nunca hubo break.
    """
    for elemento in lista:
        if elemento == objetivo:
            return True
    else:
        # se llega aqui solo si el bucle termino sin break
        return False


# --- SOLUCION 8 -------------------------------------------------------------
def suma_digitos(numero):
    """
    Suma de cifras con while.
    """
    total = 0
    while numero > 0:
        total += numero % 10    # % 10 = ultimo digito
        numero //= 10           # // 10 = quita el ultimo digito
    return total


# --- SOLUCION 9 -------------------------------------------------------------
def cruzar_listas(nombres, edades):
    """
    zip() empareja elementos de dos listas.
    """
    return [f"{nombre}:{edad}" for nombre, edad in zip(nombres, edades)]


# --- SOLUCION 10 ------------------------------------------------------------
def piramide(altura):
    """
    Piramide de asteriscos.
    """
    return ["*" * i for i in range(1, altura + 1)]


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