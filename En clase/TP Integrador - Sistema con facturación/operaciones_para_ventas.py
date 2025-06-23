from operaciones_para_productos import codigos_de_los_productos_en, descripcion_del_prodcuto_con_codigo_en


# print("20-01-1999".split("-"))


def ingresar_producto_y_cantidad(lista_de_productos):
    """
    Propósito: Devuelve una lista de tuplas que contienen el nombre de un producto y la cantidad que se compro de este.
    parametro: 
        lista_de_productos (list): lista de productos
    Return: retorna una lista de tuplas.
    """
    lista_de_tuplas = []
    lista_productos = codigos_de_los_productos_en(lista_de_productos)
    continuar = "si"
    while continuar != "no":
        codigo_producto = input("Ingrese el código del producto: ").strip()
        if codigo_producto in lista_productos:
            nombre_del_producto = descripcion_del_prodcuto_con_codigo_en(codigo_producto, lista_de_productos)
            cantidad = int(input(f"Ingrese la cantidad que compro del producto {nombre_del_producto}: "))
            lista_de_tuplas.append((nombre_del_producto, cantidad))
            continuar = input("¿Desea seguir ingresado productos y cantidades? 'Si/No': ").lower()
        else:
            print("El código ingresado no corresponde a ningún producto.")
            continuar = input("¿Desea seguir ingresado productos y cantidades? 'Si/No': ").lower()
    return lista_de_tuplas


def obtener_descripcion_de_todos_los_productos_vendidos(lista_de_ventas):
    """
    Propósito: Obtener todos los nombres de los productos vendidos.
    Parametro:
        lista_de_ventas (list): lista de ventas realizadas.
    Return: retorna un set con las descripciones de los productos vendidos sin repetición.
    """
    lista_de_productos = set()
    for venta in lista_de_ventas:
        for producto in venta["lista de compras"]:
            lista_de_productos.add(producto[0])
    return lista_de_productos

# ventas = [{'cliente': 1, 'fecha': "20-01-2025", 'lista de compras': [('alfajor rasta', 2), ('alfajor capitan', 4)]}, {'cliente': 2, 'fecha': "25-06-2025", 'lista de compras': [('alfajor rasta', 3)]}, {'cliente': 1, 'fecha': "26-06-2025", 'lista de compras': [('alfajor rasta', 4)]}]

# print(obtener_descripcion_de_todos_los_productos_vendidos(ventas))

# producto_vendidos = obtener_descripcion_de_todos_los_productos_vendidos(ventas)

# print("alfajor capitan" in producto_vendidos)


# lista = [1,2,3]
# print(lista.index(2))


def obtener_clientes_que_compraron_productos(lista_ventas):
    """
    Propósito: obtener los clientes que realizaron una compra.
    Parametro:
        lista_ventas (list): lista de ventas realizadas.
    Return: retorna un set con los id de los clientes que realizaron una compra.
    """
    set_de_clientes = set()
    for venta in lista_ventas:
        set_de_clientes.add(venta["id del cliente"])
    return set_de_clientes