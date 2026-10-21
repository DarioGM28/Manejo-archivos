import os


class ServicioPeliculas:
    def __init__(self):
        self.nombre_archivo = 'Peliculas.txt'

    def agregar_pelicula (self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf8') as archivo: #acepta cualquier caracter
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
            print('---LISTADO DE PELICULAS---')
            print(archivo.read())

    def eliminar_archivo_peliculas(self):
        os.remove(self.nombre_archivo)
        print(f'Archivo eliminado: {self.nombre_archivo}')

