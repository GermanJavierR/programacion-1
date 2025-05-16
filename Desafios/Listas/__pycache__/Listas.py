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