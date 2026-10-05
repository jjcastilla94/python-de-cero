"""
RETO FINAL - Biblioteca (todo junto)
====================================
Este archivo mezcla TODO lo aprendido: clases, herencia, properties,
diccionarios, listas, lambdas, validacion con try/except, archivos y menu
por consola.

COMO FUNCIONA
-------------
1. Ejecuta:  python 11_reto_biblioteca.py
2. Cada "TODO" esta marcado con  raise NotImplementedError
3. Al terminar, compara con:
   soluciones/11_reto_biblioteca_solucion.py

REGLAS DE LA BIBLIOTECA
-----------------------
- Un libro tiene: titulo, autor, anio, disponible (bool), categoria (str)
- Un usuario tiene: nombre, email y una lista de libros prestados
- La biblioteca permite: prestar, devolver, buscar por titulo/autor y guardar
  en un archivo JSON
"""

import json


# ==========================================================================
# CLASES
# ==========================================================================

class Libro:
    """Representa un libro de la biblioteca."""

    def __init__(self, titulo, autor, anio, categoria="general"):
        # TODO 1: guarda titulo, autor, anio, categoria y disponible = True
        raise NotImplementedError("TODO 1")

    def __str__(self):
        """Ejercicio 2: "Python Basico | Ramirez | 2024 | disponible" """
        raise NotImplementedError("TODO 2")

    def a_diccionario(self):
        """
        Ejercicio 3: devuelve el libro como diccionario
        (util para guardarlo en JSON).
        """
        raise NotImplementedError("TODO 3")

    @staticmethod
    def desde_diccionario(datos):
        """
        Ejercicio 4:classmethod que RECONSTRUYE un Libro desde un diccionario.
        Pista: cls(...) crea un objeto de la propia clase.
        """
        raise NotImplementedError("TODO 4")

    @property
    def antiguedad(self):
        """
        Ejercicio 5:property que devuelve cuantos anos tiene el libro
        (2026 - anio). Si el anio es del futuro, devuelve 0.
        """
        raise NotImplementedError("TODO 5")


class Usuario:
    """Persona que puede tomar prestados libros."""

    def __init__(self, nombre, email):
        # TODO 6: guarda nombre, email y crea la lista vacia "prestados"
        raise NotImplementedError("TODO 6")

    def __str__(self):
        """Ejercicio 7: "Ana <ana@mail.com> (2 prestados)" """
        raise NotImplementedError("TODO 7")

    def prestar(self, libro):
        """
        Ejercicio 8: anade el libro a su lista de prestados.
        Regla: maximo 3 libros. Si se supera, lanza ValueError.
        """
        raise NotImplementedError("TODO 8")

    def devolver(self, titulo):
        """
        Ejercicio 9: elimina de su lista el libro con ese titulo y lo
        devuelve. Si no lo tenia prestado, lanza ValueError.
        """
        raise NotImplementedError("TODO 9")


