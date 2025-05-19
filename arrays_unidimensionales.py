# 1) Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

from Modulos.validaciones import es_un_numero_entero_positivo, es_un_numero

def crear_array_de_numeros(numero):
    """
    Propósito: devuelve una array con tantos números como se le indique.
    Parametro: 
        numero (int): cantidad de elementos que tendra la array.
    Return: retorna una array con tantos elementos como se le indico.
    """
    
    if es_un_numero_entero_positivo(numero):
        nueva_array = []
        for i in range(numero):
            nueva_array += [i]
        return nueva_array
    else:
        return "El valor ingresado no es un número entero."

# print(crear_array_de_numeros(3))

# Preguntar si está bien o podía otra cosa.


# 2) Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

def cantidad_de_numeros_a_ingresar_a_la_array(cantidad_de_elementos):
    """
    Propósito: devuelve una array con tantos números como se le indique.
    Parametro: 
        numero (int): cantidad de elementos que tendra la array.
    Return: retorna una array con tantos elementos como se le indico.
    """

    if es_un_numero_entero_positivo(cantidad_de_elementos):

        nueva_array = crear_array_de_numeros(cantidad_de_elementos)

        for i in range(len(nueva_array)):

            elemento_a_agregar = input("Por favor, ingrese un número para la lista: ")

            while not es_un_numero(elemento_a_agregar):
               print("El valor ingresado no es un número. Por favor, intente de nuevo.")
               elemento_a_agregar = input("Por favor, ingrese un número para la lista: ")

            nueva_array[i] = int(elemento_a_agregar)

        return nueva_array
    else:
        return "El valor ingresado no es un número entero positivo."

# print(cantidad_de_numeros_a_ingresar_a_la_array(3))



# 3) Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 

from Modulos.validaciones import todos_los_elementos_de_la_lista_son


def todos_los_elementos_son_numeros(lista):
    """
    Propósito: Indicar si todos los elementos de la lista dada son números.
    Parametros:
        lista (list): lista a evaluar sus elementos.
    Return: return True en caso de que todos los elementos de la lista sean números, en caso contrario retorna False.
    """
    return isinstance(lista, list) and todos_los_elementos_de_la_lista_son(lista, int)


def promedio_de_la_lista(lista_de_numeros):
    """
    Propósito: Indicar el promedio de los números de la lista.
    Parametros:
        lista_de_numeros (list): lista de números a la que se calculara el promedio.
    Return: retorna el promedio de los elementos de la lista ingresada.
    """

    if todos_los_elementos_son_numeros(lista_de_numeros):
        suma_total = 0
        for i in range(len(lista_de_numeros)):
            suma_total += lista_de_numeros[i]
        return suma_total / len(lista_de_numeros)
    else:
        return "No ha ingresado un lista de números valida o ingresaste una lista vacía."
    

# print(promedio_de_la_lista([1,2,3,4,5,6,1,-8, -15, -8]))



# 4) Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

def promedio_de_los_positivos_en_la_lista(lista_de_numeros):
    """
    Propósito: Devolver el promedio de los positivos de la lista dada.
    Parametros: 
        lista_de_numeros (list): lista de números de la cual solo se sacará el promedio de los positivos.
    Return: retorna el promedio de los positivos de la lista dada.
    """
    if todos_los_elementos_son_numeros(lista_de_numeros):
        lista_solo_de_positivos = []
        for i in range(len(lista_de_numeros)):
            if lista_de_numeros[i] > 0:
                lista_solo_de_positivos += [lista_de_numeros[i]]
        return promedio_de_la_lista(lista_solo_de_positivos)
    else:
        return "Alguno de los elementos de la lista ingresado no es un número o ingresaste una lista vacía."  


# print(promedio_de_los_positivos_en_la_lista([1,2,3,4,5,-8, -15, -8]))


# 5) Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def producto_de_la_lista(lista):
    """
    Propósito: calcular el producto de la lista.
    Parametro:
        lista (list): lista de la cual se sacará el producto.
    Return: retorna el producto de todos los elementos de la lista.
    """
    if todos_los_elementos_son_numeros(lista):
        producto_total = 1
        for i in range(len(lista)):
            producto_total *= lista[i]
        return producto_total
    else:
        return "Alguno de los elementos de la lista ingresada no es un número, ingresaste una lista vacía o no ingresaste una lista."


# print(producto_de_la_lista([1,2,3,4,5,-8, -15, -8]))


# 6) Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def posicion_del_int_mas_grande(lista):
    """
    Propósito: Indicar la posición del número entero más grande.
    Parametro:
        lista (list): lista de números de la que se sacará la posición del número entero más alto.
    Return: retorna un entero referido a la posición del número entero más alto en la lista dada.
    """
    if todos_los_elementos_de_la_lista_son(lista, int):
        numero_mas_grande = numero_mas_grande_de_la_lista(lista)
        return f"La posición del elemento más grande en las es: {lista.index(numero_mas_grande)}" # .index() devuelve la primera posición que encuentre del elemento que le indiquemos.
    else:
        return "Alguno de los elementos de la lista no es un número, ingresaste una lista vacía o no ingresaste una lista."

def numero_mas_grande_de_la_lista(lista):
    """
    Propósito: Indicar cual es el número más grande la lista dada.
    Parametro:
        lista (list): lista de números en la cual se buscará el número más grande.
    Return: retorna el número más grande de la lista.
    """
    if todos_los_elementos_de_la_lista_son(lista, int):
        numero_mas_grande = float("-inf")
        for i in range(len(lista)):
            if lista[i] > numero_mas_grande:
                numero_mas_grande = lista[i]
        return numero_mas_grande
    else:
        return "No se ha ingresado una lista de números enteros."

