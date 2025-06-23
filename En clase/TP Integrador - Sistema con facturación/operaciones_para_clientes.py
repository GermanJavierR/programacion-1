def provincia_del_cliente(cliente):
    """
    Propósito: Indica la provincía del cliente con el id indicado.
    Parametros:
        id_cliente (int): id del cliente del que se quiere saber su provincia.
        lista_de_clientes (list): lista de clientes de la que se va a obtener la provincia del cliente.
    Return: retorna un str que representa la provincia del cliente.
    """
    
    return cliente["provincia"]


def cliente_con_id_en(id_del_cliente, lista_clientes):
    """
    Propósito: Devolver el cliente con el id indicado.
    Parametros:
        id_del_cliente (int) : id por el que se buscará al cliente.
        lista_clientes (list): lista de clientes en la que se va a buscar.
    Return: retorna el incliente con el id indicado.
    """
    for cliente in lista_clientes:
        if cliente["id"] == id_del_cliente:
            return cliente