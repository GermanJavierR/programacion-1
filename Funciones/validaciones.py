# Ejercicio de validación.

"""
🔹 Enunciado 1: Validar número decimal (float)
Objetivo: Crear una función que valide si un valor recibido como parámetro (string o número) puede interpretarse como un número decimal.

Enunciado:
Escribí una función llamada es_float(valor) que reciba un solo parámetro. La función debe retornar True si el valor puede convertirse a float, ya sea que venga como string (por ejemplo, "3.14") o como número (3.14), y False en caso contrario.
Probá tu función con distintos valores como "3.14", 3.14, "texto", "12", 12, y None.
"""

def es_float(valor):
    """
        Propósito: valida si la variable ingresada es un flotante.
        Parametro:
            valor (string o número) : valor a validar.
        Return: retorna True si la variable ingresada es un flotante.
    """
    if type(valor) == float:
        return True
    elif type(valor) == str:
        sin_el_punto = ""
        cantidad_de_puntos = 0
    
        for i in str(valor):
            if i == ".":
                cantidad_de_puntos += 1
            else:
                sin_el_punto += i

        return sin_el_punto.isdigit() and cantidad_de_puntos == 1
    else:
        return False


# print(es_float("3.14"))
# print(es_float(3.14))
# print(es_float("texto"))
# print(es_float("12"))
# print(es_float(12))
# print(es_float(None))


"""
🔹 Enunciado 2: Validar número entero (int)
Objetivo: Crear una función que valide si un valor puede interpretarse como un número entero.

Enunciado:
Escribí una función llamada es_entero(valor) que reciba un solo parámetro. La función debe retornar True si el valor puede convertirse a int, ya sea que venga como string ("5") o como número (5), y False en caso contrario.
Probá tu función con valores como "5", 5, "5.0", 5.0, "cinco" y None.
"""

def es_entero(valor):
    """
        Propósito: validar si el valor ingresado es un entero.
        Parametro:
            valor (str o número) : valor a evaluar si es un entero
        Return: retornara True si el valor ingresado es un entero o False en el caso contrario.
    """

    if type(valor) == int:
        return True
    elif type(valor) == str:
        var = ""
    
        for i in valor:
            var += i
    
        return var.isdigit()
    else:
        return False
    


# print(es_entero("5"))
# print(es_entero(5))
# print(es_entero("5.0"))
# print(es_entero(5.0))
# print(es_entero("cinco"))
# print(es_entero(None))


"""
🔹 Enunciado 3: Validar si un valor es alfanumérico
Objetivo: Crear una función que verifique si un string es estrictamente alfanumérico.

Enunciado:
Escribí una función llamada es_alfanumerico(valor) que reciba un parámetro y devuelva True si es un string compuesto únicamente por letras y/o números (sin espacios, símbolos o acentos), y False en caso contrario.
Probá la función con valores como "Hola123", "hola mundo", "123", "!!!", "" y None.
"""

def es_alfanumerico(valor):
    """
        Propósito: Validar si el valor ingresado es alfanumerico.
        Parametro:
            valor (str) : valor a evaluar si es alfanumerico.
        Return: retorna True en  caso de que la cadena ingresada sea estrictamente alfanumerico, en caso contrario retorna False.
    """
    if valor == None:
        return False
    else: 
        var = str(valor).lower()
        return not contiene_acentos(valor) and var.isalnum()
    

def contiene_acentos(valor):
    """
        Propósito: Indicar si el valor ingresado tiene alguna letra con acento.
        Parametro:
            valor (str) : valor a validar si tiene algún acento.
        Return: retorna True si la cadena ingresada contiene alguna letra con acento, en caso contrario retorna False.
    """
    if valor == None or isinstance(valor, int) or isinstance(valor, float) or isinstance(valor, bool):
        return False
    else:
        var = str(valor).lower()
        return ("á" in var) or ("é" in var) or ("í" in var) or ("ó" in var) or ("ú" in var)


# print(es_alfanumerico("Hola123"))
# print(es_alfanumerico("hola mundo"))
# print(es_alfanumerico("123"))
# print(es_alfanumerico("!!!"))
# print(es_alfanumerico(""))
# print(es_alfanumerico(None))