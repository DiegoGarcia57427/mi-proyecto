from utils.file_manager import cargar_clientes

def buscar_por_nombre(nombre):
    """Busca un cliente por nombre"""
    clientes = cargar_clientes()
    for c in clientes:
        if c["nombre_completo"].lower() == nombre.lower():
            return c
    return None
