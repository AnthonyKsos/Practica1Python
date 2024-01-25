# Solicitar los valores de 2 números
x = int(input("Ingrese el valor del primer número: "))
y = int(input("Ingrese el valor del segundo número: "))

# Mostrar el menú
print("\nMenú")
print("1. Mostrar una suma de los dos números")
print("2. Mostrar una resta de los dos números")
print("3. Mostrar una multiplicación de los dos números")
opcion = int(input("Ingrese una opción: "))

# Realizar una operación con los números ingresados según la opción ingresada
if opcion == 1:
    suma = x + y
    print(f"La suma es {suma}")
elif opcion == 2:
    resta =  x - y
    print(f"La resta es {resta}")
elif opcion == 3:
    multiplicación = x * y
    print(f"La multiplicación es {multiplicación}")
else:
    print("La opción no es correcta")