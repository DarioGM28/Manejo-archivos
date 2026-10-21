#abrir un archivo en modo exclusivo

nombre_archivo = 'Mi_archivo.txt'

try:
    with open (nombre_archivo, 'x') as archivo:
        archivo.write("Esccritura en modo exclusivo\n")
        archivo.write('Espero sea util\n')
    print(f"archivo creado {nombre_archivo}")
except FileExistsError as e:
    print(f"El archivo {nombre_archivo} ya existe\nerror de tipo {e}")