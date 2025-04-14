# 1) Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

# numero_actual = 1

# while numero_actual != 11:
#     print(numero_actual)
#     numero_actual += 1

# 2) Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

# numero_actual_2 = 10

# while numero_actual_2 != 0:
#     print(numero_actual_2)
#     numero_actual_2 -= 1

# 3) Mostrar la suma de los números desde el 1 hasta el 10.

# numero_actual_3 = 1
# cantidad_actual = 0

# while numero_actual_3 != 11:
#     cantidad_actual += numero_actual_3
#     print(cantidad_actual)
#     numero_actual_3 += 1

# 4) Mostrar la suma de los números pares desde el 1 hasta el 10.

# numero_actual = 2
# cantidad_actual = 0

# while numero_actual <= 10:
#     cantidad_actual += numero_actual
#     numero_actual += 2

# print(cantidad_actual)

# 5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

# numeros_ingresados = 5
# cantidad_actual = 0

# while numeros_ingresados != 0:
#     cantidad_actual += int(input("Ingrese un número: "))
#     numeros_ingresados -= 1

# promedio_de_los_numeros = cantidad_actual / 5

# print(f"La suma de los números ingresados es de {cantidad_actual}")
# print(f"El promedio de los números ingresados es de {promedio_de_los_numeros}")

# 6) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

# numero = input("Ingrese un número, si no desea ingresar mas número ingrese \"Listo\": ").lower()
# cantidad_de_numeros_ingresados = 0
# suma_actual = 0

# while numero != "listo":
#     suma_actual += int(numero)
#     cantidad_de_numeros_ingresados += 1
#     numero = input("Ingrese un número, si no desea ingresar mas número ingrese \"Listo\": ").lower()

# print(f"La suma de los numero ingresados es: {suma_actual}.")
# if cantidad_de_numeros_ingresados != 0:
#     print(f"El promedio de los números ingresados es de: {suma_actual / cantidad_de_numeros_ingresados}")
# else:
#     print("El promedio es 0")

# 7) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

# numero = input("Ingrese un número, si no desea ingresar mas número ingrese \"Listo\": ").lower()
# suma_de_positivos = 0
# producto_de_negativos = 1
# cantidad_de_negativos = 0

# while numero != "listo":
#     if int(numero) > 0:
#         suma_de_positivos += int(numero)
#     else:
#         producto_de_negativos *= int(numero)
#         cantidad_de_negativos += 1
#     numero = input("Ingrese un número, si no desea ingresar mas número ingrese \"Listo\": ").lower()
    

# print(f"La suma de los números positivos es: {suma_de_positivos}")

# if cantidad_de_negativos > 0:
#     print(f"El producto de los números negativos es: {producto_de_negativos}")
# else:
#     print("El producto de los números negativos es 0.")


# 8) Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# cantidad_de_ingresos = 10

# while cantidad_de_ingresos != 0:
#     numero_ingresado = int(input("Ingrese un número entero: "))
#     numero_max_actual = numero_ingresado
#     numero_min_actual = numero_ingresado
#     if numero_ingresado > numero_max_actual:
#         numero_max_actual = numero_ingresado
#     elif numero_ingresado < numero_min_actual:
#         numero_min_actual = numero_ingresado
#     cantidad_de_ingresos -= 1

# print(f"El número más grande ingresado es {numero_max_actual}")
# print(f"El numero más chico ingresado es {numero_min_actual}")

# 9) Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

# cantidad_minima_de_numeros = 5
# cantidad_actual = 0
# cantidad_de_numeros = 5

# while cantidad_minima_de_numeros != 0:
#     numero_actual = int(input("Ingrese un número: "))
#     cantidad_actual += numero_actual
#     cantidad_minima_de_numeros -= 1

# numero_o_terminar = input("Ingrese un número o si desea no ingresar más, escriba \"Terminar\": ").lower()

