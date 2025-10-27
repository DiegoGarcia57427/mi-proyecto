import os
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "clientes")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def guardar_cliente(cliente):
    """Guarda un cliente en un archivo .txt"""
    try:
        file_path = os.path.join(DATA_DIR, f"{cliente['id']}.txt")
        with open(file_path, "w") as f:
            json.dump(cliente, f, indent=4)
    except Exception as e:
        print(f"Error al guardar el cliente: {e}")

def cargar_clientes():
    """Carga todos los clientes desde los archivos .txt"""
    clientes = []
    try:
        for archivo in os.listdir(DATA_DIR):
            if archivo.endswith(".txt"):
                with open(os.path.join(DATA_DIR, archivo), "r") as f:
                    clientes.append(json.load(f))
    except Exception as e:
        print(f"Error al cargar clientes: {e}")
    return clientes
