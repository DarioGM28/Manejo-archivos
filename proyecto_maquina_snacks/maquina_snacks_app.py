from proyecto_maquina_snacks.servicio_snacks import ServicioSnacks
from proyecto_maquina_snacks.snack import Snack


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print('***Maquina de snacks***')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrio un error: {e}")

    def mostrar_menu(self):
        print('''Menu
        1. Comprar Snacks
        2. Mostrar Snacks
        3. Agregar Nuevo Snacks al Invetario
        4. Inventario de Snacks
        5. Salir''')
        return int(input('Ingrese una opcion: '))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snacks()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto....')
            return True
        else:
            print(f'Opcion invalida: {opcion}')
        return False

    def comprar_snack(self):
        id_snack = int(input('Ingrese un numero (id) de snack: '))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f"Snack Encontrado: {snack}")
        else:
            print(f'Snack {id_snack} no encontrado')

    def mostrar_ticket(self):
        if not self.productos:
            print('No hay productos encontrados')
            return
        total = sum(snack.precio for snack in self.productos)
        print('----TICKET DE VENTA----')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - COP{producto.precio:.2f}')
        print(f'Total -> COP{total}')

    def agregar_snacks(self):
        nombre = input('Nombre del sanck: ')
        precio = float(input('Precio del sanck: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snacks(nuevo_snack)
        print('Snack agregado correctamente')

if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()