class Biblioteca:
    """Gestion de libros y usuarios."""

    def __init__(self, nombre="Biblioteca Python"):
        # TODO 10: guarda nombre, crea lista "libros" y diccionario "usuarios"
        raise NotImplementedError("TODO 10")

    def registrar(self, libro):
        """
        Ejercicio 11: anade un libro a la lista. Si ya existe un libro con
        el mismo titulo, lanza ValueError.
        """
        raise NotImplementedError("TODO 11")

    def buscar(self, texto):
        """
        Ejercicio 12: devuelve la lista de libros cuyo titulo o autor
        contengan "texto" (sin distinguir mayusculas).
        """
        raise NotImplementedError("TODO 12")

    def prestar(self, email, titulo):
        """
        Ejercicio 13: presta un libro a un usuario existente.
        Reglas (lanza ValueError si no se cumple):
            - el usuario debe existir
            - el libro debe existir
            - el libro debe estar disponible
        Al prestar: marca el libro como no disponible y anadelo a la lista
        del usuario. Devuelve un texto con el resultado.
        """
        raise NotImplementedError("TODO 13")

    def devolver(self, email, titulo):
        """
        Ejercicio 14: devuelve un libro. Marca el libro como disponible,
        quitalo de la lista del usuario y devuelve un texto con el resultado.
        """
        raise NotImplementedError("TODO 14")

    def estadisticas(self):
        """
        Ejercicio 15: devuelve un diccionario con:
            "total"       numero de libros
            "disponibles" numero de libros disponibles
            "prestados"   numero de libros prestados
            "usuarios"    numero de usuarios
            "categorias"  lista ordenada de categorias sin repetir
        """
        raise NotImplementedError("TODO 15")

    def guardar(self, ruta):
        """
        Ejercicio 16: guarda en un archivo JSON un diccionario con:
            "nombre"    -> nombre de la biblioteca
            "libros"    -> lista de libros en formato diccionario
            "usuarios"  -> {email: [titulos prestados]}
        """
        raise NotImplementedError("TODO 16")

    def cargar(self, ruta):
        """
        Ejercicio 17: carga el archivo JSON creado por guardar() y reconstruye
        los libros (Libro.desde_diccionario) y los usuarios con sus listas
        de prestados. Si el archivo no existe, devuelve False.
        """
        raise NotImplementedError("TODO 17")

    def __len__(self):
        """Ejercicio 18: devuelve el numero de libros (__len__ permite len(biblioteca))."""
        raise NotImplementedError("TODO 18")

    def __str__(self):
        """Ejercicio 19: "{nombre} - {n} libros" """
        raise NotImplementedError("TODO 19")


# ==========================================================================
# DATOS DE PRUEBA Y MENU (esto YA esta hecho: no lo cambies)
# ==========================================================================

def datos_iniciales():
    """Devuelve una biblioteca con 3 libros y 1 usuario listos para probar."""
    biblioteca = Biblioteca("Biblioteca Municipal")
    for libro in [
        Libro("Python Basico", "Ana Ramirez", 2024, "programacion"),
        Libro("Clean Code", "Robert Martin", 2008, "programacion"),
        Libro("Cien anos de soledad", "Gabriel Garcia Marquez", 1967, "novela"),
    ]:
        biblioteca.registrar(libro)

    ana = Usuario("Ana", "ana@mail.com")
    biblioteca.usuarios[ana.email] = ana
    return biblioteca


def menu(biblioteca):
    """Menu por consola que usa TODAS las funciones anteriores."""
    while True:
        print("\n--- MENU ---")
        print("1. Registrar libro     2. Buscar libro")
        print("3. Prestar libro       4. Devolver libro")
        print("5. Estadisticas        6. Guardar en JSON")
        print("7. Salir")
        opcion = input("Elige una opcion: ").strip()

        try:
            if opcion == "1":
                titulo = input("Titulo: ")
                autor = input("Autor: ")
                anio = int(input("Anio: "))
                categoria = input("Categoria (general): ") or "general"
                biblioteca.registrar(Libro(titulo, autor, anio, categoria))
                print("[OK] Libro registrado")

            elif opcion == "2":
                texto = input("Buscar: ")
                for libro in biblioteca.buscar(texto):
                    print("  -", libro)

            elif opcion == "3":
                biblioteca.prestar(input("Email: "), input("Titulo: "))

            elif opcion == "4":
                biblioteca.devolver(input("Email: "), input("Titulo: "))

            elif opcion == "5":
                for clave, valor in biblioteca.estadisticas().items():
                    print(f"  {clave}: {valor}")

            elif opcion == "6":
                ruta = input("Archivo (biblioteca.json): ")
                biblioteca.guardar(ruta)
                print("[OK] Guardado en", ruta)

            elif opcion == "7":
                print("Hasta luego")
                break

            else:
                print("[!] Opcion no valida")

        except ValueError as error:
            # el menu captura los errores controlados de la biblioteca
            print("[ERROR]", error)
        except Exception as error:
            print("[ERROR inesperado]", type(error).__name__, error)


if __name__ == "__main__":
    menu(datos_iniciales())