# Cómo contribuir

¡Gracias por querer mejorar este proyecto! Cualquier ayuda vale: una errata
corregida, un ejercicio nuevo o una explicación más clara.

Las contribuciones entran mediante **pull requests**. Sigue esta guía para que
tu trabajo sea fácil de revisar y de integrar.

---

## 1. Antes de empezar

- **Lee [`README.md`](README.md)** y [`ejercicios/GUIA_DE_EJERCICIOS.md`](ejercicios/GUIA_DE_EJERCICIOS.md) para entender la estructura.
- Revisa si tu idea ya está planteada en [las issues abiertas](https://github.com/jjcastilla94/python-de-cero/issues).
- Para cambios grandes (un tema nuevo completo, un motor de ejercicios),
  **abre primero una issue** y comenta tu propuesta: así evitamos que dos
  personas hagieran el mismo trabajo.

## 2. Reglas de estilo (obligatorias)

Se revisan las contribuciones con estos criterios, así que conviene cumplirlos:

| Elemento | Regla | Ejemplo |
|----------|-------|---------|
| Indentación | 4 espacios, **nunca** tabulaciones | `    return total` |
| Nombres de funciones y variables | `snake_case` en español o inglés, **consistente** | `contar_palabras` |
| Nombres de clases | `PascalCase` | `CuentaBancaria` |
| Constantes | `MAYUSCULAS_SIN_GUIONES_BAJOS` | `MAX_INTENTOS` |
| Línea | máximo 88 caracteres | parte las líneas largas |
| Idioma | **español**, con tildes y `ñ` correctas | "bisiesto", "número" |
| Comentarios | explican el **porqué**, no el qué | `# el % 10 da el último dígito` |
| Prints de depuración | fuera del código entregado | nada de `print("DEBUG")` |
| Imports | en la parte superior del archivo | `import math` |

Todo el código debe ser **ejecutable**: nada de pseudocódigo en los ejemplos.

## 3. Comprobaciones obligatorias antes de abrir el PR

```bash
# 1. ninguna solución debe mostrar [ERROR]
python ejercicios/verificar_soluciones.py

# 2. tu archivo debe compilar
python -m compileall ejercicios
python -m py_compile ejercicios/05_cadenas.py
```

Si tu contribución añade un tema nuevo, añade también su archivo en
`ejercicios/soluciones/` y su línea en la tabla del `README.md`.

## 4. Estructura de un ejercicio

Mantén el formato para que el repo sea homogéneo:

```python
def nombre_funcion(parametro):
    """
    Qué hace la función.

    Entrada:  nombre_funcion("Ana", 25) -> "Ana (25 años)"
    Pista:    usa f-strings
    """
    raise NotImplementedError("TODO n.n")
```

Y en el final del archivo, el runner:

```python
EJERCICIOS = [
    lambda: nombre_funcion("Ana", 25),
]

if __name__ == "__main__":
    _main(EJERCICIOS)
```

En la solución, los comentarios explican **por qué** esa es la forma correcta,
no solo **qué** hace.

## 5. Proceso de pull request

1. Crea una rama con un nombre claro:
   `git checkout -b fix/slicing-05`
2. Haz tus commits con mensajes descriptivos en español o inglés:
   `fix(cadenas): corrige el ejemplo de slicing negativo`
   Tipos usados: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
3. Sube la rama: `git push origin fix/slicing-05`
4. Abre el PR contra `main` usando la plantilla y describe:
   - **Qué** cambias y **por qué**
   - **Cómo** lo has verificado
   - Relación con el número de issue (`#12`), si aplica
5. Responde a la revisión con calma: los cambios son decisiones del proyecto,
   no un ataque personal.

## 6. Tipos de contribución que buscamos

- 📝 **Correcciones**: erratas, ejemplos que no funcionan, enlaces rotos.
- 🧩 **Ejercicios nuevos**: otro ejercicio para un tema existente.
- 🆕 **Tema nuevo**: hay que añadir la sección en la chuleta, los ejercicios,
  la solución, la fila en la tabla del README y la entrada en el CHANGELOG.
- 💡 **Mejor pedagogía**: explicaciones más claras, más pistas, casos límite.
- 🧪 **Herramientas**: más comprobaciones, nuevos runners, traducciones.

## 7. Conducta

Al participar aceptas el [código de conducta](CODE_OF_CONDUCT.md).
Si presumes conducta inapropiada, abre una issue o escribe a los mantenedores.

## 8. Preguntas

¿Dudas sobre el contenido? Abre una
[issue de discusión](https://github.com/jjcastilla94/python-de-cero/issues/new/choose).
¡No hace falta que sepas la respuesta para preguntar!