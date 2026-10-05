"""
SOLUCION 10 - Errores, archivos y modulos
=========================================
Verifica tu resultado ejecutando:
    python soluciones/10_errores_archivos_solucion.py
"""

import csv
import datetime
import json
import math
import os
import random
import re


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
# PARTE A - Manejo de errores
# ==========================================================================

def division_segura(a, b):
    """
    Division que no se rompe con b == 0.
    """
    try:
        return a / b
    except ZeroDivisionError:
        # se captura SOLO el error indicado; el resto de errores se propagan
        return "error: division por cero"


def leer_numero(texto):
    """
    Convierte a entero o devuelve None.
    """
    try:
        return int(texto)
    except ValueError:
        return None
    # finally no hace falta aqui, pero sirve para logs o limpieza


def validar_rango(valor, minimo, maximo):
    """
    Valida numero y rango con try/except.
    """
    try:
        numero = float(valor)      # aqui salta ValueError si no es numero
    except ValueError:
        return "error: no es un numero"

    if not minimo <= numero <= maximo:
        return "error: fuera de rango"
    return "ok"


def edad_valida(edad):
    """
    Lanza un error propio con raise.
    """
    if edad < 0 or edad > 120:
        # raise crea una excepcion: el programa se detiene aqui
        raise ValueError("edad invalida")
    return edad


# ==========================================================================
# PARTE B - Archivos
# ==========================================================================

def escribir_y_leer(ruta):
    """
    Escribe tres lineas y las devuelve en mayusculas.
    """
    # el modo "w" BORRA el archivo si ya existe
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("uno\n")
        archivo.write("dos\n")
        archivo.write("tres\n")
    # with cierra el archivo automaticamente, incluso si hay error

    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read().upper()


def contar_lineas(ruta):
    """
    Cuenta lineas no vacias; -1 si el archivo no existe.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            # iterar el archivo da una linea cada vez
            return len([linea for linea in archivo if linea.strip()])
    except FileNotFoundError:
        return -1


def anadir_linea(ruta, texto):
    """
    Anade al final sin borrar (modo "a" de append).
    """
    # "a" crea el archivo si no existe y escribe al final
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"{texto}\n")
    return True


def copiar_archivo(origen, destino):
    """
    Copia un archivo y devuelve cuantos caracteres se copiaron.
    """
    try:
        with open(origen, "r", encoding="utf-8") as f_origen:
            contenido = f_origen.read()
    except FileNotFoundError:
        return -1

    with open(destino, "w", encoding="utf-8") as f_destino:
        f_destino.write(contenido)
    return len(contenido)


# ==========================================================================
# PARTE C - Modulos estandar
# ==========================================================================

def con_modulos_estandar():
    """
    Usa math, random, datetime y os.
    """
    return {
        "raiz": math.sqrt(144),                  # raiz cuadrada
        "redondeo": math.floor(3.7),             # parte entera: 3
        "aleatorio": random.randint(1, 6),       # entero aleatorio 1-6
        "hoy": datetime.date.today().isoformat(),
        "carpeta": os.path.exists("datos.txt"),
    }


def buscar_emails(texto):
    """
    Extrae emails con expresiones regulares.
    """
    # re.findall devuelve todas las coincidencias del patron
    return re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", texto)


def guardar_y_leer_json(ruta, datos):
    """
    Ida y vuelta a JSON.
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

    with open(ruta, "r", encoding="utf-8") as archivo:
        # json.load lee el archivo y lo convierte en diccionario
        return json.load(archivo)


def guardar_csv(ruta, filas):
    """
    Ida y vuelta a CSV.
    """
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        # en windows hace falta newline="" para evitar lineas en blanco
        escritor = csv.writer(archivo)
        escritor.writerows(filas)

    with open(ruta, "r", newline="", encoding="utf-8") as archivo:
        return list(csv.reader(archivo))


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