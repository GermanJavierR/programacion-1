"""
Desafío: Sistema de Recomendación de Productos
Una tienda online quiere mejorar su sistema de recomendaciones analizando el comportamiento de sus clientes. Para ello, dispone del historial de compras de dos usuarios distintos, almacenado en listas de productos.
📌 Objetivo: Escribir un programa en Python que permita analizar estos historiales de compra y responder las siguientes preguntas:
 1️⃣ Productos en común: ¿Qué productos han comprado ambos usuarios?
 2️⃣ Productos exclusivos: ¿Qué productos ha comprado cada usuario que el otro no ha adquirido?
 3️⃣ Catálogo total: ¿Cuál sería el conjunto total de productos comprados entre los dos usuarios?
 4️⃣ Recomendaciones: ¿Cómo podrías utilizar esta información para sugerir productos a cada usuario?
🎯 Requisitos:
 ✔️ El programa debe recibir como entrada dos listas de productos (pueden ser ingresadas manualmente o predefinidas).
 ✔️ Debe procesar y mostrar los resultados de forma clara.
 ✔️ Se valorará el uso de funciones para estructurar el código de manera organizada.
🔹 Extras opcionales:
Permitir que los usuarios ingresen sus listas manualmente.
Ampliar el programa para comparar más de dos usuarios.
"""

# lista1 = input("Por favor, ingrese una lista de productos: ")

from Listas import esta_en_la_lista


productos_del_usuario_1 = ["Coca cola", "Helado", "Harina", "Fideos"]
productos_del_usuario_2 = [ "Aceite", "Helado", "Harina", "Chocolate", "Carne"]

# 1)

def productos_en_comun_entre(compras_usuario1, compras_usuario2):
    """"""
    if isinstance(compras_usuario1, list) and isinstance(compras_usuario2, list):
        productos_en_comun = []
        for producto in compras_usuario1:
            if esta_en_la_lista(producto, compras_usuario2):
                productos_en_comun += [producto]
        return productos_en_comun
    else:
        return "Algunos de los datos ingresados no es una lista."


# print(productos_en_comun_entre(productos_del_usuario_1, productos_del_usuario_2))


# 2)

def productos_exclusivos_de_user1_con_respecto_a_user2(compras_usuario1, compras_usuario2):
    """
    Propósito:
    """
    if isinstance(compras_usuario1, list) and isinstance(compras_usuario2, list):
        productos_en_comun = productos_en_comun_entre(compras_usuario1, compras_usuario2)
        productos_exclusivos_de_cada_uno = []
        for i in compras_usuario1:
            if not esta_en_la_lista(i, productos_en_comun):
                productos_exclusivos_de_cada_uno += [i]
        return productos_exclusivos_de_cada_uno
    else:
        return "Algunos de los datos ingresados no es una lista."
    
print(productos_exclusivos_de_user1_con_respecto_a_user2(productos_del_usuario_1, productos_del_usuario_2))
print(productos_exclusivos_de_user1_con_respecto_a_user2(productos_del_usuario_2, productos_del_usuario_1))


# 3)

def productos_totales_comprados_entre(compras_usuario1, compras_usuario2):
    """
    """
    if isinstance(compras_usuario1, list) and isinstance(compras_usuario2, list):
        return compras_usuario1 + compras_usuario2
    else:
        return "Algunos de los datos ingresados no es una lista."

# Con elementos repetidos.


# 4)

def recomendacion_de_productos_para_user1_con_respecto_al_user2(compras_usuario1, compras_usuario2):
    """
    """
    if isinstance(compras_usuario1, list) and isinstance(compras_usuario2, list):
        productos_para_recomendar = productos_exclusivos_de_user1_con_respecto_a_user2(compras_usuario2, compras_usuario1)
        return productos_para_recomendar
    else:
        return "Algunos de los datos ingresados no es una lista."
    

print(recomendacion_de_productos_para_user1_con_respecto_al_user2(productos_del_usuario_1, productos_del_usuario_2))