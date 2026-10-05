# Guia de ejercicios de Python basico

Practica tema por tema todo lo explicado en la chuleta `../Python_Basico.md`.
Cada tema tiene **dos archivos**:

| Archivo | Para que sirve |
|---------|----------------|
| `01_variables_y_tipos.py` | los ejercicios: completa cada `TODO` |
| `soluciones/01_variables_y_tipos_solucion.py` | la respuesta comentada para comparar |

## Como se trabaja

1. Ejecuta el ejercicio: `python 01_variables_y_tipos.py`
2. Cada funcion pendiente lanza `NotImplementedError`, asi que el runner
   muestra `[PENDIENTE]` sin romperse.
3. Escribe el codigo (**borra el `raise NotImplementedError(...)`**).
4. Vuelve a ejecutar y compara tu resultado con el esperado en el comentario.
5. Cuando termines, mira la solucion del mismo tema y lee sus comentarios.
6. Repite con el siguiente tema en orden: los ultimos usan los anteriores.

## Orden recomendado

```
01_variables_y_tipos.py          tipos, conversion, f-strings
02_operadores.py                 aritmeticos, comparacion, logicos, is vs ==
03_condicionales.py              if / elif / else, ternario, fizzbuzz
04_bucles.py                     for, while, range, enumerate, zip, break, continue
05_cadenas.py                    indexacion, slicing, metodos de str
06_listas.py                     metodos, comprensiones, copia vs referencia
07_tuplas_diccionarios_sets.py   datos con clave, sin duplicados, comparaciones
08_funciones.py                 args, **kwargs, recursividad, lambda, map/filter
09_poo.py                        clases, properties, herencia, super()
10_errores_archivos.py           try/except/raise, with open, modulos estandar
11_reto_biblioteca.py            reto final: todo junto + menu por consola
```

## Comprobacion rapida

Para ver que las soluciones siguen funcionando:

```bash
python verificar_soluciones.py
```

## Como contribuir

Este repositorio es abierto: si encuentras una errata, un ejercicio que se puede
mejorar o te falta un tema, puedes añadirlo tu mismo. Lee
[\CONTRIBUTING.md\](../CONTRIBUTING.md) para conocer el estilo de codigo que se
revisa (4 espacios, \snake_case\, comentarios en espanol) y los pasos para abrir
un pull request.

## Tips

- Escribe primero el ejemplo del comentario y luego quita los espacios.
- Si te atascas mas de 5 minutos, mira solo el comentario del ejercicio
  (la solucion esta a un archivo de distancia).
- No copies y pegues: escribe el codigo aunque consultes el resultado.
- Los errores son mensajes: `[ERROR] TypeError: ...` te dice que buscar.
- Repite los temas rapidos (01-04) cada semana durante 10 minutos: la
  memorizacion viene de la repeticion espaciada, no de leer una sola vez.