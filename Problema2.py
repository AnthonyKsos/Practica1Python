# Solicitar al usuario que ingrese el monto de su consumo
consumo = int(input('Ingrese su consumo en el restaurante: '))

# Solicitar al usuario que ingrese el porcentaje de propina que desea dejar
porcentaje_propina = int(input('Ingrese el porcentaje de propina: '))

# Calcular el monto de la propina
propina = consumo * (porcentaje_propina / 100)

# Imprimir el monto de la propina
print(f"La propina a dejar es {propina}")