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

def devolver_numero_flotante(numero_ingresado):
    """
        Proposito: devuelve el numero flotante ingresado.

        Parametro:
            numero_ingresado (floar): parametro que se devolverá.
        Return:
            float: retorna el número ingresado.
    """
    if isinstance(numero_ingresado, float): #Evalua si el número ingresado es un entero.
        return numero_ingresado
    else:
        return "Lo que ha ingresado no es un flotante."
    

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

def es_par_o_impar(numero):
    """
        Proposito: Indica si el número ingresado ese par o impar.
        Parametro:
            numero (int): número a evaluar si es par o impar.
        Return: retorna un string diciendo si el número ingresado es par o impar.
    """
    if isinstance(numero, int):
        if numero % 2 == 0:
            return f"El número {numero} es par."
        else:
            return f"El número {numero} es impar."
    else:
        return "No ha ingresado un número entero."
    

# 7) Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def es_par_o_impar2(numero):
    """
        Proposito: Indica si el número ingresado ese par o impar.
        Parametro:
            número (int): número a evaluar si es par o impar.
        Return: retorna True si le número ingresado es par y False en el caso contrario.
    """
    if isinstance(numero, int):
        return numero % 2 == 0
    else:
        return "No ha ingresado un número entero."


# print(es_par_o_impar2(2))
# print(es_par_o_impar2(2.5))
# print(es_par_o_impar2("hola"))
# print(es_par_o_impar2(None))


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
    if es_enetro_o_flotante(base) and es_enetro_o_flotante(exponente):
        resultado = 1
        for i in range(exponente):
            resultado *= base
        return resultado 
    else:
        return "Alguno de los datos ingresados no es valido."

# print(potencia_del_numero(3,3))

# se puede hacer la potencia como numero ** exponente.


# 10) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def es_primo(numero):
    """
        Propósito: Indicar si el número es primo.
        Parametro:
            numero (int) : número al cual se evaluar si es primo o no.
        Return: retorna True si el número ingresado es primo, en caso contrario retorna False.
    """

    if isinstance(numero, int): 
        cantidad_de_divisores = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                cantidad_de_divisores += 1

        return cantidad_de_divisores == 2
    else:
        return "No ha ingresado un valor valido."

# print(es_primo(11))

# 11) Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

from primos import cantidad_de_primos_hasta, imprimir_primos_hasta
from validaciones import es_entero

def mostrar_todos_los_primos_hasta():
    """
    Propósito:
    
    """
    numero_ingresado = input("Por favor, ingrese un número entero: ")
    if es_entero(numero_ingresado):
        numero_ingresado = int(numero_ingresado)
        cantidad_de_primos_encontrados = cantidad_de_primos_hasta(numero_ingresado)
        imprimir_primos_hasta(numero_ingresado)

        return f"La cantidad de primos es: {cantidad_de_primos_encontrados}"
    else:
        return "El valor ingresado no es un número entero."

print(mostrar_todos_los_primos_hasta())


# 12) Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def tabla_de_mutiplicar_de(numero, inicio = 1, final = 10):
    """
    Propósito: imprimir la tabla de multiplicar del número dado.
    Parametros:
        numero (int): número en el que basará la tabla.
        inicio (int): número desde el que se iniciará la tabla del número dado.
        final (int): número en el que se terminará la tabla del número dado.
    """
    if es_entero(numero) and es_entero(inicio) and es_entero(final):
        numero_de_la_tabla = int(numero)
        numero_inicial = int(inicio)
        numero_final = int(final)
        for numero_actual in range(numero_inicial, numero_final + 1):
            resultado = numero_de_la_tabla * numero_actual
            print(f"{numero_de_la_tabla} x {numero_actual} = {resultado}")
    else:
        print("El valor ingresado no es un número entero.")

# tabla_de_mutiplicar_de(2)
# tabla_de_mutiplicar_de(2, 4, 8)
# tabla_de_mutiplicar_de(2, 4)

# Preguntar por los números 

# 13) Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.


def devolver_tipo_de_dato(valor, tipo_de_dato):
    """
    proposito: devuelve el dato ingresado por el usuario

    Parametro:
        valor (): valor a evaluar si cumple con el tipo de dato que se indique
        tipo_de_dato (): el tipo que se usará para evaluar el valor ingresado
    Returns:
        int: Devuelve el valor ingresado si es del tipo indicado.
    """
    if isinstance(valor, tipo_de_dato):
        return valor
    else:
        return "Lo que ha ingresado no corresponde con el tipo ingresado."


# print(devolver_tipo_de_dato("1", str))







def es_par_o_impar3(número):
    """
        Proposito: Indica si el número ingresado ese par o impar.
        Parametro:
            número (int): número a evaluar si es par o impar.
        Return: retorna True si le número ingresado es par y False en el caso contrario.
    """
    if es_entero(número):
        return int(número) % 2 == 0
    else:
        return "No ha ingresado un número entero."


# print(es_par_o_impar3(2))
# print(es_par_o_impar3(2.5))
# print(es_par_o_impar3("hola"))
# print(es_par_o_impar3("2"))
# print(es_par_o_impar3(True))
# print(es_par_o_impar3(None))

