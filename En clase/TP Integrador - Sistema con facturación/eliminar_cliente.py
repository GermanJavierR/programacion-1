"""
8. Eliminar Cliente
- De la lista original de diccionario de Clientes que me permita eliminar un cliente
siempre y cuando el mismo no se encuentre registrado en una venta
"""

import json 
import os
from operaciones_para_ventas import obtener_clientes_que_compraron_productos
from operaciones_para_clientes import cliente_con_id_en



archivo = "clientes.json"


if not os.path.exists(archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
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


def eliminar_cliente():
    """
    Propósito: Eliminar un cliente de la lista de clientes registrados.
    Return: retorna un archivo con todos los cliente sin el que se quiere eliminar.
    """

    try:
        with open(archivo, "r", encoding="UTF-8") as clientes:
            datos_clientes = json.load(clientes)

        with open(archivo3, "r", encoding="UTF-8") as ventas:
            datos_ventas = json.load(ventas)

        try:
            id_del_cliente = int(input("Ingrese el ID del cliente que desee eliminar: ").strip())
        except:
            print("El valor ingresado no es un número entero.")
            return

        try:

            set_de_ids_clientes_que_compraron = obtener_clientes_que_compraron_productos(datos_ventas)

            if id_del_cliente in set_de_ids_clientes_que_compraron:
                print("El cliente se encuentra registrado en una venta. No se puede eliminar.")
                return
            else:
                cliente = cliente_con_id_en(id_del_cliente, datos_clientes)
                datos_clientes.remove(cliente)
            
            with open(archivo, "w", encoding="UTF-8") as clientes:
                json.dump(datos_clientes, clientes, indent= 4)

            print("El cliente fue eliminado con éxito.")

        except Exception:
            print("El ID ingresado no corresponde a ningún cliente registrado.")

    except Exception as e:
        print("Ocurrio un error!", e)



# eliminar_cliente()