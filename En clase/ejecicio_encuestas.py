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