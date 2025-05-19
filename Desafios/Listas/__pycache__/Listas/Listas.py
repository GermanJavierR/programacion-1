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


# lista1 = [1,2,3,4,5]

# print(esta_en_la_lista(2, lista1))


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

