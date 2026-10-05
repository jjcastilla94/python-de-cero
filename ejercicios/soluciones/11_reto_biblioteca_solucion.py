"""
SOLUCION 11 - Reto final: Biblioteca
====================================
Verifica tu resultado ejecutando:
    python soluciones/11_reto_biblioteca_solucion.py
"""

import datetime
import json


# ==========================================================================
# CLASES
# ==========================================================================

class Libro:
    """Representa un libro de la biblioteca."""

    ANIO_ACTUAL = datetime.date.today().year   # atributo de CLASE

    def __init__(self, titulo, autor, anio, categoria="general"):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.disponible = True      # todo libro empieza disponible

    def __str__(self):
        """Ejercicio 2."""
        estado = "disponible" if self.disponible else "prestado"
        return f"{self.titulo} | {self.autor} | {self.anio} | {estado}"

    def a_diccionario(self):
        """Ejercicio 3: el libro como diccionario (para JSON)."""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "categoria": self.categoria,
            "disponible": self.disponible,
        }

    @staticmethod
    def desde_diccionario(datos):
        """Ejercicio 4: reconstruye un Libro desde un diccionario."""
        libro = Libro(
            datos["titulo"],
            datos["autor"],
            datos["anio"],
            datos.get("categoria", "general"),
        )
        libro.disponible = datos.get("disponible", True)
        return libro

    @property
    def antiguedad(self):
        """Ejercicio 5: property que se usa como si fuera un atributo."""
        # un @property NO lleva parentesis al usarlo: libro.antiguedad
        return max(0, self.ANIO_ACTUAL - self.anio)


class Usuario:
    """Persona que puede tomar prestados libros."""

    MAXIMO_PRESTAMOS = 3   # atributo de clase

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.prestados = []       # lista de libros prestados

    def __str__(self):
        """Ejercicio 7."""
        cantidad = len(self.prestados)
        return f"{self.nombre} <{self.email}> ({cantidad} prestados)"

    def prestar(self, libro):
        """Ejercicio 8: como mucho 3 libros."""
        if len(self.prestados) >= self.MAXIMO_PRESTAMOS:
            raise ValueError(
                f"{self.nombre} ya tiene {self.MAXIMO_PRESTAMOS} libros "
                "prestados: no puede tomar mas"
            )
        self.prestados.append(libro)
        return len(self.prestados)

    def devolver(self, titulo):
        """Ejercicio 9: devuelve un libro prestado."""
        for libro in self.prestados:
            if libro.titulo == titulo:
                self.prestados.remove(libro)   # remove quita la coincidencia
                return libro
        raise ValueError(f"{self.nombre} no tiene prestado '{titulo}'")


