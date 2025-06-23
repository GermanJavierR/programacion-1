import os
import json

archivo = "clientes.json"


if not os.path.exists(archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        print("El archivo JSON a sido creado.")
    except Exception as e:
        print("Error al crear archivo JSON:", e)



"""
1. Cargar clientes
- Estructura: lista de diccionarios (JSON)
- Cada cliente debe tener ID único, nombre y provincia.
- Validar que el ID no se repita y que los campos no estén vacíos.
"""
def cargar_cliente():
    """
    Propósito: Cargar cliente en el archivo json
    """
    try:
        with open(archivo, "r", encoding="utf-8") as clientes:
            datos = json.load(clientes)
        try:
            cliente_id = int(input("Ingrese ID del cliente: ")) 
            encontrado = next((a for a in datos if a["id"] == cliente_id), None)
            if encontrado:
                print("Error: ID ya existente.")
                return
            nombre = input("Ingrese nombre: ").strip()
            provincia = input("Ingrese provincia: ").strip()
            if not nombre or not provincia:
                print("Error: nombre y provincia no pueden estar vacíos.")
                return
            nuevo_cliente = {"id": cliente_id, "nombre": nombre, "provincia": provincia}
            datos.append(nuevo_cliente)
        except ValueError:
            print("Error: ID debe ser un número entero.")
        with open(archivo, "w", encoding="utf-8") as clientes:
            json.dump(datos, clientes, indent=4)
    except Exception as e:
        print("Orcurrio un error!", e)


# cargar_cliente()
