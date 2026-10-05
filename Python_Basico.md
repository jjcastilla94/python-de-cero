# Python Básico — guía completa con definiciones y ejemplos

> Documento de referencia. Cada sección tiene: **definición** → **ejemplo** → **comentario**.
> Todos los ejemplos son ejecutables con `python archivo.py`.

---

## 1. ¿Qué es Python?

**Definición:** Python es un lenguaje de programación **interpretado**, **dinámicamente tipado**, de **alto nivel** y con **sintaxis legible**. Fue creado por Guido van Rossum en 1991.

Características clave:
- **Interpretado**: no se compila a código máquina; lo ejecuta un intérprete línea a línea.
- **Tipado dinámico**: el tipo se deduce en tiempo de ejecución, no se declara.
- **Multi-paradigma**: soporta orientación a objetos, funcional y procedural.
- **Multiplataforma**: Windows, Linux, macOS, web, móvil, IoT.

```python
# No necesitas declarar el tipo
x = 10      # int
x = "10"    # ahora es str, Python lo permite
print(x)   # 10
```

---

## 2. Instalación y Primeros Pasos

**Definición:** El intérprete de Python se instala desde [python.org](https://python.org). En la instalación marca **"Add Python to PATH"**.

Comandos básicos en terminal:

```bash
python --version      # muestra la versión instalada
python main.py        # ejecuta un archivo
pip install numpy    # instala una librería externa
```

Estructura mínima de un programa:

```python
# main.py
print("Hola mundo")   # imprime en consola
```

`print()` acepta varios argumentos y separador:

```python
print("Hola", "Mundo", sep="-")     # Hola-Mundo
print("Hola", "Mundo", end="!\n")   # Hola Mundo!
```

---

## 3. Comentarios

**Definición:** Texto que Python ignora. Sirve para documentar el código.

```python
# Comentario de una línea

# Comentario
# de varias líneas

"""
Docstring: comentario de bloque.
Se usa para documentar funciones y clases.
Es la única forma de "comentario" oficial.
"""

print("Esto sí se ejecuta")   # Esto NO se ejecuta
```

---

## 4. Variables y Tipos de Datos

**Definición:** Una **variable** es un espacio en memoria con un nombre que almacena un valor. Python usa **snake_case** por convención.

### 4.1 Tipos básicos

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `int` | Número entero | `edad = 25` |
| `float` | Número decimal | `precio = 19.99` |
| `str` | Texto (entre comillas) | `nombre = "Ana"` |
| `bool` | Verdadero o falso | `activo = True` |
| `None` | Ausencia de valor | `resultado = None` |
| `complex` | Número complejo | `z = 3 + 2j` |

```python
edad = 25
precio = 19.99
nombre = "Ana"
activo = True
vacio = None

print(type(edad))    # <class 'int'>
print(type(precio))  # <class 'float'>
print(type(nombre))  # <class 'str'>
```

### 4.2 Reglas para nombres de variables

- Empiezan con letra o `_`.
- Pueden contener letras, dígitos y `_`.
- No pueden empezar con número.
- No son palabras reservadas (`if`, `for`, `class`...).

```python
_mi_variable = 1      # válido
Variable2 = 2         # válido (pero usa minúsculas por convención)
# 2variable = 3       # ERROR: empieza con número
```

### 4.3 Múltiples asignaciones

```python
a = b = c = 0
x, y, z = 1, 2, 3
a, b = b, a          # intercambio (swap)

print(x, y, z)       # 1 2 3
```

### 4.4 Constantes

**Definición:** Aunque Python no las impone, se escriben en MAYÚSCULAS para valores que no deben cambiar.

```python
PI = 3.14159
MAX_INTENTOS = 3
```

---

## 5. Operadores

### 5.1 Aritméticos

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `+` | Suma / concatena | `5 + 3` / `"a" + "b"` | `8` / `"ab"` |
| `-` | Resta | `5 - 3` | `2` |
| `*` | Multiplicación | `5 * 3` | `15` |
| `/` | División real | `5 / 2` | `2.5` |
| `//` | División entera | `5 // 2` | `2` |
| `%` | Módulo (resto) | `5 % 2` | `1` |
| `**` | Potencia | `5 ** 2` | `25` |

```python
print(10 / 3)    # 3.3333333333333335
print(10 // 3)   # 3
print(10 % 3)    # 1
print(2 ** 10)   # 1024
```

### 5.2 De asignación

```python
x = 10
x += 5    # x = x + 5  -> 15
x -= 3    # 12
x *= 2    # 24
x /= 4    # 6.0
x //= 2   # 3
x %= 2    # 1
x **= 3   # 1
```

### 5.3 De comparación

**Definición:** Devuelven `True` o `False`.

```python
print(5 == 5)    # True  (igualdad)
print(5 != 5)    # False (desigualdad)
print(5 > 3)     # True  (mayor)
print(5 >= 5)    # True  (mayor o igual)
print(5 < 3)     # False (menor)
print(5 <= 3)    # False (menor o igual)
```

### 5.4 Lógicos

**Definición:** `and`, `or`, `not` combinan condiciones.

```python
edad = 20
tiene_cedula = True

# and: ambas deben ser True
puede_entrar = edad >= 18 and tiene_cedula
print(puede_entrar)   # True

# or: al menos una debe ser True
puede_oferta = edad >= 18 or edad == 16
print(puede_oferta)    # True

# not: invierte el valor
print(not puede_entrar)   # False
```

### 5.5 Pertenencia y identidad

```python
print("a" in "hola")        # True
print(3 in [1, 2, 3])       # True
print(3 not in [1, 2])      # True

# is compara identidad (referencia de memoria)
a = [1, 2]
b = a
print(a is b)     # True
print(a is [1, 2])  # False (distinto objeto)
```

---

## 6. Estructuras de Control

### 6.1 Condicionales

**Definición:** Ejecutan un bloque de código **solo si** se cumple una condición.

```python
edad = 22

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

Condición en una sola línea (ternario):

```python
estado = "mayor" if edad >= 18 else "menor"
print(estado)
```

### 6.2 Bucles

**Definición:** Repiten un bloque de código.

#### `for` — repetir sobre una secuencia

```python
# sobre un rango
for i in range(5):
    print(i)          # 0 1 2 3 4

# sobre una lista
frutas = ["manzana", "naranja", "plátano"]
for fruta in frutas:
    print(fruta)

# con índice
for i, fruta in enumerate(frutas):
    print(i, fruta)   # 0 manzana / 1 naranja / 2 plátano
```

`range()` variantes:

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(5, 0, -1)   # 5, 4, 3, 2, 1  (cuenta atrás)
```

#### `while` — repetir mientras la condición sea True

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

#### Control del flujo dentro del bucle

```python
for i in range(10):
    if i == 3:
        continue     # salta a la siguiente iteración
    if i == 6:
        break        # termina el bucle
    print(i)
# imprime 0 1 2 4 5
```

| Palabra | Efecto |
|---------|--------|
| `break` | Sale del bucle |
| `continue` | Salta a la siguiente vuelta |
| `else` | Se ejecuta si el bucle terminó sin `break` |
| `pass` | No hace nada (placeholder) |

```python
for i in range(3):
    print(i)
else:
    print("El bucle terminó normal")   # sí se ejecuta
```

---

## 7. Cadenas de Texto (Strings)

**Definición:** Una `str` es una secuencia **inmutable** de caracteres entre comillas simples `'`, dobles `"` o triples.

```python
nombre = "Ana"
apellido = 'Pérez'
completo = """Texto
multilínea"""
```

### 7.1 Concatenación y formateo

```python
# concatenación
saludo = "Hola " + nombre + "!"

# f-strings (forma moderna y recomendada)
edad = 25
print(f"{nombre} tiene {edad} años")

# format()
print("{} tiene {} años".format(nombre, edad))

# %
print("%s tiene %d años" % (nombre, edad))
```

### 7.2 Métodos útiles

```python
texto = "  Hola Mundo  "

print(texto.strip())        # "Hola Mundo"      (quita espacios)
print(texto.upper())       # "  HOLA MUNDO  "
print(texto.lower())       # "  hola mundo  "
print(texto.replace("Mundo", "Python"))
print(len(texto))          # 16  (longitud)
print(texto.split())       # ['Hola', 'Mundo']  (divide en lista)

# cortar en trozos
frases = ["a,b,c", "1,2,3"]
for f in frases:
    print(f.split(","))
```

Métodos más usados:

| Método | Función |
|--------|---------|
| `strip()` | Elimina espacios al inicio y final |
| `upper()` / `lower()` | Mayúsculas / minúsculas |
| `replace(a, b)` | Reemplaza subcadena |
| `split(sep)` | Divide en lista |
| `join(lista)` | Une una lista en un string |
| `find(x)` | Índice de la subcadena o `-1` |
| `startswith(x)` / `endswith(x)` | Verifica inicio/fin |
| `isdigit()` / `isalpha()` | Valida tipo de contenido |

```python
print("-".join(["a", "b", "c"]))   # a-b-c
print("123".isdigit())             # True
print("abc".isalpha())             # True
```

### 7.3 Indexación y rebanadas (slicing)

**Definición:** El primer índice es `0`, el último es `-1`. El corte es `[inicio:fin:salto]`.

```python
palabra = "Python"

print(palabra[0])     # P
print(palabra[-1])    # n
print(palabra[0:3])   # Pyt
print(palabra[:4])    # Pyth
print(palabra[2:])    # thon
print(palabra[::2])   # Pto  (cada 2)
print(palabra[::-1])  # nohtyP  (invertir)
```

---

## 8. Listas

**Definición:** Una **lista** es una colección **ordenada, mutable** y admite valores de distintos tipos.

```python
lista = [1, 2, 3, "cuatro", 5.0, True]
```

### 8.1 Acceso y modificación

```python
print(lista[0])      # 1
lista[0] = 100       # modificar
lista.append(6)      # agregar al final -> [100, 2, 3, 'cuatro', 5.0, True, 6]
lista.insert(0, 0)   # insertar al inicio
lista.remove(100)    # elimina la primera coincidencia
ultimo = lista.pop() # elimina y devuelve el último
```

### 8.2 Métodos comunes

| Método | Función |
|--------|---------|
| `append(x)` | Agrega al final |
| `insert(i, x)` | Inserta en la posición `i` |
| `remove(x)` | Elimina la primera aparición |
| `pop(i)` | Elimina y devuelve el elemento |
| `sort()` | Ordena ascendente |
| `sort(reverse=True)` | Ordena descendente |
| `reverse()` | Invierte el orden |
| `index(x)` | Posición de un elemento |
| `count(x)` | Cuántas veces aparece |
| `clear()` | Vacía la lista |
| `copy()` | Copia la lista |

```python
numeros = [5, 3, 8, 1, 3]
numeros.sort()
print(numeros)              # [1, 3, 3, 5, 8]
numeros.sort(reverse=True)
print(numeros)              # [8, 5, 3, 3, 1]
print(numeros.index(5))     # 1
print(numeros.count(3))     # 2
```

### 8.3 Copia frente a referencia

```python
original = [1, 2, 3]

copia = original.copy()      # copia independiente
misma = original             # MISMA referencia (no es copia)

copia.append(4)
print(original)   # [1, 2, 3]  (no cambia)
print(misma)      # [1, 2, 3, 4] (sí cambia)
```

### 8.4 Comprensiones de listas

**Definición:** Crear listas a partir de un bucle en una sola línea.

```python
cuadrados = [i ** 2 for i in range(6)]
print(cuadrados)             # [0, 1, 4, 9, 16, 25]

pares = [i for i in range(10) if i % 2 == 0]
print(pares)                 # [0, 2, 4, 6, 8]

# equivalente con bucle normal
normal = []
for i in range(10):
    if i % 2 == 0:
        normal.append(i)
```

---

## 9. Tuplas

**Definición:** Una **tupla** es como una lista pero **inmutable**: no se puede modificar después de crearla.

```python
tupla = ("rojo", "verde", "azul")
print(tupla[0])       # rojo
# tupla[0] = "amarillo"   -> ERROR: no se puede asignar

# Se usa cuando los datos no deben cambiar
x, y = (10, 20)       # desempaquetado
print(x, y)           # 10 20
```

| Ventaja | Detalle |
|---------|---------|
| Seguridad | No puede alterarse por error |
| Velocidad | Más rápida que una lista |
| Uso como clave | Puede usarse en diccionarios (las listas no) |

---

## 10. Diccionarios

**Definición:** Un **diccionario** guarda pares **clave: valor**. Las claves son únicas e inmutables.

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

print(persona["nombre"])        # Ana
persona["edad"] = 26            # modificar
persona["email"] = "a@b.com"   # agregar
del persona["ciudad"]          # eliminar
```

### 10.1 Métodos comunes

```python
print(persona.keys())      # dict_keys([...])
print(persona.values())    # dict_values([...])
print(persona.items())     # pares clave-valor
print(persona.get("edad"))        # 26
print(persona.get("tel", "N/A"))  # N/A (valor por defecto)
print("nombre" in persona)         # True
```

```python
print(persona.get("edad", 0))   # si no existe, devuelve 0
persona.setdefault("pais", "España")  # agrega solo si no existe
```

### 10.2 Recorrer un diccionario

```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

```python
# solo claves
for clave in persona:
    print(clave)

# comprehension
nombres = {k: v for k, v in persona.items() if isinstance(v, str)}
```

### 10.3 Diccionario vs lista

| Necesitas | Usa |
|-----------|-----|
| Posiciones, orden fijo, valores repetidos | Lista |
| Buscar por nombre/etiqueta, datos con campos | Diccionario |

---

## 11. Conjuntos (Sets)

**Definición:** Colección **sin orden y sin elementos repetidos**. Muy útil para eliminar duplicados.

```python
s = {1, 2, 3, 3, 4}
print(s)          # {1, 2, 3, 4}  (el 3 duplicado se elimina)

s.add(5)
s.remove(1)
```

Operaciones entre conjuntos:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)   # {3, 4}        intersección
print(a | b)   # {1,2,3,4,5,6} unión
print(a - b)   # {1, 2}        diferencia
print(a ^ b)   # {1, 2, 5, 6}  simétrica

