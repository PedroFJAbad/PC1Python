# Leer dos números ingresados por el usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú y obtener la opción del usuario
print("1. Sumar los dos números")
print("2. Restar los dos números (el primero menos el segundo)")
print("3. Multiplicar los dos números")
opcion = input("Elija una opción (1/2/3): ")

# Realizar la operación correspondiente según la opción elegida
if opcion == "1":
    resultado = num1 + num2
    print("La suma de los dos números es:", int(resultado) if resultado.is_integer() else resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("La resta de los dos números es:", int(resultado) if resultado.is_integer() else resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("La multiplicación de los dos números es:", int(resultado) if resultado.is_integer() else resultado)
else:
    print("Opción no válida. Por favor, elija una opción válida (1/2/3).")