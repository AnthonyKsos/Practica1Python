# Solicitar al usuario que ingrese el número de payasos
num_payaso = int(input('Ingrese el número de payasos: '))

# Solicitar al usuario que ingrese el número de muñecas
num_muñeca = int(input('Ingrese el número de muñecas: '))

# Calcular el peso total de los payasos
peso_payasos = num_payaso * 112

# Calcular el peso total de las muñecas
peso_muñecas = num_muñeca * 75

# Imprimir el peso total del paquete
print("Peso total del paquete:", peso_payasos + peso_muñecas)