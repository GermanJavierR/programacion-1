# 1) Mostrar 10 repeticiones de números ascendentes desde el 1 al 10. (for)

# for numero in range(1, 11):
#     print(numero)

# 2) Mostrar 10 repeticiones de números descendentes desde el 10 al 1. (for)

# for numero in range(10, 0, -1):
#     print(numero)

# 3) Mostrar la suma de los números desde el 1 hasta el 10. (for , acumulador)

# cantidad_total = 0

# for numero in range(1, 11):
#     cantidad_total += numero
#     print(f"La cantidad actual es {cantidad_total}")


# 4) Mostrar la suma de los números pares desde el 1 hasta el 10. (for, acumulador, 2)

# suma_total_de_los_pares = 0

# for numero in range(0, 11, 2):
#     suma_total_de_los_pares += numero
#     print(suma_total_de_los_pares)


# 5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.(for, acumulador y contador(opcional), promedio)

# suma_total = 0
# contador = 5

# for numero in range(5):
#     suma_total += int(input("Por favor, ingrese un número: "))
#     print(f"La suma total actual es {suma_total}")

# promedio = suma_total / contador

# print(f"La suma total de los números ingresados es {suma_total} y el promedio es {promedio}")


# 6) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.(while, acumulador y contador, promedio)

# suma_total = 0
# cantidad_de_numeros_ingresados = 0
# continuar = "si"

# while continuar != "no":
#     numero_ingresado = input("Por favor, ingrese un número: ").lower()
#     suma_total += int(numero_ingresado)
#     cantidad_de_numeros_ingresados += 1
#     continuar = input("¿Desea continuar? Ingrese si o no: ")
    

# promedio = suma_total / cantidad_de_numeros_ingresados

# print(f"La suma total de los números ingresados es {suma_total} y el promedio es {promedio}")


# 7) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.(while, acumulador += acumulador *=)

# suma_total_de_los_positivos = 0
# producto_de_los_negativos = 1
# cantidad_de_negativos = 0

# while True:
#     numero_ingresado = input("Por favor, ingrese un número, si desea no ingresar más número ingrese \"FIN\": ").lower()
#     if numero_ingresado == "fin":
#         break
#     elif int(numero_ingresado) > 0:
#         suma_total_de_los_positivos += int(numero_ingresado)
#     else:
#         cantidad_de_negativos = 1
#         producto_de_los_negativos *= int(numero_ingresado)

# if cantidad_de_negativos == 0:
#     producto_de_los_negativos = 0


# print(f"La suma de los números positivos ingresados es {suma_total_de_los_positivos} y el producto de los números negativos es {producto_de_los_negativos}")


# 8) Ingresar 10 números enteros. Determinar el máximo y el mínimo.(for, max , mix )

# numero_max = float('-inf')
# numero_min = float('inf')

# for numero in range(10):
#     numero_actual = int(input("Por favor, ingrese un número: "))
#     if numero_actual > numero_max:
#         numero_max = numero_actual
#     elif numero_actual < numero_min:
#         numero_min = numero_actual

# print(f"El valor más grande es {numero_max} y el más chico es {numero_min}")


# Anexo

# 9) Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.(while, acumulador, contador, promedio)

# cantidad_de_numeros_ingresados = 0
# suma_total = 0
# promedio = 0
# continuar = "SI"

# while continuar != "NO":
#     numero_ingresado = int(input("Por favor, ingrese un número: "))
#     suma_total += numero_ingresado
#     cantidad_de_numeros_ingresados += 1
#     print(f"La suma total actual es {suma_total}")
#     if cantidad_de_numeros_ingresados >= 5:
#         continuar = input("¿Desea continuar ingresando números? Ingres si o no: ").upper()


# promedio = suma_total / cantidad_de_numeros_ingresados

# print(f"La suma total de los número ingresados es {suma_total} y el promedio es {promedio}")


# 10) Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.(for y while, acumulador, contador, promedio)