# Se puede usar .index() o lo tengo que hacer de otra manera?

# print(todos_los_elementos_de_la_lista_son([], int))
# print(producto_de_la_lista([]))
# print(posicion_del_int_mas_grande([1,2,3,4,5,-8, -15, -8]))
# print(posicion_del_int_mas_grande([103,2,26,4,5,-8, -15, -8]))
# print(posicion_del_int_mas_grande([103,2,26,4,5,-8, -15, 531]))


# 7) Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def posicion_o_posiciones_del_int_mas_grande(lista):
    """
    Propósito: Muestra la/las posiciones en donde se encuentra/n el/los valor/es máximo/s hallado/s.
    Parametros:
        lista (list): lista de números enteros donde se buscara el valor o los valores más altos.
    Return: Retorna el/los valor/es más alto/s hallado/s.
    """
    if todos_los_elementos_de_la_lista_son(lista, int):
        posicion_de_valor_o_valores_maximos = []
        valor_maximo = numero_mas_grande_de_la_lista(lista)
        for i in range(len(lista)):
            if lista[i] == valor_maximo:
                posicion_de_valor_o_valores_maximos += [i]
        return f"Las posiciones con los valores más grande de la lista son las posiciones: {posicion_de_valor_o_valores_maximos}"
    else:
        return "No se ha ingresado una lista solo de enteros."


print(posicion_o_posiciones_del_int_mas_grande([103,2,26,4,103,-8, -15, -8,103]))
# print([1,3,3,4,4].index(4))


# 8) Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
#   Una lista de nombres (lista_nombres).
#   Un nombre a buscar en la lista (nombre_antiguo).
#   Un nombre de reemplazo (nombre_nuevo).
# La función debe realizar las siguientes acciones:
# Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
# Retornar la cantidad total de reemplazos realizados.

from Modulos.validaciones import todos_los_str_son_alpha

def reemplazar_nombre(lista, nombre_antiguo, nuevo_nombre):
    """
    Propósito: reemplazar el nombre antiguo dado en la lista por el nuevo nombre también dado.
    Parametros:
        lista (list nombres): Lista en la cual se reemplazará el nombre antiguo por el nuevo.
        nombre_antiguo (str): nombre que se va a reemplazar.
        nombre_nuevo (str): nombre que ocupara el lugar del anterior.
    Return: retorna la lista dada con el el nuevo nombre en el lugar del distinto.
    """
    if todos_los_elementos_de_la_lista_son(lista, str) and todos_los_str_son_alpha(lista):
        posiciones_del_nombre_antiguo = posicion_o_posiciones_del_str_en_la_lista(lista, nombre_antiguo)
        nueva_lista = lista
        for i in posiciones_del_nombre_antiguo:
            nueva_lista[i] = nuevo_nombre
        return nueva_lista 
    else:
        return "No ha ingresado una lista de str que solo contengan caracteres alfabeticos."


def posicion_o_posiciones_del_str_en_la_lista(lista, string):
    """
    Propósito: Indicar los indices en donde se encuentre el nombre dado en la lista dada.
    Parametros: 
        lista (list): lista de nombre en los que se buscará el nombre dado.
        nombre (str): nombre que se buscará en la lista.
    Return: retorna una lista de ints que representan
    """
    if todos_los_elementos_de_la_lista_son(lista, str):
        posiciones_del_str = []
        for i in range(len(lista)):
            if lista[i] == string:
                posiciones_del_str += [i]
        return posiciones_del_str
    else:
        return "No ha ingresado una lista valida."


lista1 = [1,2,3]
lista2 = ["Germán", "Damián", 1]
lista3 = ["Germán", "Damián", "Matias", "Damián"]

# print(reemplazar_nombre(lista1, "Damián", "Melany"))
# print(reemplazar_nombre(lista2, "Damián", "Melany"))
# print(reemplazar_nombre(lista3, "Damián", "Melany"))


# 9) Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

from Modulos.validaciones import esta_en_la_lista, lista_sin_repeticiones

def interseccion_entre_dos_lista(lista1, lista2):
    """
    Propósito: mostrar la intersección de los arrays dados.
    Parametros:
        lista1 (list): primera lista que se verá que elementos tiene en común con la segunda lista ingresada.
        lista2 (list): segunda lista que se verá que elementos tiene en común con la primera.
    Return: retorna una nueva lista con la intersección de las listas dadas.
    """
    if isinstance(lista1, list) and isinstance(lista2, list):
        nueva_lista = []
        for i in range(len(lista2)):
            if esta_en_la_lista(lista2[i], lista1):
                nueva_lista += [lista2[i]]
        return nueva_lista
    else:
        return "Alguno de los parametros ingresados no es una lista."
    
# No tiene elementos repetidos está intersección.

print(interseccion_entre_dos_lista(lista1, lista2))
print(interseccion_entre_dos_lista(lista3, lista2))




# 10) Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

def union_de_dos_arrays(lista1, lista2):
    """
    Propósito:
    Parametros:
    Return:
    """
    if isinstance(lista1, list) and isinstance(lista2, list):
        nueva_lista = lista_sin_repeticiones(lista1)
        for i in range(len(lista2)):
            if not esta_en_la_lista(lista2[i], nueva_lista):
                nueva_lista += [lista2[i]]
        return nueva_lista
    else:
        return "Alguno de los parametros ingresados no es una lista."

# Union sin elementos repetidos repeticiones.

# 11) Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.


