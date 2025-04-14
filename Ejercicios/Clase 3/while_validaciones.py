# 1) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

# clave_usuario = input("Ingrese su clave: ")
# clave_actual_del_usuario = "hola"

# while clave_usuario != clave_actual_del_usuario:
#     print("La clave ingresada es erronea! Intente de nuevo.")
#     clave_usuario = input("Ingrese su clave: ")

# print("La clave es correcta! Bienvenido.")


# 2) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos. 

# cantidad_de_intentos_disponibles = 3
# clave_actual_del_usuario_2 = "adios"
# clave_usuario = input("Ingrese su clave: ").lower()

# while cantidad_de_intentos_disponibles > 0 and clave_usuario != clave_actual_del_usuario_2:
#     cantidad_de_intentos_disponibles -= 1
#     print(f"La clave ingresada es erronea! Intente de nuevo, le quedan {cantidad_de_intentos_disponibles} intentos.")
#     clave_usuario = input("Ingrese su clave: ")

# if cantidad_de_intentos_disponibles > 0:
#     print("La clave ingresada es correcta! Bienvenido.")
# else:
#     print("Clave erronea! Se quedo sin intentos. ")


# 3) Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

# nota_usuario = int(input("Ingrese una nota: "))

# while nota_usuario < 1 or nota_usuario > 10:
#     nota_usuario = int(input("Ingrese una nota: "))

# print("El número ingresado es valido.")

# 4) Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul. 

# color_usuario = input("Ingrese un color: ").lower()

# while color_usuario != "rojo" and color_usuario != "verde" and color_usuario != "azul":
#     color_usuario = input("Ingrese un color: ").lower()

# print("El color ingresado es valido.")


# Integrador Validaciones
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.

# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.


apellido_usuario = input("Por favor, ingrese su apellido: ")
edad_usuario = int(input("Por favor, ingrese su edad: "))
estado_civil_usuario = input("Por favor, ingrese su estado civil: ").lower()
legajo_usuario = input("Por favor, ingrese su legajo: ")

edad_es_valida = 18 <= edad_usuario <= 90

estado_civil_es_valido = estado_civil_usuario == "soltero" or estado_civil_usuario == "soltera" or estado_civil_usuario == "casado" or estado_civil_usuario == "casada" or estado_civil_usuario == "divorciado" or estado_civil_usuario == "divorciada" or estado_civil_usuario == "viudo" or estado_civil_usuario == "viuda"

legajo_valido = (legajo_usuario.find("0") != 0) and len(legajo_usuario) == 4

while (not edad_es_valida) or (not estado_civil_es_valido) or (not legajo_valido):
    if (not edad_es_valida):
        edad_usuario = int(input("Por favor, ingrese su edad: "))
        edad_es_valida = 18 <= edad_usuario <= 90
    elif (not estado_civil_es_valido):
        estado_civil_usuario = input("Por favor, ingrese su estado civil: ").lower()
        estado_civil_es_valido = estado_civil_usuario == "soltero" or estado_civil_usuario == "soltera" or estado_civil_usuario == "casado" or estado_civil_usuario == "casada" or estado_civil_usuario == "divorciado" or estado_civil_usuario == "divorciada" or estado_civil_usuario == "viudo" or estado_civil_usuario == "viuda"
    else:
        legajo_usuario = input("Por favor, ingrese su legajo: ")
        legajo_valido = (legajo_usuario.find("0") != 0) and len(legajo_usuario) == 4

print(f"Apellido: {apellido_usuario}")
print(f"Edad: {edad_usuario}")
print(f"Estado civil: {estado_civil_usuario}")
print(f"Legajo: {legajo_usuario}")