# eliminar duplicados de una lista
lista = [1, 1, 2, 3, 3, 4]
unicos = list(set(lista))
print(unicos)   # [1, 2, 3, 4] (el orden puede variar)
```

---

## 12. Funciones

**Definición:** Bloque de código reutilizable que recibe **parámetros** y puede devolver un **retorno**.

```python
def saludar(nombre, saludo="Hola"):
    """Función con parámetro por defecto."""
    return f"{saludo}, {nombre}!"

print(saludar("Ana"))                    # Hola, Ana!
print(saludar("Ana", saludo="Buenos días"))
```

### 12.1 Retorno múltiple

```python
def min_max(lista):
    return min(lista), max(lista)

menor, mayor = min_max([4, 9, 2])
print(menor, mayor)   # 2 9
```

### 12.2 `*args` y `**kwargs`

**Definición:** Permiten recibir un número variable de argumentos.

```python
def sumar(*numeros):
    return sum(numeros)
print(sumar(1, 2, 3))    # 6

def datos(**info):
    print(info)
datos(nombre="Ana", edad=25)   # {'nombre': 'Ana', 'edad': 25}
```

### 12.3 Funciones lambda (anónimas)

```python
cuadrado = lambda x: x ** 2
print(cuadrado(5))   # 25

# muy usadas con sort()
personas = [("Ana", 25), ("Luis", 30), ("Eva", 22)]
personas.sort(key=lambda p: p[1])
print(personas)   # [('Eva', 22), ('Ana', 25), ('Luis', 30)]
```

### 12.4 Scope (ámbito)

**Definición:** Una variable puede ser **local** (dentro de la función) o **global** (fuera de ella).

```python
contador = 0        # global

