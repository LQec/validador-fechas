import os
from datetime import datetime


def validar_fecha(entrada):
    """Valida que una fecha tenga el formato correcto (dd/mm/yyyy) y exista."""
    try:
        fecha_valida = datetime.strptime(entrada, "%d/%m/%Y")
        return fecha_valida.strftime("%d/%m/%Y")  # Retorna la fecha bien formateada
    except ValueError:
        return None  # Indica que la fecha no es válida


def solicitar_fecha():
    """Solicita al usuario ingresar una fecha válida."""
    while True:
        fecha = input("Ingrese una fecha (dd/mm/yyyy): ").strip()
        fecha_validada = validar_fecha(fecha)

        if fecha_validada:
            print(f"✅ Fecha válida: {fecha_validada}")
            return fecha_validada
        else:
            print("❌ Error: Fecha inválida. Intente nuevamente.")


def guardar_fecha_en_archivo(fecha, archivo="fechas_validas.txt"):
    """Guarda la fecha validada en un archivo de texto."""
    try:
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"{fecha}\n")
        print(f"✅ Fecha guardada en {archivo}")
    except Exception as e:
        print(f"❌ Error al guardar la fecha: {e}")


def main():
    print("📅 Validador de Fechas")
    fecha = solicitar_fecha()
    guardar_fecha_en_archivo(fecha)


if __name__ == "__main__":
    main()
