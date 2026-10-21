
nombre_archivo = "Mi_archivo.txt"

#Leer usando metodo readlineas

with open (nombre_archivo, 'r') as archivo:
    #leer todas las lineas
    #print(archivo.readlines())
    #otra forma de imprimirlo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea)
        print()
        #print(linea.strip()), si queremos quitar los saltos de linea

#leer todo el contenido del archivo
print('Leyendo el contenido con el metodo read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())
