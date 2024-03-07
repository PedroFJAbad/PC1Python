# Solicitar al usuario que ingrese el costo de la comida y el porcentaje de propina
costo_comida = float(input("Ingrese el costo de la comida: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar por ejemplo 15 equivale a 15%:"))

# Calcular la cantidad de propina
propina = costo_comida * (porcentaje_propina/100)

# Mostrar la cantidad de propina
print("La cantidad a dejar como propina es: $" , propina) 
print("¿Esta de acuerdo?")
respuesta = input("Si o no: ")

if respuesta.lower() == "si":
    print("¡Gracias, Vuelva pronto!")
elif respuesta.lower() == "no":
    print("¡Gracias, Vuelva pronto!")
else:
    print("Respuesta no válida. Por favor, ingrese 'Si' o 'No'.")