import os 
import json
from operaciones_para_ventas import ingresar_producto_y_cantidad

"""
3. Registrar ventas
- Estructura: lista de ventas (JSON)
- Cada venta: cliente por ID, fecha actual, lista de tuplas (producto, cantidad).
- Validar existencia de cliente, producto y cantidad válida.
"""


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


archivo3 = "ventas.json"

if not os.path.exists(archivo3):
    try:
        with open(archivo3, "w", encoding="utf-8") as ventas:
            json.dump([],ventas, indent=4)
        print("El archivo JSON a sido creado.")
    except Exception as e:
        print("Ocurrio un error al crear el archivo", e)


def registrar_ventas():
    """
    Propósito: registrar las ventas hechas en un archivo json.
    """
    try:
        with open(archivo3, "r", encoding="UTF-8") as ventas:
            datos_ventas = json.load(ventas)

        with open(archivo, "r", encoding="UTF-8") as clientes:
            datos_clientes = json.load(clientes)

        with open(archivo2, "r", encoding="UTF-8") as productos:
            datos_productos = json.load(productos)

        try:
            id_cliente = int(input("Ingrese el id del cliente que realizo la compra: "))
            encontrado = next((a for a in datos_clientes if a["id"] == id_cliente), None)
            if not encontrado:
                print("El id ingresado no corresponde a ningún cliente registrado.")
                return
            
            fecha = input("Ingrese la fecha de cuando se realizo la compra en formato DD-MM-AAAA: ").strip()
            if not fecha:
                print("La fecha no puede ser vacía.")
                return
            
            lista_de_tuplas = ingresar_producto_y_cantidad(datos_productos)
            if not lista_de_tuplas:
                print("La lista de tuplas no puede ser vacía.")
                return

            nueva_venta = {"id del cliente" : id_cliente, "fecha" : fecha, "lista de compras" : lista_de_tuplas}

            datos_ventas.append(nueva_venta)
        except:
            print("El valor ingresado para la id del cliente no es un entero.")
        
        with open(archivo3, "w", encoding="UTF-8") as ventas:
            json.dump(datos_ventas, ventas, indent= 4)
    except Exception as e:
        print("Ocurrio un error!", e)


# registrar_ventas()