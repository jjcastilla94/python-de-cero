message="GG"

print("Hola mundo " + message)


# Ejercicio 1

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
		print("Operación no válida")

