# Solicitar al usuario que ingrese la hora en formato HH:MM
hora_str = input("Ingrese la hora en formato HH:MM: ")

# Obtener la hora como un número de punto flotante
hora_float = float(hora_str.replace(':', '.'))

# Determinar si es hora de desayunar, almorzar o cenar
if 7.0 <= hora_float <= 8.0:
    print("Es hora de desayunar.")
elif 12.0 <= hora_float <= 13.0:
    print("Es hora de almorzar.")
elif 18.0 <= hora_float <= 19.0:
    print("Es hora de cenar.")