def incrementar():
    global contador  # modifica la global
    contador += 1
    local = 5        # local, solo existe aquí
```

---

## 13. Clases y Objetos (POO)

**Definición:** La **Programación Orientada a Objetos** modela entidades reales. Una **clase** es la plantilla; un **objeto** es una instancia.

```python
class Persona:
    # Método constructor: se llama al crear el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre     # atributo de instancia
        self.edad = edad

    # Método normal
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

    # Método estático: no usa self
    @staticmethod
    def es_mayor(edad):
        return edad >= 18

# Crear objetos
ana = Persona("Ana", 25)
print(ana.nombre)          # Ana
print(ana.saludar())       # Hola, soy Ana y tengo 25 años
print(Persona.es_mayor(20))  # True
```

### 13.1 Herencia

**Definición:** Una clase puede **heredar** atributos y métodos de otra.

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)   # llama al padre
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} estudia {self.carrera}"

e = Estudiante("Luis", 20, "Ingeniería")
print(e.saludar())    # método heredado
print(e.estudiar())
```

### 13.2 Otros conceptos

| Concepto | Significado |
|----------|-------------|
| `self` | Referencia al propio objeto |
| `cls` | Referencia a la clase (en métodos de clase) |
| `super()` | Llama al método del padre |
| `__str__` | Representación legible del objeto |
| `@property` | Convierte un método en atributo |
| `@classmethod` | Método ligado a la clase |
| `@staticmethod` | Método sin dependencia de clase u objeto |

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: {self.precio}€"

    @property
    def con_iva(self):
        return round(self.precio * 1.21, 2)

