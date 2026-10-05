"""
EJERCICIOS 09 - Programacion orientada a objetos (POO)
====================================================
Objetivo: clases, __init__, atributos, metodos, self, __str__, properties,
herencia, super(), metodos estaticos y de clase.

Ejecuta:  python 09_poo.py
Solucion: soluciones/09_poo_solucion.py
"""


# ==========================================================================
# PARTE A - Clase basica
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 1
# --------------------------------------------------------------------------
class Rectangulo:
    """
    Completa esta clase:

        r = Rectangulo(4, 3)
        r.area()      -> 12
        r.perimetro() -> 14
        str(r)        -> "Rectangulo 4x3"
        r.es_cuadrado() -> False   (True si alto == ancho)
    """
    # OJO: falta el metodo constructor __init__(self, ancho, alto)

    def area(self):
        """Devuelve ancho * alto."""
        raise NotImplementedError("TODO 1.1")

    def perimetro(self):
        """Devuelve 2 * (ancho + alto)."""
        raise NotImplementedError("TODO 1.2")

    def es_cuadrado(self):
        """True si ancho == alto."""
        raise NotImplementedError("TODO 1.3")

    def __str__(self):
        """Devuelve "Rectangulo {ancho}x{alto}"."""
        raise NotImplementedError("TODO 1.4")


# ==========================================================================
# PARTE B - Property y validacion
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 2
# --------------------------------------------------------------------------
class CuentaBancaria:
    """
    Completa esta clase:
        c = CuentaBancaria("Ana", 100)
        c.ingresar(50)    -> saldo 150
        c.retirar(200)    -> lanza ValueError ("Saldo insuficiente")
        c.retirar(20)     -> saldo 130
        c.saldo           -> 130   (atributo, no metodo: es un @property)
        c.titular         -> "Ana" (solo lectura, tambien @property)
    Ademas:
        - el saldo nunca puede quedar negativo (valida en el setter)
        - __str__ devuelve "Ana: 130.00"
    """
    # OJO: falta __init__, los @property y la validacion

    def ingresar(self, cantidad):
        """Suma dinero al saldo y devuelve el nuevo saldo."""
        raise NotImplementedError("TODO 2.1")

    def retirar(self, cantidad):
        """Resta dinero. Si no hay saldo suficiente, lanza ValueError."""
        raise NotImplementedError("TODO 2.2")

    def __str__(self):
        """Devuelve "{titular}: {saldo:.2f}"."""
        raise NotImplementedError("TODO 2")


# ==========================================================================
# PARTE C - Herencia
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 3
# --------------------------------------------------------------------------
class Animal:
    """
    Clase base. Completa:
        Animal("Rex").presentar() -> "Rex dice: Hago sonidos"
        Animal("Rex").ruido()       -> "sonido generico"
    Metodos: __init__(nombre), presentar(), ruido()
    """

    def __init__(self, nombre):
        """Guarda self.nombre."""
        raise NotImplementedError("TODO 3.1")

    def presentar(self):
        """Devuelve "{nombre} dice: {ruido()}"."""
        raise NotImplementedError("TODO 3.2")

    def ruido(self):
        """Devuelve "sonido generico"."""
        raise NotImplementedError("TODO 3.3")


# --------------------------------------------------------------------------
# EJERCICIO 4
# --------------------------------------------------------------------------
class Perro(Animal):
    """
    Hereda de Animal y sobrescribe ruido():
        Perro("Rex").ruido()      -> "guau"
        Perro("Rex").presentar() -> "Rex dice: guau"   (heredado)
    """

    def ruido(self):
        """Devuelve "guau"."""
        raise NotImplementedError("TODO 4")


class Gato(Animal):
    """
    Hereda de Animal, ruido() -> "miau", y anade el metodo saltar()
    que devuelve "{nombre} salta a 1.5 metros".
    """

    def ruido(self):
        """Devuelve "miau"."""
        raise NotImplementedError("TODO 5.1")

    def saltar(self):
        """Devuelve "{nombre} salta a 1.5 metros"."""
        raise NotImplementedError("TODO 5.2")


# --------------------------------------------------------------------------
# EJERCICIO 6
# --------------------------------------------------------------------------
class PerroGuia(Perro):
    """
    Hereda de Perro. Su __init__ recibe tambien "raza" y llama a
    super().__init__(nombre) para reutilizar el codigo del padre.
        p = PerroGuia("Rex", "Labrador")
        p.ruido()        -> "guau"
        p.raza           -> "Labrador"
        str(p)           -> "Rex (Labrador) seria guia"
    """

    def __str__(self):
        """Devuelve "{nombre} ({raza}) seria guia"."""
        raise NotImplementedError("TODO 6.1")


# ==========================================================================
# PARTE D - staticmethod, classmethod y comparacion
# ==========================================================================

# --------------------------------------------------------------------------
# EJERCICIO 7
# --------------------------------------------------------------------------
class Producto:
    """
    Completa:
        Producto("Camiseta", 20, 10).con_iva()  -> 24.2   (@staticmethod)
        Producto.precio_con_iva(100)           -> 121.0  (@staticmethod)
        Producto("A", 10).es_mas_barato_que(Producto("B", 5)) -> False
        str(Producto("Camiseta", 20, 10))       -> "Camiseta (20.00)"
        Producto("A", 10, 1) == Producto("A", 10, 2) -> True
                                             (compara nombre y precio)
    """
    # OJO: faltan __init__, __str__, __eq__, __lt__ y con_iva()
    # Pista: los "dunder" (los metodos entre lineas dobles) son los que
    #        definen como se comporta el objeto con los operadores:
    #        __init__ al crear, __str__ al imprimir, __lt__ con <, __eq__ con ==

    def __init__(self, nombre, precio, stock=0):
        """Guarda nombre, precio y stock."""
        raise NotImplementedError("TODO 7.0")

    @staticmethod
    def precio_con_iva(precio):
        """Devuelve el precio con un 21% de IVA."""
        raise NotImplementedError("TODO 7.1")

    def con_iva(self):
        """Aplica el IVA al precio de este producto."""
        raise NotImplementedError("TODO 7.2")

    def __str__(self):
        """Devuelve "{nombre} ({precio:.2f})"."""
        raise NotImplementedError("TODO 7.3")

    def __lt__(self, otro):
        """Define el operador < comparando precios."""
        raise NotImplementedError("TODO 7.4")

    def __eq__(self, otro):
        """Define el operador == comparando nombre y precio."""
        raise NotImplementedError("TODO 7.5")


def _main(ejercicios):
    import inspect

    for ej in ejercicios:
        print("=" * 62)
        nombre = getattr(ej, "__name__", "lambda")
        print(nombre, "->", (inspect.getdoc(ej) or "").strip())
        try:
            print("    ", ej())
        except NotImplementedError:
            print("     [PENDIENTE] aun no lo has escrito")
        except Exception as exc:
            print(f"     [ERROR] {type(exc).__name__}: {exc}")


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