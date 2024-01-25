# Solicitar al usuario la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Encontrar el precio correspondiente a la edad del cliente
if edad < 4:
    precio = "Gratis"
elif edad < 18:
    precio = 5
else:
    precio = 10

# Imprimir el resultado
print(f"El precio a pagar según su edad ingresada es: {precio}")