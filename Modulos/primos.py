def es_primo(numero_ingresado):
    """
    Propósito: Indicar si el número ingresao es primo o no.
    Parametro:
        numero_ingresado (int): número a evaluar si es primo.
    Return: Retorna True si el número ingresado es primo, en caso contraio retorna False
    """

    if numero_ingresado == 1:
        return False
    else:
        cantidad_de_numero_que_lo_dividen = 0

        for numero in range(1, numero_ingresado + 1):
            if numero_ingresado % numero == 0:
                cantidad_de_numero_que_lo_dividen += 1
            if cantidad_de_numero_que_lo_dividen == 3 and numero != numero_ingresado:
                continue
        
        return cantidad_de_numero_que_lo_dividen == 2
    

def cantidad_de_primos_hasta(numero):
    cantidad_de_numero_primos_totales = 0

    for numero_actual in range(1, numero + 1):
        if es_primo(numero_actual):
            cantidad_de_numero_primos_totales += 1
    
    return cantidad_de_numero_primos_totales


def imprimir_primos_hasta(numero):
    for numero_actual in range(1, numero + 1):
        if es_primo(numero_actual):
            print(numero_actual)

def imprimir_y_mostrar_la_cantidad_de_primos_hasta(numero):
    imprimir_primos_hasta(numero)
    cantidad_de_primos_hasta(numero)

# cantidad_de_numero_primos_totales = 0

# for numero in range(1, numero_ingresado + 1):
#     cantidad_de_numero_que_lo_dividen = 0

#     for numero1 in range(1, numero + 1):
#         if numero % numero1 == 0:
#             cantidad_de_numero_que_lo_dividen += 1

#     if cantidad_de_numero_que_lo_dividen == 2:
#             print(numero)
#             cantidad_de_numero_primos_totales += 1