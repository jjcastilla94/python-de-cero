# Changelog

Todas las novedades de este proyecto se registran aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado es [SemVer](https://semver.org/lang/es/): `MAJOR.MINOR.PATCH`.

- **MAJOR**: cambios incompatibles (por ejemplo, renombrar archivos o cambiar
  el formato de los ejercicios).
- **MINOR**: nuevos temas o ejercicios.
- **PATCH**: correcciones de erratas y del texto.

---

## [No publicado]

### Añadido
- *Pendiente de la primera contribución.*

---

## [0.1.0] — 2026-10-05

### Añadido
- **Chuleta de referencia** `Python_Basico.md` con 25 secciones: variables y
  tipos, operadores, condicionales, bucles, cadenas, listas, tuplas,
  diccionarios, conjuntos, funciones, POO, manejo de errores, archivos,
  módulos, funciones de orden superior, decoradores, PEP 8, ejemplo integrado,
  errores comunes y glosario.
- **11 bloques de ejercicios** en `ejercicios/`, uno por tema, con el enunciado
  comentado y un runner que marca los pendientes como `[PENDIENTE]`.
- **11 soluciones comentadas** en `ejercicios/soluciones/`, que explican el
  porqué de cada decisión.
- **Reto final** `11_reto_biblioteca.py`: clases, herencia, `@property`,
  validación con `ValueError`, persistencia en JSON y menú por consola.
- **Verificador automático** `ejercicios/verificar_soluciones.py`, que ejecuta
  todas las soluciones y falla si alguna produce un error.
- **Guía de ejercicios** `ejercicios/GUIA_DE_EJERCICIOS.md` con el orden
  recomendado y el ritmo de trabajo.
- **Documentación de comunidad**: `README.md`, `CONTRIBUTING.md`,
  `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` (MIT) y `CHANGELOG.md`.
- **Integración continua** con GitHub Actions: comprueba la sintaxis de todos los
  archivos y verifica las soluciones en Python 3.14.
- La versión mínima documentada es **Python 3.14**: es la versión con la que se
  ha probado todo el material. `main.py` usa además la sentencia `match`.

### Notas
- El proyecto no tiene dependencias externas: solo librería estándar.
- Nació como material de la Unidad 01 de un curso de programación con IA.

[No publicado]: https://github.com/jjcastilla94/python-de-cero/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/jjcastilla94/python-de-cero/releases/tag/v0.1.0