p = Producto("Camiseta", 20)
print(p)              # Camiseta: 20€
print(p.con_iva)      # 24.2
```

---

## 14. Manejo de Errores

**Definición:** `try/except` evita que el programa se detenga cuando ocurre un error.

```python
try:
    numero = int(input("Escribe un número: "))
    print(numero * 2)
except ValueError:
    print("Error: eso no es un número válido")
except Exception as e:
    print(f"Ocurrió otro error: {e}")
else:
    print("Todo salió bien")
finally:
    print("Este bloque SIEMPRE se ejecuta")
```

Lanzar errores propios:

```python
def edad_valida(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

try:
    edad_valida(-5)
except ValueError as e:
    print(e)     # La edad no puede ser negativa
```

---

## 15. Entrada de usuario

**Definición:** `input()` siempre devuelve una **cadena** (`str`).

```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}")

# Convertir a número
edad = int(input("¿Qué edad tienes? "))
altura = float(input("¿Tu altura en metros? "))
```

```python
# Validación: no salir del bucle hasta tener un número válido
while True:
    try:
        edad = int(input("Edad: "))
        break
    except ValueError:
        print("Introduce un número válido")
```

---

## 16. Archivos

**Definición:** Permiten leer y escribir datos persistidos. Se usan con `with`, que cierra el archivo automáticamente.

```python
# Escribir
with open("notas.txt", "w") as f:
    f.write("Ana: 9\n")
    f.write("Luis: 8\n")

