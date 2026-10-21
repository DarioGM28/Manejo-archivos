from proyecto_catalogo_peliculas.pelicula import Pelicula
from proyecto_catalogo_peliculas.servicio_pelicula import ServicioPeliculas


class AppCatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('***CATALOGO DE PELICULAS***')
        while True:
            try:
                print('''\tOPCIONES
                   1. Agregar Peliculas
                   2. Listar Peliculas
                   3. Eliminar Catalogo
                   4. Salir''')
                opcion = int(input('Ingrese una opcion (1-4): '))
                if opcion == 1:
                    nombre_pelicula = input('Ingrese el nombre del pelicula: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('SALIENDO DEL PROGRAMA....')
                    break
                else:
                    print('Opcion invalida')

            except ValueError:
                print('Opcion incorrecta')
            except Exception as e:
                print(f"Ocurrio el error: {e}")
if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()
