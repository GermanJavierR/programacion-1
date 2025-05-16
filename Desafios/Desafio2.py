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

productos_del_usuario_1 = ["Coca cola", "Heldado", "Harina", "Fideos"]
productos_del_usuario_2 = [ "Aceite", "Heldado", "Harina", "Chocolate", "Carne"]
productos_en_comun = []

for producto in productos_del_usuario_1:
    productos_en_comun += [producto]


for i in productos_del_usuario_2:
    if not esta_en_la_lista(i, productos_en_comun):
        productos_en_comun += [i]

print(productos_en_comun)