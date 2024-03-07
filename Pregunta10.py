# Definir la lista de muestra
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Eliminar elementos en las posiciones 0, 4 y 5
posiciones = [0, 4, 5]
for i in sorted(posiciones, reverse=True):
    lista.pop(i)

# Mostrar la lista resultante
print(lista)