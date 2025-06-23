"""
5. Buscar clientes por provincia
- Permitir ingresar una provincia y mostrar los clientes coincidentes usando comprensión de
listas
"""

import json
import os
from operaciones_para_clientes import provincia_del_cliente

archivo = "clientes.json"


if not os.path.exists(archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        print("El archivo JSON a sido creado.")
    except Exception as e:
        print("Error al crear archivo JSON:", e)



def buscar_por_provincia():
    """
    Propósito: buscar los clientes que correspondan a la provincia ingresada por el usuario.
    Return: retorna todos los clientes que tengan la provincia ingresada.
    """
    try:
        with open(archivo, "r", encoding="UTF-8") as clientes:
            datos_clientes = json.load(clientes)
        
        try:
            provincia_a_buscar = input("Ingrese la provincia por la que desea filtrar: ").strip().lower()
            
            if not provincia_a_buscar:
                print("La provincia a buscar no puede ser vacío.")
                return
            
            for cliente in datos_clientes:
                clientes_encontrado = 0
                if provincia_del_cliente(cliente).lower() == provincia_a_buscar:
                    print(f"El nombre del cliente es {cliente["nombre"]}. Su número de id es {cliente["id"]}. Es de la provincia de {cliente["provincia"]}")
                    clientes_encontrado += 1
            
            if clientes_encontrado == 0:
                print(f"No se han en contrado cliente con la provincia \"{provincia_a_buscar}\"")
            

        except Exception as e:
            print("Ocurrio un erro!", e)

    except Exception as e:
        print("Ocurrio un error!", e)


# buscar_por_provincia()