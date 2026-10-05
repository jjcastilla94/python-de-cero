"""
EJERCICIOS 10 - Errores, archivos y modulos
===========================================
Objetivo: try/except/else/finally, raise, validacion de entradas, leer y
escribir archivos con with, y uso de modulos estandar (math, random,
datetime, os, csv, json, re).

Ejecuta:  python 10_errores_archivos.py
Solucion: soluciones/10_errores_archivos_solucion.py
"""


# ==========================================================================
# PARTE A - Manejo de errores
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
def division_segura(a, b):
    """
    Devuelve la division de a entre b. Si b es 0 NO debe romperse el
    programa: devuelve el texto "error: division por cero".
    Usa try/except ZeroDivisionError.
    """
    raise NotImplementedError("TODO 1")


# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
def leer_numero(texto):
    """
    Convierte "texto" a entero. Si no es posible devuelve None.
    NO dejes que el ValueError llegue al programa.
    """
    raise NotImplementedError("TODO 2")


# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
def validar_rango(valor, minimo, maximo):
    """
    Devuelve:
        - "ok"                si minimo <= valor <= maximo
        - "error: no es un numero"  si no se puede convertir a float
        - "error: fuera de rango"  si el numero no esta entre los limites
    Todo con try/except, sin romper el programa.
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
def edad_valida(edad):
    """
    Si la edad es menor de 0 o mayor de 120, lanza un error tu propio con
    raise ValueError("edad invalida"). Si es correcta, devuelve la edad.
    """
    raise NotImplementedError("TODO 4")


# ==========================================================================
# PARTE B - Archivos de texto
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 5
# --------------------------------------------------------------------------
def escribir_y_leer(ruta):
    """
    Escribe en el archivo "ruta" tres lineas ("uno", "dos", "tres") usando
    with open(ruta, "w") y devuelve el contenido leido en MAYUSCULAS.
    Recuerda cerrar siempre con with.
    """
    raise NotImplementedError("TODO 5")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
def contar_lineas(ruta):
    """
    Devuelve cuantas lineas tiene el archivo (sin contar lineas vacias).
    Si el archivo no existe, devuelve -1 (captura FileNotFoundError).
    """
    raise NotImplementedError("TODO 6")


# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
def anadir_linea(ruta, texto):
    """
    Anade una linea al final de un archivo existente SIN borrar lo que
    hay dentro (modo "a"). Si el archivo no existe, lo crea.
    """
    raise NotImplementedError("TODO 7")


# --------------------------------------------------------------------------
# EJERCICIO 8
# --------------------------------------------------------------------------
def copiar_archivo(origen, destino):
    """
    Copia el contenido de "origen" en "destino" y devuelve el numero de
    caracteres copiados. Si el origen no existe, devuelve -1.
    """
    raise NotImplementedError("TODO 8")


# ==========================================================================
# PARTE C - Modulos estandar
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 9
# --------------------------------------------------------------------------
def con_modulos_estandar():
    """
    Usa los modulos estandar y devuelve un diccionario con:
        "raiz"      -> math.sqrt(144)
        "redondeo"  -> math.floor(3.7)  (parte entera)
        "aleatorio" -> un entero aleatorio entre 1 y 6 (importa random)
        "hoy"       -> la fecha de hoy como texto (importa datetime)
        "carpeta"   -> si el archivo "datos.txt" existe en la carpeta actual
                       (importa os, usa os.path.exists)
    """
    raise NotImplementedError("TODO 9")


# --------------------------------------------------------------------------
# EJERCICIO 10
# --------------------------------------------------------------------------
def buscar_emails(texto):
    r"""
    Usa el modulo re para devolver la lista de emails de un texto.
    Entrada:  buscar_emails("ana@a.com y luis@b.org")
              -> ["ana@a.com", "luis@b.org"]
    Expresion regular sugerida: r"[\w.+-]+@[\w-]+\.[\w.]+"
    (la r delante de las comillas indica "cadena en bruto": los \w no se
     interpretan como caracteres especiales de Python)
    """
    raise NotImplementedError("TODO 10")


# --------------------------------------------------------------------------
# EJERCICIO 11
# --------------------------------------------------------------------------
def guardar_y_leer_json(ruta, datos):
    """
    Guarda un diccionario en un archivo JSON y lo lee de vuelta devolviendo
    el diccionario leido. Usa el modulo json con with open.
    """
    raise NotImplementedError("TODO 11")


# --------------------------------------------------------------------------
# EJERCICIO 12
# --------------------------------------------------------------------------
def guardar_csv(ruta, filas):
    """
    Guarda una lista de listas en un archivo CSV y devuelve la lista de
    filas leida de vuelta. Usa el modulo csv.
    filas = [["nombre", "edad"], ["Ana", 25], ["Luis", 30]]
    """
    raise NotImplementedError("TODO 12")


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


RUTA = "datos_ejercicios.txt"

EJERCICIOS = [
    lambda: division_segura(10, 2),
    lambda: division_segura(10, 0),
    lambda: leer_numero("123"),
    lambda: leer_numero("abc"),
    lambda: validar_rango("5", 1, 10),
    lambda: validar_rango("50", 1, 10),
    lambda: validar_rango("abc", 1, 10),
    lambda: edad_valida(30),
    lambda: escribir_y_leer(RUTA),
    lambda: contar_lineas(RUTA),
    lambda: anadir_linea(RUTA, "cuatro"),
    lambda: copiar_archivo(RUTA, "datos_copia.txt"),
    lambda: copiar_archivo("no_existe.txt", "datos_copia.txt"),
    con_modulos_estandar,
    lambda: buscar_emails("ana@a.com y luis@b.org"),
    lambda: guardar_y_leer_json("datos.json", {"nombre": "Ana", "edad": 25}),
    lambda: guardar_csv("datos.csv", [["nombre", "edad"], ["Ana", 25]]),
]

if __name__ == "__main__":
    _main(EJERCICIOS)