# Leer
with open("notas.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# Leer línea por línea
with open("notas.txt", "r") as f:
    for linea in f:
        print(linea.strip())

# Modos de apertura
# "r"  lectura (error si no existe)
# "w"  escritura (borra el archivo)
# "a"  añadir al final
# "x"  crear (error si ya existe)
# "r+" lectura y escritura
```

```python
# CSV simple
with open("datos.csv", "w") as f:
    f.write("nombre,edad\nAna,25\nLuis,30\n")

import csv
with open("datos.csv", newline="") as f:
    for fila in csv.reader(f):
        print(fila)
```

---

## 17. Módulos yPaquetes

**Definición:** Un **módulo** es un archivo `.py`. Un **paquete** es una carpeta con varios módulos.

### 17.1 Importar

```python
import math
print(math.sqrt(16))          # 4.0
print(math.pi)                # 3.141592653589793

from math import sqrt, pi     # importar elementos concretos
print(sqrt(9))

import math as m              # con alias
print(m.floor(3.7))          # 3

# Módulos estándar útiles
import random
print(random.randint(1, 6))       # número aleatorio 1-6
print(random.choice(["a","b"]))
random.shuffle(lista)

import datetime
hoy = datetime.date.today()
print(hoy)

import os
print(os.getcwd())               # directorio actual
print(os.path.exists("main.py"))
```

### 17.2 Instalar paquetes externos

```bash
pip install requests
pip install pandas numpy
pip list
```

```python
import requests
respuesta = requests.get("https://api.example.com/datos")
datos = respuesta.json()
```

---

## 18. Funciones de orden superior

**Definición:** Funciones que reciben o devuelven **otras funciones**.

```python
def duplicar(x):
    return x * 2

def aplicar(f, valor):
    return f(valor)

print(aplicar(duplicar, 5))   # 10
print(aplicar(lambda x: x + 1, 5))   # 6
```

`map()`, `filter()`, `reduce()`:

```python
numeros = [1, 2, 3, 4, 5]

# map: transforma cada elemento
print(list(map(lambda x: x ** 2, numeros)))     # [1, 4, 9, 16, 25]

# filter: mantiene los que cumplen la condición
print(list(filter(lambda x: x % 2 == 0, numeros)))  # [2, 4]

# reduce: acumula
from functools import reduce
print(reduce(lambda a, b: a + b, numeros))      # 15
```

Ordenar con clave personalizada:

```python
palabras = ["banana", "uva", "kiwi"]
palabras.sort(key=len)              # por longitud
palabras.sort(key=str.lower)        # alfabéticamente sin distinguir mayúsculas
```

---

## 19. Programación Orientada a Objetos —heritance múltiple (avanzado)

**Definición:** Una clase puede heredar de **varias** clases.

```python
class Volador:
    def volar(self):
        return "Volando"

class Nadador:
    def nadar(self):
        return "Nadando"

class Anfibio(Volador, Nadador):
    pass

a = Anfibio()
print(a.volar(), a.nadar())   # Volando Nadando
```

---

## 20. Decoradores (concepto)

**Definición:** Una función que recibe otra función y la envuelve, añadiendo comportamiento.

```python
def decorador(funcion):
    def envoltura(*args, **kwargs):
        print("Antes de llamar")
        resultado = funcion(*args, **kwargs)
        print("Después de llamar")
        return resultado
    return envoltura

@decorador
def saludar():
    print("Hola")

saludar()
```

Salida:
```
Antes de llamar
Hola
Después de llamar
```

---

## 21. Buenos Hábitos (PEP 8)

| Regla | Ejemplo |
|-------|---------|
| Nombres en `snake_case` | `mi_variable`, `nombre_persona` |
| Clases en `PascalCase` | `MiClase`, `Persona` |
| Constantes en `MAYUSCULAS` | `MAX_INTENTOS` |
| 4 espacios de indentación | nunca tabulaciones |
| Línea máx. ~79 caracteres | divide líneas largas |
| Comentarios en español/inglés consistente | — |

```python
# Bien
def calcular_promedio(notas):
    total = sum(notas)
    cantidad = len(notas)
    return total / cantidad if cantidad else 0

# Mal
def CalcularPromedio(notas):
    return sum(notas)/len(notas)
```

---

## 22. Ejemplo completo integrado

```python
"""Sistema de gestión de contactos."""

class Contacto:
    def __init__(self, nombre, email, telefono=""):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} <{self.email}>"

    def es_valido(self):
        return "@" in self.email


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, contacto):
        if not contacto.es_valido():
            raise ValueError(f"Email inválido: {contacto.email}")
        self.contactos.append(contacto)
        print(f"[OK] {contacto.nombre} agregado")

    def buscar(self, texto):
        texto = texto.lower()
        return [c for c in self.contactos
                if texto in c.nombre.lower() or texto in c.email.lower()]

    def __len__(self):
        return len(self.contactos)


