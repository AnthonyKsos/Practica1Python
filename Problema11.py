lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
print(f"Lista original: {lista_original}")

# Convertir a conjunto para eliminar duplicados
conjunto = set(lista_original)

# Pasar a otra lista sin duplicados
lista_procesada = list(conjunto)

# Imprimir
print(f"Lista procesada: {lista_procesada}")