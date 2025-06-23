from cargar_cliente import cargar_cliente
from cargar_producto import cargar_producto
from cargar_venta import registrar_ventas
from mostrar_clientes_y_productos import mostrar_clientes_y_productos
from buscar_clientes import buscar_por_provincia
from detalles_de_ventas import detalle_de_ventas
from eliminar_producto import eliminar_producto
from eliminar_cliente import eliminar_cliente


def mostrar_menu():
    """
    Propósito: Mostrar las operaciones disponibles como un menu.
    Return: imprime en la consola todas las operaciones disponibles a realizar.
    """
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cargar cliente")
    print("2. Cargar producto")
    print("3. Registrar venta")
    print("4. Mostrar clientes y productos")
    print("5. Buscar clientes por provincia")
    print("6. Mostrar detalle de ventas")
    print("7. Eliminar un producto")
    print("8. Eliminar un cliente")


continuar = "si"
while continuar != "no":
    mostrar_menu()
    operacion_a_realizar = input("Ingrese el número de la operación que desea realizar: ")
    match operacion_a_realizar:
        case "1":
            cargar_cliente()
        case "2":
            cargar_producto()
        case "3":
            registrar_ventas()
        case "4":
            mostrar_clientes_y_productos()
        case "5":
            buscar_por_provincia()
        case "6":
            detalle_de_ventas()
        case "7":
            eliminar_producto()
        case "8":
            eliminar_cliente()
    continuar = input("¿Desea realizar otra operación? \"Si/No\": ").lower()