class FechaInvalidaError(Exception):
    """Excepción personalizada para fechas inválidas"""
    pass

def es_bisiesto(anio):
    """Verifica si un año es bisiesto"""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_dias_mes(mes, anio):
    """Devuelve el número de días en un mes considerando los años bisiestos"""
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif mes in {4, 6, 9, 11}:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    else:
        raise FechaInvalidaError("Mes inválido. Debe estar entre 1 y 12.")

def validar_fecha(fecha):
    """Verifica si la fecha ingresada es válida"""
    try:
        partes = fecha.split("/")
        if len(partes) != 3:
            raise FechaInvalidaError("Formato incorrecto. Use DD/MM/AAAA.")

        dia, mes, anio = map(int, partes)

        if anio < 1:
            raise FechaInvalidaError("El año debe ser mayor a 0.")

        dias_maximos = obtener_dias_mes(mes, anio)

        if not (1 <= dia <= dias_maximos):
            raise FechaInvalidaError(f"Día inválido para el mes {mes}. Debe estar entre 1 y {dias_maximos}.")

        print("Fecha válida:", fecha)

    except ValueError:
        print("Error: Ingrese solo números en el formato DD/MM/AAAA.")
    except FechaInvalidaError as e:
        print(f"Error: {e}")

# Solicitar fecha al usuario con validación
while True:
    try:
        fecha_usuario = input("Ingrese una fecha en formato DD/MM/AAAA: ")
        validar_fecha(fecha_usuario)
        break  # Salir del bucle si la fecha es válida
    except Exception as e:
        print("Error inesperado:", e)
