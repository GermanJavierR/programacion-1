import json
import os

archivo = "clientes.json"


if not os.path.exists(archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        print("El archivo JSON a sido creado.")
    except Exception as e:
        print("Error al crear archivo JSON:", e)


archivo2 = "productos.json"


if not os.path.exists(archivo2):
    try:
        with open(archivo2, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        print("El archivo JSON a sido creado.")
    except Exception as e:
        print("Error al crear archivo JSON:", e)



"""
4. Mostrar clientes y productos
- Imprimir los datos de los archivos en formato legible.
"""

def mostrar_clientes_y_productos():
    """
    Propósito: Mostrar los clientes y los productos.
    Return: los datos de los archivos clientes y productos.
    """
    try:
        with open(archivo, "r", encoding="UTF-8") as clientes:
            datos_clientes = json.load(clientes)
    
        with open(archivo2, "r", encoding="UTF-8") as productos:
            datos_productos = json.load(productos)

        print("Los datos de los clientes son: ")
        try:
            for cliente in datos_clientes:
                print(f"El nombre del cliente es {cliente["nombre"]}. Su número de id es {cliente["id"]}. Es de la provincia de {cliente["provincia"]}")
        except Exception as e:
            print("Ocurrio un error,", e)

        print("Los datos de los productos son: ")
        try:
            for producto in datos_productos:
                print(f"La descripción del producto es: \"{producto["descripción"]}\". El código es \"{producto["código"]}\". El precio es ${producto["precio"]}")
        except Exception as e:
            print("Ocurrio un error,", e)
    except Exception as e:
        print("Ocurrio un error!", e)


# mostrar_clientes_y_productos()