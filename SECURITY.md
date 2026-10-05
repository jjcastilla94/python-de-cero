# Política de seguridad

## Qué cubre este proyecto

Este repositorio es material educativo: una chuleta de referencia y ejercicios
con soluciones comentadas. **No contiene código de producción** ni datos de
usuarios, así que el riesgo de seguridad es bajo por naturaleza.

Aun así, hay un tipo de problema que sí merece atención: si un ejercicio o una
solución contiene un ejemplo que **enseña una práctica insegura** (por ejemplo,
`eval()` sobre lo que escribe el usuario, una contraseña en el código o una
descarga sin `verify=False`), eso puede provocar que otras personas copien una
debilidad a su código.

## Cómo reportar un problema

1. Abre una [issue privada de seguridad](https://github.com/jjcastilla94/python-de-cero/security/advisories/new)
   (pestaña **Security → Report a vulnerability**).
2. Describe qué archivo y qué línea, y por qué es un problema.
3. También puedes escribir por correo a los mantenedores si prefieres no usar
   la plataforma.

Nos comprometemos a responder en un plazo razonable y a crédito del reporte en
el CHANGELOG, salvo que prefieras mantener el anonimato.

## Qué no se considera vulnerabilidad

- Erratas ortográficas o gramaticales.
- Un ejemplo que no funciona como se espera (usa las issues normales).
- Que propongamos un enfoque pedagógico distinto al tuyo.
- La ausencia de un tema en la chuleta.

## Buenas prácticas que recomendamos

Aunque sea material de aprendizaje, los ejemplos siguen estas pautas:

- Nunca escribir claves, tokens ni contraseñas en el código.
- Preferir `with open(...)` para no dejar archivos abiertos.
- Validar siempre la entrada del usuario antes de convertirla
  (`int(input())` sin `try` es un problema didáctico, no de seguridad).
- Comentarios que animen a `eval()`, `exec()` o `pickle` con datos externos.