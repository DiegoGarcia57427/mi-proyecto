import os
from utils.file_manager import DATA_DIR

def eliminar_cliente(nombre):
    """Elimina un cliente por nombre"""
    eliminado = False
    for archivo in os.listdir(DATA_DIR):
        if archivo.endswith(".txt"):
            ruta = os.path.join(DATA_DIR, archivo)
            with open(ruta, "r") as f:
                import json
                cliente = json.load(f)
            if cliente["nombre_completo"].lower() == nombre.lower():
                os.remove(ruta)
                eliminado = True
                print(f"Cliente {nombre} eliminado correctamente.")
                break
    if not eliminado:
        print("Cliente no encontrado.")
