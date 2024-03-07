def peso_paquete(num_payasos, num_muñecas):
    peso_payaso = 112  # Peso de cada payaso en gramos
    peso_muñeca = 75   # Peso de cada muñeca en gramos
    peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
    return peso_total

# Leer el número de payasos y muñecas vendidos en el último pedido
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calcular el peso total del paquete
peso_total_paquete = peso_paquete(num_payasos, num_muñecas)

# Mostrar el peso total del paquete
print("El peso total del paquete que será enviado es:", peso_total_paquete, "gramos")