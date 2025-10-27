from utils.file_manager import cargar_clientes, guardar_cliente

def modificar_cliente(nombre):
    """Modifica un cliente existente"""
    clientes = cargar_clientes()
    cliente = None
    for c in clientes:
        if c["nombre_completo"].lower() == nombre.lower():
            cliente = c
            break
    if not cliente:
        print("Cliente no encontrado.")
        return

    nuevo_nombre = input(f"Nombre [{cliente['nombre_completo']}]: ") or cliente['nombre_completo']
    nuevo_correo = input(f"Correo [{cliente['correo']}]: ") or cliente['correo']
    nueva_descripcion = input(f"Descripción [{cliente['descripcion_servicio']}]: ") or cliente['descripcion_servicio']

    cliente.update({
        "nombre_completo": nuevo_nombre,
        "correo": nuevo_correo,
        "descripcion_servicio": nueva_descripcion
    })

    guardar_cliente(cliente)
    print("Cliente modificado correctamente.")
