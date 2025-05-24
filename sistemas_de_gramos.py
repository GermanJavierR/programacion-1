"""
Una empresa se dedica al almacenamiento y posterior distribución de cereales en el interior del país. Para ello cuentan con 20 depósitos en CABA, que generalmente se encuentran en las inmediaciones de las estaciones del ferrocarril. 
Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo, cebada y centeno. 
La oficina central, recibe mensualmente una planilla de existencias donde se indican las existencias de cada cereal para cada depósito. 
Realizar un menú de opciones: while - match case
1. Obtener existencias: para ello deberá crear una función que cargue la existencia de cada grano(input) en todos los depósitos. Los valores estarán comprendidos entre 5000 Kg y 20000 Kg. (validar, que sea número) deposito_1 =  depositos[0] = 500
2. Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales. 
3. Nombre del cereal que almaceno menos kilos en cada depósito. 
4. Máxima cantidad de kilos almacenados de cada cereal. 
5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector con los valores por kilo de cada tipo de cereal. 
6. Cantidad de depósitos que hayan almacenado más de 50000 kilos entre los 4 cereales. 
7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados. Además mostrar el nombre del cereal con el máximo porcentaje. 
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.
"""

from Modulos.validaciones import es_entero, es_float, es_un_numero_negativo

filas = 5
columnas = 20

# Inicializo la matriz que contendra los depositos y las cantidades de sus cereales.
matriz_de_deposito = [[0 for c in range(columnas)] for f in range(filas)]

# Cambie el valor de la primera lista para que sean los depositos.
for i in range(len(matriz_de_deposito[0])):
    matriz_de_deposito[0][i] = f"Dpst {i + 1}"


# Muestro la matris por la consola.
for i in range(len(matriz_de_deposito)):
    for j in range(len(matriz_de_deposito[i])):
        print(matriz_de_deposito[i][j], end=" ")
    print("")


# print(matriz_de_deposito[0][2])

def obtener_existencia():
    """
    Propósito: carga la existencia de cada grano en todos los depositos.
    Return: retorna la matriz de los depositos con los valores de los cereales actualizados.
    """
    for i in range(1, len(matriz_de_deposito)):
        for j in range(len(matriz_de_deposito[i])):
            if i == 1:
                grano_actual = "maiz"
            elif i == 2:
                grano_actual = "trigo"
            elif i == 3:
                grano_actual = "cebada"
            else:
                grano_actual = "centeno"

            seguir_intentado = "Si"
            while seguir_intentado != "No":
                cantidad_del_grano = input(f"Por favor, ingrese la cantidad de {grano_actual} existente para el deposito {j + 1}, la canitdad debe ser entre 5000 kg y 20000 kg: ")
                if es_entero(cantidad_del_grano) or es_float(cantidad_del_grano) or es_un_numero_negativo(cantidad_del_grano):
                    cantidad_del_grano = int(cantidad_del_grano)
                    if 5000 < cantidad_del_grano < 20000:
                    # if es_un_numero_negativo(cantidad_del_grano) and (cantidad_del_grano <= matriz_de_deposito[i][j]):
                    #     matriz_de_deposito[i][j] -= cantidad_del_grano
                        matriz_de_deposito[i][j] += cantidad_del_grano
                        seguir_intentado = "No"
                    else:
                        print("El número ingresado no está dentro de los valores comprendidos.")
                    
                else:
                    print("El valor ingresado no es valido, por favor vuelva a intentar.")


obtener_existencia()


for i in range(len(matriz_de_deposito)):
    for j in range(len(matriz_de_deposito[i])):
        print(matriz_de_deposito[i][j], end=" ")
    print("")



def cantidad_total_de_kilos_de_los_depositos():
    """"""

# print(matriz_de_deposito)


