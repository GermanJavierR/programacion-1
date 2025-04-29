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

metros_consumidos = float(input("Ingrese la cantidad de metros consumidos: "))
tipo_de_cliente = input("Ingrese su tipo de cliente (Residencial, Comercial, Industrial): ").lower()

cargo_fijo = 7000
costo_por_metro = 200
bonificacion = 0
recargo = 0
IVA = 0.21
subtotal = cargo_fijo + (costo_por_metro * metros_consumidos)

match tipo_de_cliente:
    case "residencial":

        if metros_consumidos < 30:
            bonificacion = 0.10
        elif metros_consumidos > 80:
            recargo = 0.15

        if subtotal < 35000:
            bonificacion += 0.05

    case "comercial":
        if metros_consumidos > 300:
            bonificacion = 0.12
        elif metros_consumidos > 150:
            bonificacion = 0.08
        elif metros_consumidos < 50:
            recargo = 0.05

    case "industrial":
        if metros_consumidos > 1000:
            bonificacion = 0.30
        elif metros_consumidos > 500:
            bonificacion = 0.20
        elif metros_consumidos < 200:
            recargo = 0.10

    case _:
        print("El tipo de cliente ingresado no es correcto.")

IVA_a_cobrar = subtotal * IVA
bonificacion_a_cobrar = subtotal * bonificacion
recargo_a_cobrar = subtotal * recargo
subtotal_con_recargo_y_bonificaciones = subtotal + bonificacion_a_cobrar + recargo_a_cobrar
total_final = subtotal_con_recargo_y_bonificaciones + IVA_a_cobrar

print(f"El subtotal del consumo es de ${subtotal:.2f}")

if bonificacion_a_cobrar > 0:
    print(f"La bonificación del servicio es de ${bonificacion_a_cobrar:.2f}")
else:
    print("No hay bonificaciones.")

if recargo_a_cobrar > 0:    
    print(f"El recargo del servicio es de ${recargo_a_cobrar:.2f}")
else:
    print("No hay recargo del servicio.")

print(f"El subtotal con recargo y bonificaciones es de ${subtotal_con_recargo_y_bonificaciones:.2f}")
print(f"El iva a agregar al subtotal es de ${IVA_a_cobrar:.2f}")
print(f"El total final a pagar es de ${total_final:.2f}")