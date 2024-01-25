# Solicitar al usuario el número de shows musicales
num_show_musicales = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))

# Validar si fueron más de 3 con un valor booleano
if num_show_musicales > 3:
    boolean = True
else:
    boolean = False

# Imprimir el resultado
print(f"¿El usuario a visto más de 3 shows?: {boolean}")