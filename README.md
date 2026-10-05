# python-de-cero

[![Python](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![Licencia](https://img.shields.io/badge/licencia-MIT-green.svg)](LICENSE)
[![CI](https://github.com/jjcastilla94/python-de-cero/actions/workflows/ci.yml/badge.svg)](https://github.com/jjcastilla94/python-de-cero/actions/workflows/ci.yml)
[![Código de conducta](https://img.shields.io/badge/c%C3%B3digo%20de%20conducta-Contributor%20Covenant-violet.svg)](CODE_OF_CONDUCT.md)

> **Guía de referencia y ejercicios de Python en español.**
> Una chuleta con los 25 temas básicos, 11 bloques de ejercicios comentados con
> sus soluciones y un reto final tipo proyecto para comprobar que lo sabes hacer.

[![Estrellas](https://img.shields.io/github/stars/jjcastilla94/python-de-cero?style=social)](https://github.com/jjcastilla94/python-de-cero/stargazers)
[![Forks](https://img.shields.io/github/forks/jjcastilla94/python-de-cero?style=social)](https://github.com/jjcastilla94/python-de-cero/network/members)
[![Issues](https://img.shields.io/github/issues/jjcastilla94/python-de-cero)](https://github.com/jjcastilla94/python-de-cero/issues)

---

## Por qué existe este repositorio

La mayoría de tutoriales de Python en español tienen dos problemas: o son
larguísimos y no se pueden repasar, o son tan cortos que no cubren lo que un
entrevista te pregunta. Este repo busca el punto medio:

1. **Una chuleta (`Python_Basico.md`)**: todo lo básico en un solo archivo,
   con definición y ejemplo mínimo por concepto. Se consulta, no se memoriza.
2. **Ejercicios por temas (`ejercicios/`)**: 11 bloques ordenados, del
   `print("hola")` a la POO, cada uno con el enunciado comentado y su
   solución explicada línea a línea.
3. **Un reto final (`11_reto_biblioteca.py`)**: una biblioteca completa con
   clases, herencia, properties, validación, persistencia en JSON y menú por
   consola. Todo lo anterior se usa aquí.

Cero dependencias externas: solo la librería estándar de Python.
Idiomatico, portable y ejecutable tal cual.

---

## Estructura del repositorio

```
.
├── README.md                       Este archivo (resumen del proyecto)
├── LICENSE                         Licencia MIT
├── CHANGELOG.md                    Historial de versiones
├── CONTRIBUTING.md                 Cómo colaborar
├── CODE_OF_CONDUCT.md              Conducta esperada
├── SECURITY.md                     Cómo reportar problemas de seguridad
├── Python_Basico.md                Chuleta de referencia (25 secciones)
├── main.py                         Programa de prueba inicial
└── ejercicios/
    ├── GUIA_DE_EJERCICIOS.md       Guía de uso de los ejercicios
    ├── 01_variables_y_tipos.py     Un archivo por tema (con TODO)
    ├── 02_operadores.py
    ├── 03_condicionales.py
    ├── 04_bucles.py
    ├── 05_cadenas.py
    ├── 06_listas.py
    ├── 07_tuplas_diccionarios_sets.py
    ├── 08_funciones.py
    ├── 09_poo.py
    ├── 10_errores_archivos.py
    ├── 11_reto_biblioteca.py       Reto final tipo proyecto
    ├── verificar_soluciones.py     Comprueba que las soluciones funcionan
    └── soluciones/                 Un archivo de solución por tema
```

---

## Inicio rápido

```bash
# 1. el hola mundo
python main.py

# 2. un tema de ejercicios (los TODO muestran [PENDIENTE])
python ejercicios/01_variables_y_tipos.py

# 3. comprobar que todas las soluciones siguen funcionando
python ejercicios/verificar_soluciones.py

# 4. el reto final (menú interactivo)
python ejercicios/11_reto_biblioteca.py
```

Requisitos: **Python 3.14 o superior**. Todo el material está probado en esa
versión, que es la mínima documentada (y la recomendada para este proyecto).
Nada de `pip install`.

---

## Los 11 temas

| # | Tema | Qué se practica |
|---|------|-----------------|
| 01 | Variables y tipos | `int` `float` `str` `bool` `None`, conversión, f-strings |
| 02 | Operadores | aritméticos, de asignación, comparación, lógicos, `is` vs `==` |
| 03 | Condicionales | `if` `elif` `else`, ternario, `fizzbuzz` |
| 04 | Bucles | `for` `while` `range` `enumerate` `zip` `break` `continue` `for-else` |
| 05 | Cadenas | indexación, *slicing*, métodos de `str` |
| 06 | Listas | métodos, comprensiones, copia vs referencia |
| 07 | Tuplas, diccionarios y sets | datos con clave, duplicados, operaciones de conjuntos |
| 08 | Funciones | parámetros por defecto, `*args`, `**kwargs`, recursión, `lambda`, `map`/`filter`/`reduce` |
| 09 | POO | clases, `self`, `@property`, herencia, `super()`, `__str__`, `__eq__` |
| 10 | Errores y archivos | `try`/`except`/`finally`, `raise`, `with open`, `math` `json` `csv` `re` |
| 11 | Reto final | una biblioteca completa con menú por consola |

Cada tema sigue la misma estructura: **enunciado comentado → solución comentada**.
En `GUIA_DE_EJERCICIOS.md` tienes el ritmo de trabajo recomendado (~30 min por tema).

---

## Cómo se trabaja un tema

1. Lee la sección correspondiente de [`Python_Basico.md`](Python_Basico.md).
2. Ejecuta el ejercicio: `python ejercicios/04_bucles.py`.
3. Implementa cada función (los pendientes lanzan `NotImplementedError` y el
   runner los marca como `[PENDIENTE]` en vez de romperse).
4. Compara con la solución de `ejercicios/soluciones/` y lee sus comentarios.
5. Vuelve a ejecutar y comprueba que no queda ningún `[PENDIENTE]`.

---

## Cómo contribuir

Todas las contribuciones son bienvenidas: corrección de erratas, nuevos
ejercicios, mejores explicaciones, traducciones o herramientas.

```bash
git clone https://github.com/jjcastilla94/python-de-cero.git
cd python-de-cero
# ... haz tus cambios ...
python ejercicios/verificar_soluciones.py   # debe salir "todas OK"
git add . && git commit -m "docs: aclara slicing en 05_cadenas"
git push origin mi-rama
```

Lee [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de abrir tu primer PR.

---

## Estado del proyecto

- [x] Chuleta de referencia (25 secciones)
- [x] 11 bloques de ejercicios con soluciones
- [x] Reto final tipo proyecto
- [x] CI que verifica las soluciones en Python 3.14
- [ ] Ejercicios de nivel intermedio (algoritmos, diccionarios anidados)
- [ ] Sección de NumPy, Pandas y `scikit-learn`
- [ ] Traducción de la chuleta al inglés

¿Falta algo? [Abre una issue](https://github.com/jjcastilla94/python-de-cero/issues/new/choose).

---

## Licencia

Este proyecto se publica bajo la licencia **MIT**: puedes usarlo, modificarlo y
distribuirlo libremente. Ver [`LICENSE`](LICENSE) para el texto completo.

Si prefieres que el contenido educativo (los `.md`) se reutilice bajo condiciones
de atribución, la alternativa habitual es dual: **código MIT + documentación
CC BY 4.0**.

---

## Créditos y origen

Nació como material de trabajo de la **Unidad 01 de un curso de programación con
IA** y se abrió a la comunidad. Si te sirve, una estrella ayuda a que otras
personas lo encuentren.

---

<p align="center">
  Hecho con <code>chuletas</code>, ejercicios y <code>print()</code> · Python 3.14
</p>