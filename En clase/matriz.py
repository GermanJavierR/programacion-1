matrix = [
    [2,4,5,6],
    [6,3,1,9]
]


# Manera correcta de mostrar los datos de una matriz.
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print("")

# Otra manera de mostrarlo.
for fila in matrix:
    print(fila)


# Mostrar elemento de una matriz.
print(matrix[1][0])

print(matrix[1][1])


# Modificación de un elemento de una matriz.
matrix[1][0] = 15

print(matrix[1][0])



# Formas de crear una matriz.
filas = 3
columnas = 4
matriz = [[0 for c in range(columnas)] for f in range(filas)]

print(matriz)


# Carga secuencial.
# for i in range(filas):
#     for j in range(columnas):
#         matriz[i][j] = int(input(f"Ingrese valor en fila {i}, columna {j}: "))


# Carga aleatoria.
def cargar_matriz_aleatoriamente(matriz:list):
    seguir = "S"
    while seguir == "S":
        filas = int(input("Cuantas filas desea ingresar?: "))
        columnas = int(input("Cuantas columnas desea ingresar?: "))
        fila = int(input("Indice de fila: "))
        columna = int(input("Indice de columna: "))

        # Inicializar la matriz con ceros
        for i in range(filas):
            matriz.append([0] * columnas)
        
        print(matriz)

        dato = int(input("Ingrese el número a cargar: "))
        matriz[fila - 1][columna - 1] = dato # más intuitivo para el usuario.
        seguir = input("Desea seguir cargando? S/N: ")

mi_matriz = []
cargar_matriz_aleatoriamente(mi_matriz)

for i in mi_matriz:
    print(i)