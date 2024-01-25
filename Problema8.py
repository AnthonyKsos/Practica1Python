# Solicitar la hora al usuario
hora = input("Introduce la hora en formato H:M (24 horas): ")

# Dividir la entrada ingresada por el carácter ':'
hora, minutos = hora.split(":")

# Convertir a enteros
hora = int(hora)
minutos = int(minutos)

# Convertir la hora a un formato de tipo float
hora_actual = hora + minutos/60

# Imprimir según la hora
if 7 <= hora_actual <= 8:
    print("Hora del desayuno")
elif 12 <= hora_actual <= 13:
    print("Hora del almuerzo")
elif 18 <= hora_actual <= 19:
    print("Hora de la cena")