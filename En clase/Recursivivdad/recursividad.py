# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print("El factorial de 5 es:", factorial(5))


# def cuenta_regresiva(n):
#     if n == 0:
#         print("¡Despegue!")
#     else:
#         print(n)
#         cuenta_regresiva(n - 1)

# cuenta_regresiva(5)

from Factorial import factorial

def pedir_y_calcular_factorial():
    numero = input("Ingrese un número entero positivo: ")
    if numero.isnumeric():
        numero = int(numero)
        if numero >= 0:
            print("El factorial de", numero, "es:", factorial(numero))
        else:
            print("Debe ingresar un número mayor o igual a cero.")
    else:
        print("Error: debe ingresar solo números.")


pedir_y_calcular_factorial()

# Intentar modularizar esto.