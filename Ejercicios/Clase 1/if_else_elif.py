# 1)
altura_del_jugador = int(input("Por favor, ingrese su altura en cm para determinar su posición: "))

if altura_del_jugador < 160:
    print("Tu posición es de Base")
elif altura_del_jugador < 180:
    print("Tu posición es de Escolta")
elif altura_del_jugador < 200:
    print("Tu posición es de Alero")
else:
    print("Tu posición es de Ala-Pívot o Pívot")


# 2)
import random

nombre_del_usuario = input("Ingrese su nombre: ")
nota_el_usuario = random.randrange(1, 10)

if nota_el_usuario <= 3:
    print(f"El usuario {nombre_del_usuario} está Desaprobado")
elif nota_el_usuario <= 5:
    print(f"El usuario {nombre_del_usuario} está Aprobado")
else:
    print(f"El usuario {nombre_del_usuario} tiene Promoción directa")