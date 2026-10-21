import os.path


from proyecto_maquina_snacks.snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = "snacks.txt"

    def __init__(self):
        self.snacks: list = []
        #Revisar si ya existe el archivo de snacks
        #Si ya existe obtenemos los snacks del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        #Si NO existe agregamos snacks
        else:
            self.cargar_snacks_inciales()

    def cargar_snacks_inciales(self):
        snacks_inciales = [
            Snack('Papas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 120),
        ]
        self.snacks.extend(snacks_inciales)
        self.guardar_snacks_archivo(snacks_inciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f"{snack.escribir_snack()}\n")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for line in archivo:
                    id_snack, nombre, precio = line.strip().split(',') #Desempaquetamos y almacenamos en las variables
                    snack = Snack(nombre, float(precio)) #No ponemos el id_snack por que ya se pone en el contructor de la clase Snack
                    snacks.append(snack)
        except Exception as e:
            print(f"Error al leer snacks: {e}")
        return snacks

    def agregar_snacks(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('---Snacks en el inventario---')
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks

