"""
SOLUCION 03 - Condicionales
===========================
Verifica tu resultado ejecutando:
    python soluciones/03_condicionales_solucion.py
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
def signo(numero):
    """
    Devuelve "positivo", "negativo" o "cero".
    """
    # elif solo se comprueba cuando el if anterior fue False
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"


# --- SOLUCION 2 -------------------------------------------------------------
def calificar(nota):
    """
    Nota numerica -> letra.
    """
    # primero se valida el rango, despues se Mira la nota
    if nota < 0 or nota > 100:
        return "nota invalida"
    elif nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"


# --- SOLUCION 3 -------------------------------------------------------------
def es_bisiesto(anio):
    """
    Bisiesto: divisible entre 4 y no entre 100, o divisible entre 400.
    """
    # los parentesis controlan el orden: (A and not B) or C
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


# --- SOLUCION 4 -------------------------------------------------------------
def paridad(numero):
    """
    Ternario en una sola linea.
    """
    return "par" if numero % 2 == 0 else "impar"


# --- SOLUCION 5 -------------------------------------------------------------
def validar_password(password):
    """
    Devuelve la lista de requisitos NO cumplidos.
    """
    # any() pregunta si ALGUNO cumple -> por eso se niega con not
    # any(c.isupper() for c in password)  -> hay mayusculas?
    requisitos = []
    if len(password) < 8:
        requisitos.append("longitud")
    if not any(c.isupper() for c in password):
        requisitos.append("mayuscula")
    if not any(c.islower() for c in password):
        requisitos.append("minuscula")
    if not any(c.isdigit() for c in password):
        requisitos.append("digito")
    return requisitos


# --- SOLUCION 6 -------------------------------------------------------------
def fizzbuzz(n):
    """
    FizzBuzz del 1 al n.
    """
    resultado = []
    for i in range(1, n + 1):
        # el caso mas especifico (3 y 5) SIEMPRE va primero
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    return resultado


# --- SOLUCION 7 -------------------------------------------------------------
def tipo_triangulo(a, b, c):
    """
    Clasifica un triangulo por sus lados.
    """
    # desigualdad triangular: la suma de dos lados debe superar al tercero
    if a + b <= c or a + c <= b or b + c <= a:
        return "no es triangulo"
    elif a == b == c:
        return "equilatero"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "escaleno"


# --- SOLUCION 8 -------------------------------------------------------------
def clasificar_valor(valor):
    """
    Clasifica un valor con if-elif-else y sin operadores logicos.
    """
    if valor is None or valor in ("", [], {}):
        return "vacio"
    elif type(valor) in (int, float):
        return "numero"
    elif isinstance(valor, str):
        return "texto"
    else:
        return "otro"


EJERCICIOS = [
    lambda: signo(7),
    lambda: signo(0),
    lambda: calificar(85),
    lambda: calificar(120),
    lambda: es_bisiesto(2024),
    lambda: es_bisiesto(1900),
    lambda: paridad(4),
    lambda: validar_password("abc"),
    lambda: validar_password("Abcdefg1"),
    lambda: fizzbuzz(15),
    lambda: tipo_triangulo(3, 3, 3),
    lambda: tipo_triangulo(3, 3, 5),
    lambda: tipo_triangulo(1, 2, 10),
    lambda: clasificar_valor(""),
    lambda: clasificar_valor(5),
    lambda: clasificar_valor("hola"),
]

if __name__ == "__main__":
    _main(EJERCICIOS)