# while
# cantidad_de_numeros_ingresados = 0
# suma_total = 0
# promedio = 0
# continuar = "SI"

# while continuar != "NO":
#     numero_ingresado = int(input("Por favor, ingrese un número: "))
#     suma_total += numero_ingresado
#     cantidad_de_numeros_ingresados += 1
#     print(f"La suma total actual es {suma_total}")
#     if cantidad_de_numeros_ingresados == 10:
#         break
#     elif cantidad_de_numeros_ingresados >= 5:
#         continuar = input("¿Desea continuar ingresando números? Ingrese si o no: ").upper()

# promedio = suma_total / cantidad_de_numeros_ingresados

# print(f"La suma total de los números ingresados es {suma_total} y el promedio es {promedio}")


#for
# suma_total = 0
# promedio = 0

# for numero in range(1, 11):
#     numero_ingresado = int(input("Por favor, ingrese un número: "))
#     suma_total += numero_ingresado
#     cantidad_de_numeros_ingresados = numero
#     if numero == 10:
#         break
#     elif numero >= 5:
#         continuar = input("¿Desea continuar ingresando números? Ingrese si o no: ").upper()
#         if continuar == "NO":
#             break

# promedio = suma_total / cantidad_de_numeros_ingresados

# print(f"La suma total de los números ingresados es {suma_total} y el promedio es {promedio}")


# Integrador While
"""
Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar: (while)
    A. La suma acumulada de los números negativos.
    B. La suma acumulada de los números positivos.
    C. La cantidad de números negativos ingresados.
    D. El promedio de los números positivos.
    E. El número positivo más grande.
    F. El porcentaje de números negativos ingresados, respecto del total de ingresos.
"""

suma_de_los_positivos = 0
suma_de_los_negativos = 0
cantidad_de_negativos = 0
cantidad_de_positivos = 0
numero_positivo_mas_grande = float("-inf")
continuar = "si"

while continuar != "no":
    numero_ingresado = int(input("Por favor, ingrese un número: "))
    if numero_ingresado > 0:
        suma_de_los_positivos += numero_ingresado
        cantidad_de_positivos += 1
        if numero_ingresado > numero_positivo_mas_grande:
            numero_positivo_mas_grande = numero_ingresado
    elif numero_ingresado < 0:
        suma_de_los_negativos += numero_ingresado
        cantidad_de_negativos += 1
    continuar = input("¿Desea seguir ingresando números? ingrese \"si\" o \"no\": ")

promedio_de_los_positivos = suma_de_los_positivos / cantidad_de_positivos

porcentaje_de_negativos = (cantidad_de_negativos * 100) / (cantidad_de_negativos + cantidad_de_positivos)

print("¿Qué desea ver?")
print("A. La suma acumulada de los números negativos.")
print("B. La suma acumulada de los números positivos.")
print("C. La cantidad de números negativos ingresados.")
print("D. El promedio de los números positivos.")
print("E. El número positivo más grande.")
print("F. El porcentaje de números negativos ingresados, respecto del total de ingresos.")

opcion_a_mostrar = input("Ingrese la letra correspondiente a lo que desee ver: ").upper()

match opcion_a_mostrar:
    case "A":
        print(f"La suma acumulada de los números negativos es {suma_de_los_negativos}.")
    case "B":
        print(f"La suma acumulada de los números positivos es {suma_de_los_positivos}.")
    case "C":
        print(f"La cantidad de los números positivos ingresados es {cantidad_de_positivos}.")
    case "D":
        print(f"El promedio de los números positivos es {promedio_de_los_positivos}.")
    case "E":
        if numero_positivo_mas_grande == float("-inf"):
            print("No se ingresaron números positivos.")
        else:
            print(f"El número positivos más grande ingresado es {numero_positivo_mas_grande}")
    case "F":
        print(f"El porcentaje de números negativos, respecto del total ingresado es {porcentaje_de_negativos}%")
    case _:
        print("El valor ingresado no corresponde a ninguna de las opciones validas.")