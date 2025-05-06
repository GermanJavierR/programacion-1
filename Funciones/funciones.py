# 1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def devolver_numero_entero(numero_ingresado):
    """
    proposito: devuelve el número entero ingresado por el usuario.

    Parametro:
        numero_ingresado (int): el parametro que se devolverá.
    Returns:
        int: Devuelve el número entero ingresado.
    """
    if isinstance(numero_ingresado, int): #Evalua si el número ingresado es un entero.
        return numero_ingresado
    else:
        return "Lo que ha ingresado no es un entero."



# print(devolver_numero_entero(4.7))

# No sé si está bien así o pide que se pueda ingresar el parametro desde la consola con el input.

# 2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# def devolver_numero_flotante(numero_ingresado):
#     """
#         Proposito: devuelve el numero flotante ingresado.

#         Parametro:
#             numero_ingresado (floar): parametro que se devolverá.
#         Return:
#             float: retorna el número ingresado.
#     """
#     if isinstance(numero_ingresado, float): #Evalua si el número ingresado es un entero.
#         return numero_ingresado
#     else:
#         return "Lo que ha ingresado no es un flotante."
    

def devolver_numero_flotante2(numero_ingresado):
    """
        Proposito: devuelve el numero flotante ingresado.

        Parametro:
            numero_ingresado (floar): parametro que se devolverá.
        Return:
            float: retorna el número ingresado.
    """
    numero = input("Ingrese un número: ")
    if not numero.isdigit() and not numero.isalpha():  # Evalua si el caracter ingresado no es un número entero y si no es caracter alfabetico
        return f"{numero_ingresado} es un flotante"
    else:
        return "Lo que ha ingresado no es un flotante."
    
# No sé si está bien.

# print(devolver_numero_flotante(4))
# print(devolver_numero_flotante(8.5))



# 3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def devolver_cadena(cadena_ingresada):
    """
        Proposito: devuelve la cadena de caracteres ingresada.

        Parametros:
            cadena_ingresada (str): cadena que se va a retornar.

        Return:
            str: retorna la cadena ingresada.
    """
    if isinstance(cadena_ingresada, str):
        return cadena_ingresada
    else:
        return "Lo que ha ingresado no es una cadena de caracteres."

# Intentar usar isalnum()


# 4) Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área

def area_del_rectangulo(base, altura):
    """
        Proposito: retorna el áres de un rectangulo.

        Precondición:
            base (float o int): medida de la base del triangulo
            altura (float o int): medida de la altura del triangulo.

        Return: retorna el resultado de la base por la altura.
    """

    if es_enetro_o_flotante(base) and es_enetro_o_flotante(altura):
        return base * altura
    else:
        return "Alguno de los datos ingresados no es un número."


def es_enetro_o_flotante(numero):
    """
        Propósito: retorna si el dato ingresado es un número

        Parametro:
            numero (float o int): número que se evaluara.

        Return: retorna un bool dependiendo si el elemento ingresado es un número, ya sea int o float.
    """

    return isinstance(numero, int) or isinstance(numero, float)


# print(area_del_rectangulo(3,5))


# 5) Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_del_circulo(radio):
    """
        Proposito: calcula el radio de un circulo.

        Parametro: 
            radio (float): radio del circulo 

        Return: la multiplicación de pi por el radio al cuadrado.
    """
    if es_enetro_o_flotante(radio):
        respuesta = 3.1416 * (radio * radio)
        return f"El area del circulo es {respuesta}"
    else:
        return "No ha ingresado un número valido."


# 6) Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def es_par_o_impar(número):
    """
        Proposito: Indica si el número ingresado ese par o impar.
        Parametro:
            número (int): número a evaluar si es par o impar.
        Return: retorna un string diciendo si el número ingresado es par o impar.
    """
    if isinstance(número, int):
        if número % 2 == 0:
            return f"El número {número} es par."
        else:
            return f"El número {número} es impar."
    else:
        return "No ha ingresado un número entero."
    

