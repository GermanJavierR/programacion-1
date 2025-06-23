"""
7. Eliminar Productos
- De la lista original de productos que me permita eliminar un producto siempre y
cuando el mismo no se encuentre registrado en una venta
"""

import json 
import os
from operaciones_para_productos import descripcion_del_prodcuto_con_codigo_en, producto_con_codigo
from operaciones_para_ventas import obtener_descripcion_de_todos_los_productos_vendidos


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



def eliminar_producto():
    """
    Propósito: Eliminar un producto registrado.
    Return: retorna el archivo con los productos actualizados.
    """

    try:
        with open(archivo2, "r", encoding="UTF-8") as productos:
            datos_productos = json.load(productos)

        with open(archivo3, "r", encoding="UTF-8") as ventas:
            datos_ventas = json.load(ventas)

        codigo_del_producto = input("Ingrese el código del producto que desee eliminar: ").strip()
            
        if not codigo_del_producto:
            print("El código del producto no puede ser vacío.")
            return

        try:
            descripcion_del_producto = descripcion_del_prodcuto_con_codigo_en(codigo_del_producto, datos_productos)

            set_de_productos_vendidos = obtener_descripcion_de_todos_los_productos_vendidos(datos_ventas)

            if descripcion_del_producto in set_de_productos_vendidos:
                print("El producto se encuentra registrado en una venta. No se puede eliminar.")
                return
            else:
                producto = producto_con_codigo(codigo_del_producto, datos_productos)
                datos_productos.remove(producto)
            
            with open(archivo2, "w", encoding="UTF-8") as productos:
                json.dump(datos_productos, productos, indent= 4)

            print("El producto fue eliminado con éxito.")

        except Exception:
            print("El código del producto ingresado no corresponde a ningún producto registrado.")

    except Exception as e:
        print("Ocurrio un error!", e)


# eliminar_producto()