def main():
    agenda = Agenda()

    try:
        agenda.agregar(Contacto("Ana", "ana@mail.com", "600111222"))
        agenda.agregar(Contacto("Luis", "luis@mail.com"))
        agenda.agregar(Contacto("Malo", "correo-invalido"))
    except ValueError as e:
        print(f"[ERROR] {e}")

    print("\nContactos:", len(agenda))
    resultados = agenda.buscar("a")
    for c in resultados:
        print(" -", c)


if __name__ == "__main__":
    main()
```

Salida esperada:
```
[OK] Ana agregado
[OK] Luis agregado
[ERROR] Email inválido: correo-invalido

Contactos: 2
 - Ana <ana@mail.com>
```

---

## 23. Errores comunes de principiante

| Error | Causa | Solución |
|-------|-------|----------|
| `TypeError: can only concatenate str` | Mezclar tipos con `+` | Usa f-strings |
| `ValueError: invalid literal for int()` | `int("abc")` | Usa `try/except` o `str.isdigit()` |
| `NameError: name 'x' is not defined` | Usar variable antes de crearla | Revisa el orden de las líneas |
| `IndentationError` | Mezclar tabulaciones y espacios | Usa siempre 4 espacios |
| `IndexError: list index out of range` | Índice mayor que la lista | `range(len(lista))` |
| Bucle infinito | Falta actualizar la condición | Revisa el `+=` o `break` |
| Imprimir dentro de un bucle innecesario | `print` dentro de `for` en listas grandes | Acumula y imprime al final |

---

## 24. Glosario rápido

| Término | Significado |
|---------|-------------|
| **Algoritmo** | Secuencia ordenada de pasos para resolver un problema |
| **Variable** | Nombre que referencia un valor en memoria |
| **Tipo** | Clasificación de un valor (`int`, `str`...) |
| **Expresión** | Fragmento de código que produce un valor |
| **Sentencia** | Instrucción completa (termina en `:` o fin de línea) |
| **Bloque** | Grupo de líneas indentadas |
| **Función** | Bloque de código reutilizable |
| **Clase** | Plantilla para crear objetos |
| **Objeto** | Instancia concreta de una clase |
| **Módulo** | Archivo `.py` con código reutilizable |
| **Paquete** | Carpeta que agrupa módulos |
| **Iteración** | Una vuelta de un bucle |
| **Excepción** | Error en tiempo de ejecución |
| **Indentación** | Sangría que define el bloque |

---

## 25. Recursos para seguir aprendiendo

- Documentación oficial (español): <https://docs.python.org/es/3/>
- Ejercicios interactivos: <https://www.w3schools.com/python/>
- Ejercicios con mentoría: <https://exercism.org/tracks/python>
- Retos de programación: <https://codewars.com>
- Curso gratuito de Python en español: <https://www.cursus.org/>

---

## 26. Cómo estudiar con este documento

1. No lo leas entero de una vez: úsalo como **referencia** mientras haces los
   ejercicios de `ejercicios/`.
2. Cada sección tiene el formato *definición → ejemplo → comentario*, así que
   puedes leer solo el ejemplo si ya conoces el concepto.
3. Si un ejemplo no se ejecuta como esperas, comprueba tu versión de Python y
   abre una issue describiendo el caso.
4. Cuando termines el tema 11, vuelve aquí para repasar las secciones que más
   se te olvidan (suelen ser *slicing*, comprensiones y `*args`/`**kwargs`).

---

*Material del repositorio `python-de-cero`. Licencia MIT: si lo reutilizas,
cita la fuente.*
