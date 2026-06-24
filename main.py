from archivos_csv import cargar_datos_desde_csv
from archivos_csv import guardar_datos_en_csv

from funciones_paises import agregar_pais
from funciones_paises import actualizar_pais
from funciones_paises import buscar_pais
from funciones_paises import filtrar_paises
from funciones_paises import ordenar_paises

from estadisticas import mostrar_estadisticas
def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\n" + "="*40)
    print("  SISTEMA DE GESTIÓN DE PAÍSES  ")
    print("="*40)
    print(f"1. Agregar un país\n2. Actualizar población y superficie\n3. Buscar un país por nombre\n4. Filtrar países")
    print(f"5. Ordenar países\n6. Mostrar estadísticas\n7. Salir")
    print("="*40)


def main():
    # 1. Cargamos los datos al iniciar (Función del paso anterior)
    paises = cargar_datos_desde_csv()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("\nGuardando cambios antes de salir...")
            guardar_datos_en_csv(paises) # <--- Aquí llamamos a la función
            print("¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            # Validación de entrada errónea solicitada por la cátedra
            print("\nError: Opción inválida. Por favor, ingrese un número del 1 al 7.")


if __name__ == "__main__":
    main()

print ()