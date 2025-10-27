from datetime import datetime
from utils.file_manager import guardar_cliente, cargar_clientes

def ejecutar():
    """Crea un cliente con ID único, fecha de registro y descripción del servicio"""
    clientes = cargar_clientes()
    id_cliente = max([c["id"] for c in clientes], default=0) + 1
    nombre = input("Nombre completo: ")
    correo = input("Correo: ")
    descripcion = input("Descripción del servicio: ")

    cliente = {
        "id": id_cliente,
        "nombre_completo": nombre,
        "correo": correo,
        "descripcion_servicio": descripcion,
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    guardar_cliente(cliente)
    print(f"\nCliente {nombre} registrado con ID {id_cliente}")
