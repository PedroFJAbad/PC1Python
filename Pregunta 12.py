# Mapeo de extensiones de archivo a tipos MIME
extensiones_mimes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"}

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo
extension = nombre_archivo.lower().split(".")[-1]

# Obtener el tipo MIME correspondiente
tipo_mime = extensiones_mimes.get(extension, "application/octet-stream")

# Mostrar el tipo MIME correspondiente
print(f"El tipo MIME para '{nombre_archivo}' es: {tipo_mime}")