from services.crear_cliente import ejecutar as crear_cliente
from services.buscar_cliente import buscar_por_nombre as buscar_cliente
from services.modificar_clientes import modificar_cliente
from services.listado_clientes import listar_todos
from services.eliminar_cliente import eliminar_cliente

def menu():
    print("\n--- Gestión de Clientes ---")
    print("1. Crear cliente nuevo")
    print("2. Buscar cliente por nombre")
    print("3. Listar todos los clientes")
    print("4. Modificar cliente")
    print("5. Eliminar cliente")
    print("6. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("\nSelecciona una opción: ").strip()
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            nombre = input("Ingresa el nombre del cliente: ")
            cliente = buscar_cliente(nombre)
            if cliente:
                print("\nCliente encontrado:")
                print(cliente)
            else:
                print("No se encontró ningún cliente con ese nombre.")
        elif opcion == "3":
            clientes = listar_todos()
            if clientes:
                print("\nLista de clientes:")
                for c in clientes:
                    print(f"{c['id']}: {c['nombre_completo']} - {c['correo']} - {c['descripcion_servicio']}")
            else:
                print("No hay clientes registrados.")
        elif opcion == "4":
            nombre = input("Ingresa el nombre del cliente a modificar: ")
            modificar_cliente(nombre)
        elif opcion == "5":
            nombre = input("Ingresa el nombre del cliente a eliminar: ")
            eliminar_cliente(nombre)
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
