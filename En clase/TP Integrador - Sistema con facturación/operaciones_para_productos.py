def codigos_de_los_productos_en(lista):
    """
    Propósito: Devolver una lista con los códigos de los productos en la lista dada. 
    Parametro: 
        lista (list): lista de productos de la que se quiere obtener sus códigos.
    return: retorna una lista de números que representan los codigos de los productos.
    """
    lista_de_codigos = []
    for i in lista:
        lista_de_codigos.append(i["código"])
    return lista_de_codigos


def descripcion_del_prodcuto_con_codigo_en(codigo, lista_de_productos):
    """
    Propósito: Devolver la descripción del producto con el código ingresado en la lista de productos dada.
    Parametros:
        codigo (str): codigo del producto del que se quiere obtener su descripción.
        lista_de_productos (list): lista de productos.
    Return: retorna una str que es la descripción del producto con el código dado.
    """
    for i in lista_de_productos:
        if i["código"] == codigo:
            return i["descripción"]
        

def precio_del_producto(nombre_del_producto, lista_de_productos):
    """
    Propósito: Indidcar el precio del producto dado.
    Parametros:
        nombre_del_producto (str): nombre del producto que se va a buscar en la lista dada.
        lista_de_productos (list): lista de productos donde se va a buscar el nombre dado.
    Return: retorna el precio del nombre del producto dado.
    """
    for i in lista_de_productos:
        if i["descripción"] == nombre_del_producto:
            return i["precio"]


# productos = [{'código': 'cap1t4n', 'descripción': 'alfajor capitan', 'precio': 1000}, {'código': 'r4st4', 'descripción': 'alfajor rasta', 'precio': 1300}]

# productos.remove({"descripción": 'alfajor capitan'})
# print(productos)


def producto_con_codigo(codigo, lista_de_productos):
    """
    Propósito: retorna el producto con el código ingresado
    Parametros: 
        codigo (str): código del producto que se busca.
        lista_de_productos (list): lista de producto en la que se va a buscar.
    Return: retorna el producto con el código ingresado.
    """
    for i in lista_de_productos:
        if i["código"] == codigo:
            return i