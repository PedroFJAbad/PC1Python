# Solicitar al usuario que ingrese un entero positivo
N = int(input("Ingrese un entero positivo: "))

# Calcular la suma de los enteros desde 1 hasta N
suma = 0
for i in range(1, N + 1):
    suma += i

# Mostrar la suma de los enteros desde 1 hasta N
print("La suma de los enteros desde 1 hasta", N, "es:", suma)