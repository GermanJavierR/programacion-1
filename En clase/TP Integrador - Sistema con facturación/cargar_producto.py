import os
import json 

"""
2. Cargar productos
- Estructura: lista de diccionarios (JSON)
- Cada producto debe tener código único, descripción y precio.
- Validar código único y precio mayor a 0.
"""

archivo2 = "productos.json"


if not os.path.exists(archivo2):
    try:
        with open(archivo2, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        print("El archivo JSON a sido creado.")
    except Exception as e:
        print("Error al crear archivo JSON:", e)


def cargar_producto():
    """
    Propósito: cargar los productos ingresados por el usuario a un archivo .json
    """
    try:
        with open(archivo2, "r", encoding="utf-8") as productos:
            datos = json.load(productos)

        try:
            descripcion = input("Ingrese la descripción del producto: ").strip()
            codigo = input("Ingrese el código del producto: ").strip()
            if not descripcion or not codigo:
                print("La descripción y el código no pueden estar vacios.")
                return
            encontrar = next((a for a in datos if a["código"] == codigo), None)
            if encontrar:
                print("El código ingresado ya pertenece a un producto.")
                return 
            precio = int(input("Ingrese el precio del producto: "))
            nuevo_producto = {"descripción": descripcion, "código": codigo, "precio": precio}
            datos.append(nuevo_producto)
        except Exception as e:
            print("El valor ingresado para el precio del producto no es un entero positivo.")
        with open(archivo2, "w", encoding="utf-8") as prodcutos:
            json.dump(datos, prodcutos, indent = 4)
        print("El producto se ha cargado correctamente!")
    except Exception as e:
        print("Ocurrio un error!", e)   



# cargar_producto()
