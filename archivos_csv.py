import csv
import os

def cargar_datos_desde_csv(nombre_archivo="paises.csv"):
    """
    Lee el archivo CSV y retorna una lista de diccionarios con los países.
    Maneja errores si el archivo no existe .
    """
    lista_paises = []
    
    # Validación: Verificamos si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no existe. Se iniciará con el sistema vacío.")
        return lista_paises

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            # Usamos DictReader para que asocie automáticamente los encabezados con los valores
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                try:
                    # Limpiamos espacios en blanco y convertimos los tipos de datos
                    pais = {
                        "nombre": fila["nombre"].strip().capitalize(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip().capitalize()
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError):
                    # Control de errores de formato en filas específicas
                    print("Advertencia: Se omitió una fila del CSV por error de formato o datos faltantes.")
                    
        print(f"Éxito: Se cargaron {len(lista_paises)} países correctamente.")
    except Exception as e:
        print(f"Error crítico al leer el archivo: {e}")
        
    return lista_paises


def guardar_datos_en_csv(lista_paises, nombre_archivo="paises.csv"):


    """
    Toma la lista de países actual en memoria y la escribe en el archivo CSV,
    sobreescribiendo el contenido anterior con los datos actualizados.
    """
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            # Definimos los encabezados obligatorios tal cual el formato original
            campos = ["nombre", "poblacion", "superficie", "continente"]
            
            lector = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribimos la cabecera (nombre, poblacion, superficie, continente)
            lector.writeheader()
            
            # Escribimos todas las filas de nuestra lista
            lector.writerows(lista_paises)
            
        print(f"\n¡Éxito! Los datos se guardaron correctamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"\nError crítico al intentar guardar los datos en el archivo: {e}")