# 7) Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def es_par_o_impar2(número):
    """
        Proposito: Indica si el número ingresado ese par o impar.
        Parametro:
            número (int): número a evaluar si es par o impar.
        Return: retorna True si le número ingresado es par y False en el caso contrario.
    """
    if isinstance(número, int):
        return número % 2 == 0
    else:
        return "No ha ingresado un número entero."


# 8) Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def numero_mas_grande_entre_tres(a, b, c):
    """
        Proposito: retornar el número más grande entre los tres dados.
        Parametros:
            a (int o float) : número que se va a comparar con los demás 
            b (int o float) : número que se va a comparar con los demás 
            c (int o float) : número que se va a comparar con los demás 
        Return: retorna el número más grande.
    """
    if es_enetro_o_flotante(a) and es_enetro_o_flotante(b) and es_enetro_o_flotante(c):
        return numero_mas_grande(numero_mas_grande(a, b), c)
    else:
        return "Alguno de los datos ingresados es erroneo."


def numero_mas_grande(a, b):
    """
        Proposito: retorna el número más grande entre los dos dados.
        Parametros:
            a (int o float) : número que se va a comparar con b
            b (int o float) : número que se va a comparar con a
        Return: retorna el número más grande.
    """
    if a > b:
        return a
    else:
        return b

# print(numero_mas_grande_entre_tres(8,2,4))

# 9) Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia_del_numero(base, exponente):
    """
        Proposito: calcular la base elvado al exponente dado.
        Parametros:
            base (int o float) : base a la que se multiplicará por si misma.
            exponente (int or float) : cantidad de veces por la que se multiplicará la base.
        Return: retorna el resultado de la base multiplicada por si misma tanta veces por el exponente dado.
    """
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado 

# print(potencia_del_numero(3,3))

# 10) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def es_primo(numero):
    """
        Propósito: Indicar si el número es primo.
        Parametro:
            numero (int) : número al cual se evaluar si es primo o no.
        Return: retorna True si el número ingresado es primo, en caso contrario retorna False.
    """
    cantidad_de_divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cantidad_de_divisores += 1

    return cantidad_de_divisores == 2

# print(es_primo(11))

# 11) Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

# 12) Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

# 13) Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.



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
    sin_el_punto = ""
    cantidad_de_puntos = 0
    
    for i in str(valor):
        if i == ".":
            cantidad_de_puntos += 1
        else:
            sin_el_punto += i

    return sin_el_punto.isdigit() and cantidad_de_puntos == 1


print(es_float("3.14"))
print(es_float(3.14))
print(es_float("texto"))
print(es_float("12"))
print(es_float(12))
print(es_float(None))

"""
🔹 Enunciado 2: Validar número entero (int)
Objetivo: Crear una función que valide si un valor puede interpretarse como un número entero.

Enunciado:
Escribí una función llamada es_entero(valor) que reciba un solo parámetro. La función debe retornar True si el valor puede convertirse a int, ya sea que venga como string ("5") o como número (5), y False en caso contrario.
Probá tu función con valores como "5", 5, "5.0", 5.0, "cinco" y None.
"""

def es_entero(valor):
    """
        Propósito:
        Parametro:
        Return:
    """
    pass



"""
🔹 Enunciado 3: Validar si un valor es alfanumérico
Objetivo: Crear una función que verifique si un string es estrictamente alfanumérico.

Enunciado:
Escribí una función llamada es_alfanumerico(valor) que reciba un parámetro y devuelva True si es un string compuesto únicamente por letras y/o números (sin espacios, símbolos o acentos), y False en caso contrario.
Probá la función con valores como "Hola123", "hola mundo", "123", "!!!", "" y None.
"""
    
# numero = 4.5
# print(numero.is_integer()) 

# numero2 = "12.5"
# print(numero2.isdigit())

# for i in numero:
#     if i == ".":
        # print("Es float")
    
# hola = str("hola")
# print(hola)

# nuevo_texto = ""

# for i in "hola":
#     if i == "h":
#         continue
#     nuevo_texto += i

# print(nuevo_texto)