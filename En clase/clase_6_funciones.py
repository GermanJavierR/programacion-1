#Ejercicios propuestos en le video.

def chau_nombre(nombre):
    print("Chau,", nombre)

chau_nombre("Germán")


def multiplicar(a, b):
    resultado = a * b
    return resultado

multiplicación = multiplicar(3, 5)
print(f"La multiplicación es: {multiplicación}")


def saludar(nombre = "invitado"): # parametro opcional.
    print("Hola", nombre)


def sumar(a: int, b: int) -> int:
    return int(a + b)

# print(sumar("2", "3")) # Lo convierte a un int

# print(sumar(1.5, 2.5)) # Retorna el entero 4

# print(sumar(1.3, 2.5)) # Retorna la parte entera no más de la suma de los flotantes.

# print(sumar("12.5", "45.3")) # Explota porque no puede convertir int la concatenación de los str de números con coma.

# print(sumar("12.5", 5)) # Sigue sin poder concatenar un str con un int y convertirlo.




def dividir(a: int, b: int) -> int:
    return a / b

# resultado = dividir(3, 5) # Se hace esto para que no peder el dato y quede guardado.

# print(resultado)

# print(dividir(3, "hola")) # Explota

# print(dividir("hola", 2)) # No se puede dividir un str por un int

# print(type(dividir(4, 2))) # Diviendo dos enteros me retorna un float.  



# Valores mutables e inmutables.

lista1 = [1, 2, 3]
lista2 = lista1
lista2[0] = 99

print("lista 1:", lista1) # El primer elemento de la lista también cambia.
print("lista 2:", lista2) # El primer elemento de la lista cambia por el dado.