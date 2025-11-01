# 📋 Sistema de Gestión de Clientes (Python)

## 📘 Descripción del Proyecto
Este proyecto es una aplicación de consola desarrollada en **Python** que permite gestionar clientes de manera sencilla.  
Cada cliente se almacena en un archivo `.txt` dentro de la carpeta `data/clientes/`, incluyendo:

- 🆔 ID único y consecutivo  
- 👤 Nombre completo  
- 📧 Correo electrónico  
- 🕓 Fecha de registro (automática)  
- 💼 Servicio contratado  

---

## ⚙️ Funcionalidades Principales

✅ Crear cliente nuevo  
✅ Buscar cliente por nombre  
✅ Listar todos los clientes  
✅ Modificar cliente existente  
✅ Eliminar cliente  
✅ Guardar datos en archivos `.txt`

---

## 🗂️ Estructura del Proyecto

.
├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-313.pyc
│   └── main.cpython-313.pyc
├── clientes_txt
│   └── Diego_G.txt
├── data
│   └── clientes
├── main.py
├── services
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── buscar_cliente.cpython-313.pyc
│   │   ├── crear_cliente.cpython-313.pyc
│   │   ├── eliminar_cliente.cpython-313.pyc
│   │   ├── listado_clientes.cpython-313.pyc
│   │   └── modificar_clientes.cpython-313.pyc
│   ├── buscar_cliente.py
│   ├── crear_cliente.py
│   ├── eliminar_cliente.py
│   ├── listado_clientes.py
│   └── modificar_clientes.py
└── utils
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-313.pyc
    │   └── file_manager.cpython-313.pyc
    ├── data
    │   └── Clientes 
    └── file_manager.py


## 🗂️ Implementación del programa 

--- Gestión de Clientes ---
1. Crear cliente nuevo
2. Buscar cliente por nombre
3. Listar todos los clientes
4. Modificar cliente
5. Eliminar cliente
6. Salir


## ⚙️ Detalles técnicos

✅ Lenguaje: Python 3.10+
✅ interfaz:Consola/Terminal 
✅ Persistencia:Archivos .txt en carpeta /data/clientes
✅ Arquitectura modular: Cada acción se maneja en un archivo separado dentro de /services

## 📋 Autor

👤 Diego Arturo García Flores
📧 TecMilenio-Proyecto de programación 2025
🚀 Prueba de deploy automático Sat Nov  1 02:02:46 CST 2025
# prueba workflow
# otra prueba workflow
