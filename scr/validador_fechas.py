def es_bisiesto(anio):
    """ Verifica si un año es bisiesto """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_dias_mes(mes, anio):
    """ Retorna la cantidad de días de un mes en un año determinado """
    if mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 días
        return 31
    elif mes in [4, 6, 9, 11]:  # Meses con 30 días
        return 30
    elif mes == 2:  # Febrero
        return 29 if es_bisiesto(anio) else 28
    else:
        return -1  # Error (nunca debería ocurrir)

def validar_fecha(fecha):
    """ Valida si una fecha ingresada es correcta """
    try:
        partes = fecha.split("/")
        if len(partes) != 3:
            raise ValueError("Formato incorrecto. Use DD/MM/AAAA")

        dia, mes, anio = partes

        # Convertir a enteros
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        if mes < 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12")

        dias_en_mes = obtener_dias_mes(mes, anio)

        if dia < 1 or dia > dias_en_mes:
            raise ValueError(f"El día debe estar entre 1 y {dias_en_mes} para el mes {mes}")

        return True

    except ValueError as e:
        print(f"Error: {e}")
        return False

# Solicitar la fecha hasta que el usuario ingrese una válida
while True:
    fecha = input("Ingrese una fecha en formato DD/MM/AAAA: ")
    if validar_fecha(fecha):
        print("✅ Fecha válida")
        break
    else:
        print("❌ Fecha inválida. Inténtelo nuevamente.")
