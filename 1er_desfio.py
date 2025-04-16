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

nota_el_usuario = random.randrange(1, 10)

if nota_el_usuario <= 3:
    print(f"Desaprobado, la nota es {nota_el_usuario}")
elif nota_el_usuario <= 5:
    print(f"Aprobado, la nota es {nota_el_usuario}")
else:
    print(f"Promoción directa, la nota es {nota_el_usuario}")