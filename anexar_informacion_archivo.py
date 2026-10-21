
nombre_archivo = "Mi_archivo.txt"

with open (nombre_archivo, 'a') as archivo:
    #anexar informacion al archivo
    archivo.write("Anexando informacion\n")
    archivo.write("Saliendo de anexar informacion....\n")

print(f"se ha anexado informacion al archivo: {nombre_archivo}")