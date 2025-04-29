"""
Ejercicio:

Escribí un programa en Python que le pida al usuario ingresar su edad.

Si la edad es menor a 0 o mayor a 120, mostrar un mensaje que diga: "Edad inválida".

Si la edad es menor a 13, mostrar: "Acceso denegado. Debes tener al menos 13 años para entrar."

Si la edad está entre 13 y 17 inclusive, mostrar: "Acceso restringido. Estás en modo adolescente."

Si la edad es 18 o más, mostrar: "Acceso completo concedido."

"""
# edad_usuario = int(input("Por favor, ingrese su edad: "))

# if edad_usuario < 0 or edad_usuario > 120:
#     print("Edad inválida")
# elif edad_usuario < 13:
#     print("Acceso denegado. Debes tener al menos 13 años para entrar.")
# elif edad_usuario <= 17:
#     print("Acceso restringido. Estás en modo adolescente.")
# else:
#     print("Acceso completo concedido.")


"""
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
"""

# altura_del_jugador = int(input("Por favor, ingrese su altura en centimetros: "))

# if altura_del_jugador > 280:
#     print("La altura ingresada no es valida.")
# elif altura_del_jugador < 160:
#     print("Tu posición es Base.")
# elif altura_del_jugador <= 179:
#     print("Tu posición es Escolta.")
# elif altura_del_jugador <= 199:
#     print("Tu posición es Alero.")
# else:
#     print("Tu posición es Ala-Pívot o Pívot.")


"""
Facturación del Servicio de Agua Potable
El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.

Tarifa base:
Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
El costo por metro cúbico (m³) de agua es de $200/m³.

Bonificaciones y Recargos según tipo de cliente:

Cliente Residencial:
    Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
    Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

Cliente Comercial:
    Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
    Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
    Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

Cliente Industrial:
    Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
    Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%
    Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

Casos especiales:
    Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.

En todos los casos, se aplica el IVA del 21% sobre el total.

Requerimientos del programa:

Solicitar al usuario:
    Cantidad de metros consumidos
    Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.

Calcular:
    Subtotal de consumo.
    Bonificaciones, si corresponde
    Recargos, si corresponde
    Subtotal, con recargos y bonificaciones.
    IVA aplicado (21%), si corresponde.
    Total final a pagar.

Mostrar en pantalla el desglose de los cálculos.

"""

# metros_consumidos = float(input("Ingrese la cantidad de metros consumidos: "))
# tipo_de_cliente = input("Ingrese su tipo de cliente (Residencial, Comercial, Industrial): ").lower()

# cargo_fijo = 7000
# costo_por_metro = 200
# bonificacion = 0
# recargo = 0
# IVA = 0.21
# subtotal = cargo_fijo + (costo_por_metro * metros_consumidos)

# match tipo_de_cliente:
#     case "residencial":

#         if metros_consumidos < 30:
#             bonificacion = 0.10
#         elif metros_consumidos > 80:
#             recargo = 0.15

#         if subtotal < 35000:
#             bonificacion += 0.05

#     case "comercial":
#         if metros_consumidos > 300:
#             bonificacion = 0.12
#         elif metros_consumidos > 150:
#             bonificacion = 0.08
#         elif metros_consumidos < 50:
#             recargo = 0.05

#     case "industrial":
#         if metros_consumidos > 1000:
#             bonificacion = 0.30
#         elif metros_consumidos > 500:
#             bonificacion = 0.20
#         elif metros_consumidos < 200:
#             recargo = 0.10

#     case _:
#         print("El tipo de cliente ingresado no es correcto.")

# IVA_a_cobrar = subtotal * IVA
# bonificacion_a_cobrar = subtotal * bonificacion
# recargo_a_cobrar = subtotal * recargo
# subtotal_con_recargo_y_bonificaciones = subtotal + bonificacion_a_cobrar + recargo_a_cobrar
# total_final = subtotal_con_recargo_y_bonificaciones + IVA_a_cobrar

# print(f"El subtotal del consumo es de ${subtotal:.2f}")

# if bonificacion_a_cobrar > 0:
#     print(f"La bonificación del servicio es de ${bonificacion_a_cobrar:.2f}")
# else:
#     print("No hay bonificaciones.")

# if recargo_a_cobrar > 0:    
#     print(f"El recargo del servicio es de ${recargo_a_cobrar:.2f}")
# else:
#     print("No hay recargo del servicio.")

# print(f"El subtotal con recargo y bonificaciones es de ${subtotal_con_recargo_y_bonificaciones:.2f}")
# print(f"El iva a agregar al subtotal es de ${IVA_a_cobrar:.2f}")
# print(f"El total final a pagar es de ${total_final:.2f}")


# redondeo de flotante round(subtotal.2) o f"${subtotal:.2f}" se pone 2f porque son dos decimales y la f por flotante.


# break, continue

# for i in range(1, 11):
#     if i == 5: # Si el valor actual es igual a 5.
#         continue # Salta esta iteración
#     print(i) # Imprime el número actual.


# for i in range(1, 11):
#     if i == 5:
#         break # Termina la iteración en este punto.
#     print(i)


# for para cantidad de vueltas definidas y el while para cuando no hay un limite definido.


# tarea: realizar un algoritmo donde se le pida al user que elija entre un producto u otro, pero que decida cuantas encuentas desea contestar (cada iteracion es un user)

cantidad_de_encuentas = int(input("Por favor, ingrese un número para indicar la cantidad de encuentas que quiere contestar: "))

cantidad_de_votos_para_producto_a = 0
cantidad_de_votos_para_producto_b = 0

while cantidad_de_encuentas != 0:
    producto_ingresado = input("Por favor, indique si eligue el producto \"a\" o el producto \"b\": ").lower()
    match producto_ingresado:
        case "a":
            cantidad_de_votos_para_producto_a += 1
        case "b":
            cantidad_de_votos_para_producto_b += 1
        case _:
            print("El valor ingresado no corresponde con algunas de las opciones! Ingrese un valor valido.")
            continue
    cantidad_de_encuentas -= 1

print(f"La cantidad de votos para el producto \"a\" es de {cantidad_de_votos_para_producto_a}")
print(f"La cantidad de votos para el producto \"b\" es de {cantidad_de_votos_para_producto_b}")