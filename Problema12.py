# Solicitar al usuario que ingrese el nombre de un archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Dividir el nombre del archivo en dos partes
nombre, tipo = nombre_archivo.split(".")

# Verificar la extensión del archivo y asignar el tipo MIME correspondiente
if tipo == 'gif':
    tipo_mime = 'image/gif'
elif tipo =='jpg':
    tipo_mime = 'image/jpeg'
elif tipo == 'jpeg':
    tipo_mime = 'image/jpeg'
elif tipo == 'png':
    tipo_mime = 'image/png'
elif tipo == 'pdf':
    tipo_mime = 'application/pdf'
elif tipo == 'txt':
    tipo_mime = 'text/plain'
elif tipo == 'zip':
    tipo_mime = 'application/zip'
else: 
    tipo_mime = 'application/octet-stream'

# Imprimir
print(f"El tipo de archivo MIME es {tipo_mime}")