message = "GG"

print("Hola mundo " + message)


# Ejercicio 1: calculadora basica
# OJO: el "match" es una sentencia nueva de Python 3.10+.
# En versiones anteriores se hace con if / elif / else.

print("Dime un numero: ")
numero1 = int(input())
print("Dime otro numero")
numero2 = int(input())

print("Que operacion hacemos?")
operation = input()

match operation:
    case "+":
        print(numero1 + numero2)
    case "-":
        print(numero1 - numero2)
    case "*":
        print(numero1 * numero2)
    case "/":
        print(numero1 / numero2)
    case _:
        print("Operacion no valida")