class Biblioteca:
    """Gestion de libros y usuarios."""

    def __init__(self, nombre="Biblioteca Python"):
        self.nombre = nombre
        self.libros = []                  # lista de objetos Libro
        self.usuarios = {}                # {email: Usuario}

    def registrar(self, libro):
        """Ejercicio 11: no se admiten titulos repetidos."""
        if any(l.titulo.lower() == libro.titulo.lower() for l in self.libros):
            raise ValueError(f"Ya existe el libro '{libro.titulo}'")
        self.libros.append(libro)
        return len(self.libros)

    def buscar(self, texto):
        """Ejercicio 12: busqueda por titulo o autor, sin distinguir mayusculas."""
        texto = texto.lower()
        return [
            libro
            for libro in self.libros
            if texto in libro.titulo.lower() or texto in libro.autor.lower()
        ]

    def _buscar_libro(self, titulo):
        """Auxiliar: devuelve el libro por titulo o None."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar(self, email, titulo):
        """Ejercicio 13: validacion antes de prestar."""
        # 1) el usuario existe
        if email not in self.usuarios:
            raise ValueError(f"El usuario '{email}' no esta registrado")
        # 2) el libro existe
        libro = self._buscar_libro(titulo)
        if libro is None:
            raise ValueError(f"El libro '{titulo}' no existe")
        # 3) el libro esta disponible
        if not libro.disponible:
            raise ValueError(f"'{titulo}' ya esta prestado")

        libro.disponible = False
        self.usuarios[email].prestar(libro)
        return f"'{libro.titulo}' prestado a {email}"

    def devolver(self, email, titulo):
        """Ejercicio 14: devolver un libro."""
        if email not in self.usuarios:
            raise ValueError(f"El usuario '{email}' no esta registrado")
        libro = self._buscar_libro(titulo)
        if libro is None:
            raise ValueError(f"El libro '{titulo}' no existe")

        libro.disponible = True
        self.usuarios[email].devolver(titulo)
        return f"'{libro.titulo}' devuelto por {email}"

    def estadisticas(self):
        """Ejercicio 15: resumen con set para las categorias."""
        disponibles = len([l for l in self.libros if l.disponible])
        return {
            "total": len(self.libros),
            "disponibles": disponibles,
            "prestados": len(self.libros) - disponibles,
            "usuarios": len(self.usuarios),
            "categorias": sorted({l.categoria for l in self.libros}),
        }

    def guardar(self, ruta):
        """Ejercicio 16: serializa la biblioteca a JSON."""
        datos = {
            "nombre": self.nombre,
            "libros": [libro.a_diccionario() for libro in self.libros],
            "usuarios": {
                email: [libro.titulo for libro in usuario.prestados]
                for email, usuario in self.usuarios.items()
            },
        }
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
        return ruta

    def cargar(self, ruta):
        """Ejercicio 17: reconstruye la biblioteca desde JSON."""
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return False

        self.nombre = datos.get("nombre", "Biblioteca Python")
        self.libros = [
            Libro.desde_diccionario(item) for item in datos.get("libros", [])
        ]
        # cada usuario llega como {email: [titulos prestados]}
        self.usuarios = {}
        for email, titulos in datos.get("usuarios", {}).items():
            usuario = Usuario(email.split("@")[0], email)
            for titulo in titulos:
                libro = self._buscar_libro(titulo)
                if libro:
                    usuario.prestados.append(libro)
            self.usuarios[email] = usuario
        return True

    def __len__(self):
        """Ejercicio 18: permite hacer len(biblioteca)."""
        return len(self.libros)

    def __str__(self):
        """Ejercicio 19."""
        return f"{self.nombre} - {len(self.libros)} libros"


# ==========================================================================
# DATOS DE PRUEBA Y MENU (copiados del enunciado)
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
                print("[OK]", biblioteca.prestar(input("Email: "), input("Titulo: ")))

            elif opcion == "4":
                print("[OK]", biblioteca.devolver(input("Email: "), input("Titulo: ")))

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
            print("[ERROR]", error)
        except Exception as error:
            print("[ERROR inesperado]", type(error).__name__, error)


# ==========================================================================
# PRUEBAS automaticas de la solucion
# ==========================================================================

def pruebas():
    biblioteca = datos_iniciales()
    ana = biblioteca.usuarios["ana@mail.com"]

    print(biblioteca)                                   # Biblioteca Municipal - 3 libros
    print("len(biblioteca):", len(biblioteca))          # 3
    print("antiguedad:", biblioteca.libros[0].antiguedad)  # 2026 - 2024 = 2
    print(biblioteca.prestar("ana@mail.com", "Python Basico"))
    print("prestado de nuevo:", end=" ")
    try:
        biblioteca.prestar("ana@mail.com", "Python Basico")
    except ValueError as error:
        print("ValueError ->", error)
    print("estadisticas:", biblioteca.estadisticas())
    print("prestados de Ana:", ana.prestados)
    print(biblioteca.devolver("ana@mail.com", "Python Basico"))
    print(ana)                                          # Ana <ana@mail.com> (0 prestados)

    print("\n-- Pruebas de error --")
    for accion in [
        lambda: biblioteca.registrar(Libro("Python Basico", "Otro", 2020)),
        lambda: biblioteca.prestar("nadie@mail.com", "Clean Code"),
        lambda: biblioteca.prestar("ana@mail.com", "No existe"),
        lambda: ana.devolver("No tiene esto"),
    ]:
        try:
            accion()
        except ValueError as error:
            print("  ValueError ->", error)

    print("\n-- Guardar y cargar --")
    biblioteca.guardar("biblioteca_prueba.json")
    otra = Biblioteca()
    print("cargado:", otra.cargar("biblioteca_prueba.json"))
    print("mismo numero de libros:", len(otra) == len(biblioteca))
    print("estadisticas recargadas:", otra.estadisticas())
    print("cargar inexistente:", otra.cargar("no_existe.json"))


if __name__ == "__main__":
    if "--menu" in __import__("sys").argv:
        menu(datos_iniciales())
    else:
        pruebas()