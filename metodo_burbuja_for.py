"""
BUBBLE SORT DESCENDENTE

Descripción:
Compara elementos adyacentes e intercambia si están en el orden incorrecto.
Ordena de mayor a menor.

Ventajas:
- Simple de implementar.
Desventajas:
- Muy ineficiente para listas grandes (O(n²)).
"""

lista = [64, 34, 25, 12, 22, 11, 90]

n = len(lista)
# i = 0
# while i < n - 1:
#     intercambiado = False
#     j = 0
#     while j < n - 1 - i:
#         if lista[j] < lista[j + 1]:  # CAMBIO: buscamos el mayor primero
#             # Intercambio
#             temp = lista[j]
#             lista[j] = lista[j + 1]
#             lista[j + 1] = temp
#             intercambiado = True
#         j = j + 1
#     if not intercambiado:  # Si no hubo ningún intercambio, la lista ya está ordenada
#         break
#     i = i + 1


for i in range(n - 1):
    intercambiado = False
    for j in range(n - 1 - i):
        if lista[j] < lista[j + 1]: # CAMBIO: buscamos el mayor primero
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp
            intercambiado = True
    if not intercambiado:  # Si no hubo ningún intercambio, la lista ya está ordenada
        break

print("Lista ordenada de mayor a menor con Bubble Sort:", lista)

"""
BUBBLE SORT MEJORADO

Descripción:
Versión optimizada del algoritmo burbuja. Detecta si en una pasada no se realizaron intercambios,
lo que indica que la lista ya está ordenada y se puede terminar antes.

Ventajas:
- Simple de implementar y entender.
- Mejor que el burbuja clásico si la lista está casi ordenada.

Desventajas:
- Ineficiente en listas grandes (complejidad O(n^2)).
"""

# Lista a ordenar
lista = [64, 34, 25, 12, 22, 11, 90]

n = len(lista)
# i = 0
# while i < n - 1:
#     intercambiado = False  # Bandera para saber si hubo intercambio
#     j = 0
#     # Recorremos la lista desde el inicio hasta el penúltimo elemento no ordenado
#     # (n - 1 - i) porque cada pasada coloca el mayor elemento al final
#     # y no es necesario volver a revisarlo
#     while j < n - 1 - i:
#         if lista[j] > lista[j + 1]:  # Si los elementos están fuera de orden
#             temp = lista[j]
#             lista[j] = lista[j + 1]  # Intercambiamos
#             lista[j + 1] = temp
#             intercambiado = True  # Marcamos que hubo intercambio
#         j = j + 1
#     if not intercambiado:  # Si no hubo ningún intercambio, la lista ya está ordenada
#         break
#     i = i + 1



for i in range(n - 1):
    intercambiado = False
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]: # CAMBIO: buscamos el mayor primero
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp
            intercambiado = True
    if not intercambiado:  # Si no hubo ningún intercambio, la lista ya está ordenada
        break

# Mostramos la lista ordenada
print("Lista ordenada con Bubble Sort Mejorado:", lista)