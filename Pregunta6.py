# Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada
if edad < 4:
    precio = "Gratis"
elif edad <= 18:
    precio = 5
else:
    precio = 10

# Mostrar el precio de la entrada
if precio == "Gratis":
    print("El precio de la entrada es:", precio)
else:
    print("El precio de la entrada es:$", precio)