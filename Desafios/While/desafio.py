"""
📌 Desafío: Encuesta Tecnológica en UTN Technologies
UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.
Las tecnologías en evaluación son:
 🔹 Inteligencia Artificial (IA)
 🔹 Realidad Virtual/Aumentada (RV/RA)
 🔹 Internet de las Cosas (IOT)
Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
🔹 Recolección de Datos
Cada empleado encuestado deberá proporcionar la siguiente información:
 ✔️ Nombre
 ✔️ Edad (debe ser 18 años o más)
 ✔️ Género (Masculino, Femenino, Otro)
 ✔️ Tecnología elegida (IA, RV/RA, IOT)
El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
🔹 Análisis de Datos
A partir de las respuestas, se deben calcular las siguientes métricas:
1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
Su género no sea Femenino 
Su edad está entre los 33 y 40 años.
3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


🔹 Requisitos del Programa
 ✔️ Los datos deben solicitarse y validarse correctamente.
 ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
 ✔️ Presentar los resultados de manera clara y organizada.
"""

cantidad_de_empleados_a_ingresar = 10

cantidad_de_empleados_masculinos = 0
canitdad_de_empleados_otros = 0
cantidad_de_votos_IOT_o_IA = 0
cantidad_que_no_voto_por_IA = 0
edad_del_empleado_mas_grande_actual = 0

while cantidad_de_empleados_a_ingresar != 0:
    nombre_empleado = input("Ingrese su nombre: ")
    edad_empleado = int(input("Ingrese su edad: "))
    genero_empleado = input("Ingrese su genero (Masculino, Femenino, Otro): ").lower()
    tecnología_elegida = input("Ingrese la tecnología que desea elegir (IA, RV/RA, IOT): ").upper()

    edad_es_valida = edad_empleado >= 18
    genero_es_valido = genero_empleado == "masculino" or genero_empleado == "femenino" or genero_empleado == "otro"
    tecnologia_es_valida = tecnología_elegida == "IA" or tecnología_elegida == "RV" or tecnología_elegida == "RA" or tecnología_elegida == "IOT"

    while not edad_es_valida or not genero_es_valido or not tecnologia_es_valida :
        if not edad_es_valida:
            edad_empleado = int(input("Ingrese su edad: "))
            edad_es_valida = edad_empleado >= 18
        elif not genero_es_valido:
            genero_empleado = input("Ingrese su genero (Masculino, Femenino, Otro): ").lower()
            genero_es_valido = genero_empleado == "masculino" or genero_empleado == "femenino" or genero_empleado == "otro"
        else:
            tecnología_elegida = input("Ingrese la tecnología que desea elegir (IA, RV/RA, IOT): ").upper()
            tecnologia_es_valida = tecnología_elegida == "IA" or tecnología_elegida == "RV" or tecnología_elegida == "RA" or tecnología_elegida == "IOT"
    
    if (genero_empleado == "masculino") and (edad_empleado > edad_del_empleado_mas_grande_actual):
        edad_del_empleado_mas_grande_actual = edad_empleado
        empleado_de_mayor_edad_y_su_tecnologia = f"El empleado con mayor edad es {nombre_empleado} y la tecnología por la que votó es {tecnología_elegida}"

    if genero_empleado == "masculino":
        cantidad_de_empleados_masculinos += 1
        if (tecnología_elegida == "IA" or tecnología_elegida == "IOT") and (25 <= edad_empleado <= 50):
            cantidad_de_votos_IOT_o_IA += 1
    elif genero_empleado == "otro":
        canitdad_de_empleados_otros += 1

    if not (tecnología_elegida == "IA") and (33 < edad_empleado < 40) and (genero_empleado != "femenino"):
            cantidad_que_no_voto_por_IA += 1

    cantidad_de_empleados_a_ingresar -= 1

    

porcentaje_de_empleados_que_no_votaron_por_IA = cantidad_que_no_voto_por_IA * 100 / (cantidad_de_empleados_masculinos + canitdad_de_empleados_otros)


print(f"Son {cantidad_de_votos_IOT_o_IA} los empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive)")
print(f"El porcentaje de empleados que NO votaron por IA es del {porcentaje_de_empleados_que_no_votaron_por_IA}%")
print(empleado_de_mayor_edad_y_su_tecnologia)