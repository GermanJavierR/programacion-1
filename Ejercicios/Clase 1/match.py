estación_del_año = input("Ingrese la estación del año en la que desee viajar: ")
destino_del_viaje = input("Ingrese el destino al que desee viajar: ").lower()

match estación_del_año.lower():
    case "invierno":
        if destino_del_viaje == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if destino_del_viaje == "mar del plata" or destino_del_viaje == "catamarca":
            print("Se viaja")
        else:
            print("No se viaja")
    case "otoño":
        print("Se viaja")
    case "primavera":
        if destino_del_viaje == "bariloche":
            print("No se viaja")
        else:
            print("Se viaja")
