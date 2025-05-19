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


# Validación para saber si es un número entero.

def es_un_numero_entero_positivo(valor):
    return isinstance(valor, int) >= 0


# Validación para saber si es un número.

def es_un_numero(valor):
    return es_entero(valor) or es_float(valor) or es_un_numero_negativo(valor)


# Validación para saber si el valor ingresado es un número negativo.

def es_un_numero_negativo(valor):
    """
    Propósito: Indicar si el valor ingresado es un número negativo
    Parametro:
    Return: 
    """
    if (isinstance(valor, int) or isinstance(valor, float)) and valor < 0 :
        return True
    elif type(valor) == str:
        partes_del_string = valor.split("-")
        
        return len(partes_del_string) == 2 and partes_del_string[0] == "" and es_un_numero(partes_del_string[1])
    else:
        return False

# print(es_un_numero_negativo(4))
# print(es_un_numero_negativo(4.4))
# print(es_un_numero_negativo(-4))
# print(es_un_numero_negativo(-4.5))
# print(es_un_numero_negativo("4"))
# print(es_un_numero_negativo("4.5"))
# print(es_un_numero_negativo("-4"))
# print(es_un_numero_negativo("-4.5"))
# print(es_un_numero_negativo("hola"))
# print(es_un_numero_negativo(None))

# print("4.5".split("-"))
# print("-4.5".split("-"))

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

# print("-4".split("-"))


# -------------------------------------------------------------------------------------------------------------------- #

# Lista

def todos_los_elementos_de_la_lista_son(lista, tipo):
    if type(lista) == list:
        if lista == []:
            return False
        else:
            todos_son_del_mismo_tipo = True
            for i in range(len(lista)):
                todos_son_del_mismo_tipo = todos_son_del_mismo_tipo and type(lista[i]) == tipo
            return todos_son_del_mismo_tipo
    else:
        return "No ha ingresado un lista."
    

# print(todos_los_elementos_de_la_lista_son(1, int))
# print(todos_los_elementos_de_la_lista_son([1,2,3], int))
# print(todos_los_elementos_de_la_lista_son([1,2,"hola"], int))
# print(todos_los_elementos_de_la_lista_son([True, 1], int))
# print(todos_los_elementos_de_la_lista_son("1", int))
# print(todos_los_elementos_de_la_lista_son(["","2","hola"], str))
# print(todos_los_elementos_de_la_lista_son(None, None))
# print(todos_los_elementos_de_la_lista_son([1,2,"hola"], None))
# print(todos_los_elementos_de_la_lista_son([1,2], None))


def todos_los_str_son_alpha(lista):
    """
    Propósito: Indicar si todos los str en la lista son alpha.
    Parametro:
        lista (list): lista de la que se quiere saber si todos los str son alpha.
    Retunr: Retorna True si todos los elementos son alpha, en caso contrario retorna False.
    """
    if todos_los_elementos_de_la_lista_son(lista, str):
        todos_son_alpha = True
        for i in lista:
            todos_son_alpha = todos_son_alpha and i.isalpha()
        return todos_son_alpha
    else:
        return "No ha ingresado una lista de strings."
    

# print(todos_los_str_son_alpha(["hola", "Germán","!"]))


def esta_en_la_lista(elemento, lista):
    """
    Propósito: indica si el elemento ingresado se encuentra en la lista dada.
    Parametros:
        elemento: elemento que se va a buscar en la lista.
        lista: lista en la que se buscará el elemento dado.
    Return: en caso de que el elemento este en la lista retorna True, en caso contrario retorna False.
    """
    for i in lista:
        if i == elemento:
            return True
    
    return False


def lista_sin_repeticiones(lista):
    """
    Propósito: armar una nueva lista basada en la lista dada sin repetidos.
    Parametro:
        lista (list): lista en la cual se basará la nueva lista.
    Return: retorna una lista.
    """
    if isinstance(lista, list):
        nueva_lista = []
        for i in lista:
            if not esta_en_la_lista(i, nueva_lista):
                nueva_lista += [i]
        return nueva_lista
    else:
        return "El elemento ingresado no es una lista."
    
