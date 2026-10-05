"""
SOLUCION 09 - Programacion orientada a objetos (POO)
====================================================
Verifica tu resultado ejecutando:
    python soluciones/09_poo_solucion.py
"""


def _main(ejercicios):
    import inspect

    for ej in ejercicios:
        print("=" * 62)
        nombre = getattr(ej, "__name__", "lambda")
        print(nombre, "->", (inspect.getdoc(ej) or "").strip())
        try:
            print("    ", ej())
        except Exception as exc:
            print(f"     [ERROR] {type(exc).__name__}: {exc}")


# ==========================================================================
# PARTE A - Clase basica
# ==========================================================================

class Rectangulo:
    """Rectangulo con ancho y alto."""

    # __init__ es el CONSTRUCTOR: se llama al crear el objeto (Rectangulo(4, 3))
    # self es la referencia al propio objeto: permite guardar sus atributos
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        """Devuelve ancho * alto."""
        return self.ancho * self.alto

    def perimetro(self):
        """Devuelve 2 * (ancho + alto)."""
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        """True si ancho == alto."""
        return self.ancho == self.alto

    def __str__(self):
        """Como se muestra el objeto al imprimirlo."""
        return f"Rectangulo {self.ancho}x{self.alto}"


# ==========================================================================
# PARTE B - Property y validacion
# ==========================================================================

class CuentaBancaria:
    """Cuenta con saldo controlado mediante @property."""

    def __init__(self, titular, saldo=0):
        # OJO: titular es un property SIN setter, asi que se asigna
        # directamente al atributo "privado" _titular
        self._titular = titular
        self.saldo = saldo       # pasa por el setter -> se valida

    @property
    def titular(self):
        """Solo lectura: pedir titular no tiene parentesis."""
        return self._titular

    @property
    def saldo(self):
        """Devuelve el saldo real (guardado en _saldo)."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """Se ejecuta cada vez que se asigna cuenta.saldo = ..."""
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def ingresar(self, cantidad):
        """Suma dinero (no puede ser negativo)."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.saldo += cantidad   # pasa por el setter
        return self.saldo

    def retirar(self, cantidad):
        """Resta dinero; falla si no hay saldo suficiente."""
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        return self.saldo

    def __str__(self):
        """Devuelve "{titular}: {saldo:.2f}"."""
        return f"{self.titular}: {self.saldo:.2f}"


# ==========================================================================
# PARTE C - Herencia
# ==========================================================================

class Animal:
    """Clase base de todos los animales."""

    def __init__(self, nombre):
        self.nombre = nombre

    def presentar(self):
        """Usa ruido(): los hijos lo sobrescriben (polimorfismo)."""
        return f"{self.nombre} dice: {self.ruido()}"

    def ruido(self):
        """Comportamiento por defecto."""
        return "sonido generico"


class Perro(Animal):
    """Heredan todo de Animal y cambian solo el ruido."""

    def ruido(self):
        return "guau"


class Gato(Animal):
    """Heredan de Animal y anaden un metodo propio."""

    def ruido(self):
        return "miau"

    def saltar(self):
        return f"{self.nombre} salta a 1.5 metros"


class PerroGuia(Perro):
    """Herencia de segundo nivel: PerroGuia -> Perro -> Animal."""

    def __init__(self, nombre, raza):
        # super() llama al __init__ del padre: reutiliza su codigo
        super().__init__(nombre)
        self.raza = raza

    def __str__(self):
        return f"{self.nombre} ({self.raza}) seria guia"


# ==========================================================================
# PARTE D - staticmethod, comparaciones
# ==========================================================================

class Producto:
    """Producto comparable con < y con =="""

    IVA = 0.21   # atributo de CLASE (compartido por todos los objetos)

    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @staticmethod
    def precio_con_iva(precio):
        """No necesita self ni cls: es una calculadora suelta."""
        return round(precio * (1 + Producto.IVA), 2)

    def con_iva(self):
        """Usa el metodo estatico sobre su propio precio."""
        return self.precio_con_iva(self.precio)

    @classmethod
    def con_stock(cls, nombre, precio, stock):
        """classmethod: recibe cls (la clase) y puede crear objetos."""
        producto = cls(nombre, precio, stock)
        return producto

    def __str__(self):
        return f"{self.nombre} ({self.precio:.2f})"

    # dunder de comparacion: define el operador <
    def __lt__(self, otro):
        return self.precio < otro.precio

    # dunder de igualdad: define el operador ==
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.precio == otro.precio


EJERCICIOS = [
    lambda: str(Rectangulo(4, 3)),
    lambda: Rectangulo(4, 3).area(),
    lambda: Rectangulo(4, 3).perimetro(),
    lambda: Rectangulo(4, 4).es_cuadrado(),
    lambda: str(CuentaBancaria("Ana", 100)),
    lambda: CuentaBancaria("Ana", 100).ingresar(50),
    lambda: CuentaBancaria("Ana", 100).titular,
    lambda: Animal("Rex").presentar(),
    lambda: Perro("Rex").presentar(),
    lambda: Gato("Felix").saltar(),
    lambda: str(PerroGuia("Rex", "Labrador")),
    lambda: Producto.precio_con_iva(100),
    lambda: Producto("Camiseta", 20, 10).con_iva(),
    lambda: Producto("A", 10, 1) < Producto("B", 5, 2),
    lambda: Producto("A", 10, 1) == Producto("A", 10, 2),
]

if __name__ == "__main__":
    _main(EJERCICIOS)