# while numero_o_terminar != "terminar":
#     cantidad_actual += int(numero_o_terminar)
#     cantidad_de_numeros += 1
#     numero_o_terminar = input("Ingrese un número o si desea no ingresar más, escriba \"Terminar\": ").lower()


# promedio_de_los_numeros_ingresados = cantidad_actual / cantidad_de_numeros

# print(f"La suma total de los números es {cantidad_actual}")
# print(f"El promedio de los números ingresados es {promedio_de_los_numeros_ingresados}")

# 10) Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

# cantidad_minima_de_numeros = 1
# canitdad_maxima_de_numeros = 6
# cantidad_actual = 0
# cantidad_de_numeros = 5

# while cantidad_minima_de_numeros <= 5 :
#     numero_actual = int(input("Ingrese un número: "))
#     cantidad_actual += numero_actual
#     cantidad_minima_de_numeros += 1


# while canitdad_maxima_de_numeros <= 10 or numero_o_terminar == "terminar":
#     numero_o_terminar = input("Ingrese un número o si desea no ingresar más, escriba \"Terminar\": ").lower()
#     cantidad_actual += int(numero_o_terminar)
#     cantidad_de_numeros += 1
#     canitdad_maxima_de_numeros += 1


# promedio_de_los_numeros_ingresados = cantidad_actual / cantidad_de_numeros

# print(f"La suma total de los números es {cantidad_actual}")
# print(f"El promedio de los números ingresados es {promedio_de_los_numeros_ingresados}")


# Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

# numero_o_terminar = input("Ingrese un número o si desea no ingresar más, escriba \"Terminar\": ").lower()
# suma_de_positivos_actual = 0
# suma_de_negativos_actual = 0
# cantidad_de_numeros_negativos = 0
# cantidad_de_numeros_positivos = 0
# cantidad_de_ceros_ingresados = 0
# numero_positivo_mas_grande = 0

# while numero_o_terminar != "terminar":
#     numero_o_terminar = int(numero_o_terminar)
#     if numero_o_terminar > 0:
#         if numero_o_terminar > numero_positivo_mas_grande:
#             numero_positivo_mas_grande = numero_o_terminar
#         cantidad_de_numeros_positivos += 1
#         suma_de_positivos_actual += numero_o_terminar
#     elif numero_o_terminar < 0:
#         cantidad_de_numeros_negativos += 1
#         suma_de_negativos_actual += numero_o_terminar
#     else:
#         cantidad_de_ceros_ingresados += 1
#     numero_o_terminar = input("Ingrese un número o si desea no ingresar más, escriba \"Terminar\": ").lower()

# if cantidad_de_numeros_positivos != 0:
#     promedio_de_los_positivos = suma_de_positivos_actual / cantidad_de_numeros_positivos
# else:
#     promedio_de_los_positivos = 0

# if cantidad_de_ceros_ingresados != 0 or cantidad_de_numeros_negativos != 0 or cantidad_de_numeros_positivos != 0:
#     porcentaje_de_numeros_negativos = (cantidad_de_numeros_negativos * 100) / (cantidad_de_numeros_negativos + cantidad_de_numeros_positivos + cantidad_de_ceros_ingresados) 
# else:
#     porcentaje_de_numeros_negativos = 0

# print(f"La suma de todos los numeros negativos es: {suma_de_negativos_actual}")
# print(f"La suma de todos los numeros positivos es: {suma_de_positivos_actual}")
# print(f"La cantidad de numeros negativos ingresados es: {cantidad_de_numeros_negativos}")
# print(f"El promedio de los numeros positivos es: {promedio_de_los_positivos}")

# if numero_positivo_mas_grande == 0:
#     print("No hay números positivos.")
# else:
#     print(f"El número positivo más grande es: {numero_positivo_mas_grande}")

# print(f"El porcentaje de números negativos ingresados es: {porcentaje_de_numeros_negativos}%")
