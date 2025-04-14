# 1) Mostrar los números ascendentes desde el 1 al 10

# for numero in range(1, 11):
#     print(numero)


# 2) Mostrar los números descendentes desde el 10 al 1

# for numero in reversed(range(11)):
#     print(numero)


# 3) Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

# numero_inicial = int(input("Ingrese un número: "))

# for numero in range(numero_inicial + 1):
#     print(numero)


# 4) Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5: 
#   5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15
#   ...

# numero_de_la_tabla = int(input("Ingrese el número de la tabla que desea ver: "))

# for numero in range(11):
#     print(f"{numero_de_la_tabla} x {numero} = {numero * numero_de_la_tabla}")


# 5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma_actual = 0
cantidad_de_numeros = 0

for numero in range(10):
    numero_ingresado = int(input("Ingrese un número o 0 para terminar: "))
    if numero_ingresado != 0:    
        suma_actual += numero_ingresado
        cantidad_de_numeros += 1
    else:
        break

if cantidad_de_numeros != 0:
    promedio = suma_actual / cantidad_de_numeros
else:
    promedio = 0

print(f"La suma de los números ingresados es: {suma_actual}")
print(f"El promedio de los números ingresados es: {promedio}")


# 6) Imprimir los números múltiplos de 3 entre el 1 y el 10.



# 7) Mostrar los números pares que hay desde la unidad hasta el número 50.


# 8) Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:


# 9) Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.


# 10) Ingresar un número. Determinar si el número es primo o no.


# 11) Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
