#vamos a crear un archivo

nombre_archivo = 'Mi_archivo.txt'

#abrir el archivo en modo escritura 'w'
with open(nombre_archivo, 'w') as archivo:
    archivo = open(nombre_archivo, "w")
    archivo.write("Hola como estas ?\n")
    archivo.write("estoy agregando informacion al archivo\n")
    #archivo.close(), si no estuviera el metodo with habria que ponerlo

print(f"se creo el archivo: {nombre_archivo}")