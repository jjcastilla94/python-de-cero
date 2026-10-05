"""
SOLUCION 08 - Funciones
=======================
Verifica tu resultado ejecutando:
    python soluciones/08_funciones_solucion.py
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


# --- SOLUCION 1: parametro por defecto -------------------------------------
def saludar(nombre, saludo="Hola"):
    """
    Saludo con valor por defecto.
    """
    # "saludo" puede omitirse: entonces vale "Hola"
    return f"{saludo}, {nombre}!"


# --- SOLUCION 2: *args ------------------------------------------------------
def sumar_todos(*numeros):
    """
    Suma un numero variable de argumentos.
    """
    # numeros es una tupla; sum([]) y sum(()) valen 0
    return sum(numeros)


# --- SOLUCION 3: **kwargs ---------------------------------------------------
def construir_usuario(nombre, **campos):
    """
    Diccionario con datos variables.
    """
    usuario = {"nombre": nombre}
    usuario.update(campos)   # campos es un diccionario
    return usuario


# --- SOLUCION 4: retorno multiple ------------------------------------------
def minimo_y_maximo(lista):
    """
    Devuelve dos valores a la vez.
    """
    # return a, b  ==  return (a, b)  -> el que lo recibe hace: x, y = f()
    if not lista:
        return None, None
    return min(lista), max(lista)


# --- SOLUCION 5: recursividad ----------------------------------------------
def factorial(n):
    """
    Factorial recursivo.
    """
    # caso base: detiene la recursion; si no, se repite n veces
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# --- SOLUCION 6: fibonacci recursivo ---------------------------------------
def fibonacci(cantidad):
    """
    Fibonacci con recursion.
    """
    if cantidad <= 0:
        return []
    return [fibonacci_hasta(indice) for indice in range(cantidad)]


def fibonacci_hasta(indice):
    """Auxiliar: valor de la posicion indice de la secuencia."""
    if indice < 2:
        return indice
    return fibonacci_hasta(indice - 1) + fibonacci_hasta(indice - 2)


# --- SOLUCION 7: map / filter / reduce -------------------------------------
def con_funciones_de_orden_superior():
    """
    Funciones que reciben lambdas.
    """
    from functools import reduce

    valores = [1, 2, 3, 4, 5]
    return {
        # map devuelve un iterador, hay que envolverlo con list()
        "dobles": list(map(lambda x: x * 2, valores)),
        # filter se queda con los que cumplen la condicion
        "mayores_10": list(filter(lambda x: x > 3, [5, 8, 12, 15])),
        # reduce acumula: suma todos los valores
        "suma": reduce(lambda a, b: a + b, valores),
    }


# --- SOLUCION 8: validacion con raise --------------------------------------
def dividir(a, b):
    """
    Division validada.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Solo se admiten numeros")
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


# --- SOLUCION 9: caso limite -----------------------------------------------
def promedio(notas):
    """
    Media segura con lista vacia.
    """
    if not notas:          # atajo: lista vacia es False
        return 0
    return sum(notas) / len(notas)


# --- SOLUCION 10: funcion como dic -----------------------------------------
def contador(texto):
    """
    Cuenta letras ignorando espacios.
    """
    conteo = {}
    for letra in texto:
        if letra == " ":
            continue          # no cuenta los espacios
        conteo[letra] = conteo.get(letra, 0) + 1
    return conteo


# --- SOLUCION 11: funcion de orden superior --------------------------------
def aplicar_funcion(funcion, valores):
    """
    Aplica la funcion recibida a cada elemento.
    """
    # "funcion" es un parametro que contiene otra funcion
    return [funcion(valor) for valor in valores]


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