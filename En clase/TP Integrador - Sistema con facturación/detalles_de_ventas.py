"""
6. Mostrar detalle de ventas
- Imprimir detalle de cada factura con cliente, fecha, productos vendidos, subtotales y total
final.
- Calcular totales cruzando datos con el catálogo de productos.
"""

import json
import os
from operaciones_para_productos import precio_del_producto

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



def detalle_de_ventas():
    """
    Propósito: Mostrar los detalles de cada venta realizada.
    Return: retorna el cliente, la fecha de la venta, los productos vendidos, subtotales y total final
    """
    try :
        with open(archivo3, "r", encoding="UTF-8") as ventas:
            datos_ventas = json.load(ventas)

        with open(archivo2, "r", encoding="UTF-8") as productos:
            datos_productos = json.load(productos)

        for venta in datos_ventas:
            print(f"Compra realizada por el clienet con id \"{venta["id del cliente"]}\": ")
            total_a_facturar = 0
            for i in venta["lista de compras"]:
                precio_del_producto_actual = precio_del_producto(i[0], datos_productos) #
                subtotal = precio_del_producto_actual * i[1]
                total_a_facturar += subtotal
                print(f"El subtotal por {i[1]} {i[0]} es: ${subtotal}")
            print(f"El total a facturar por la venta del dia {venta["fecha"]} es de: ${total_a_facturar}")

    except Exception as e:
        print("Ocurrio un error!", e)


# detalle_de_ventas()