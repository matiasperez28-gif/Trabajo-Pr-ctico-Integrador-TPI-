from utilidades import solicitar_entero_valido

def agregar_pais(lista_paises):
    """
    Solicita los datos de un nuevo país, valida que no estén vacíos 
    y lo agrega a la lista en memoria.
    """
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    # 1. Validar Nombre
    while True:
        try:
            nombre = input("Ingrese el nombre del país: ").strip().capitalize()
            if not nombre:
                print("Error: El nombre no puede estar vacío.")
            else:
            # Opcional: Validar que no exista ya en la lista
                existe = False
                for p in lista_paises:
                    if p["nombre"] == nombre:
                        existe = True
                        break
                if existe:
                    print("Error: Este país ya se encuentra registrado.")
                else:
                    break
        except ValueError as ev:
             print (f"Error debe ingresar un nombre correcto: {ev} ") 

    # 2. Validar Población y Superficie usando nuestra función auxiliar
    poblacion = solicitar_entero_valido("Ingrese la cantidad de población: ")
    superficie = solicitar_entero_valido("Ingrese la superficie en km2: ")

    # 3. Validar Continente
    while True:
        continente = input("Ingrese el continente: ").strip().capitalize()
        if not continente:
            print("Error: El continente no puede estar vacío.")
        else:
            break

    # 4. Crear el diccionario y añadirlo a la lista general
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    lista_paises.append(nuevo_pais)
    print(f"\n¡Éxito! El país '{nombre}' ha sido agregado correctamente a la lista.")


def actualizar_pais(lista_paises):
    
     """ Busca un país por su nombre exacto y, si lo encuentra,
     permite actualizar sus campos de Población y Superficie.
     """
     print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    
     if not lista_paises: 
        print("El sistema está vacío. No hay países para actualizar.")
        return

     nombre_buscar = input("Ingrese el nombre del país que desea modificar: ").strip().capitalize()
    
    # Buscamos el país en la lista (ignorando mayúsculas/minúsculas)
     pais_encontrado = None
     for pais in lista_paises:
        if pais["nombre"] == nombre_buscar :
            pais_encontrado = pais
            break # Si lo encontramos, salimos del bucle
    
    # Validamos si la búsqueda no arrojó resultados
     if pais_encontrado is None:
        print(f"Error: No se encontró ningún país con el nombre '{nombre_buscar}'.")
        return

    # Si lo encontró, mostramos los datos actuales
     print(f"\nPaís encontrado: {pais_encontrado['nombre']}")
     print(f"-> Población actual: {pais_encontrado['poblacion']}")
     print(f"-> Superficie actual: {pais_encontrado['superficie']} km2")
     print("-" * 35)
    
    # Solicitamos los nuevos datos usando la función de validación que ya teníamos
     print("Ingrese los nuevos datos:")
     nueva_poblacion = solicitar_entero_valido("Nueva población: ")
     nueva_superficie = solicitar_entero_valido("Nueva superficie (km2): ")
    
    # Actualizamos el diccionario dentro de la lista
     pais_encontrado["poblacion"] = nueva_poblacion
     pais_encontrado["superficie"] = nueva_superficie
    
     print(f"\n¡Éxito! Los datos de '{pais_encontrado['nombre']}' se actualizaron correctamente.")


def buscar_pais(lista_paises):
    """
    Busca países cuyo nombre coincida de forma parcial o exacta
    con el término ingresado por el usuario.
    """
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    
    if not lista_paises:
        print("El sistema está vacío. No hay países para buscar.")
        return

    termino_buscar = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().capitalize()
    
    if not termino_buscar:
        print("Error: El término de búsqueda no puede estar vacío.")
        return

    # Lista auxiliar para guardar todos los países que coincidan
    resultados = []
    
    for pais in lista_paises:
        # El operador 'in' permite la coincidencia parcial
        if termino_buscar in pais["nombre"]:
            resultados.append(pais)
            
    # Validamos si la búsqueda no arrojó resultados
    if not resultados:
        print(f"\nNo se encontraron países que coincidan con '{termino_buscar}'.")
        return

    # Si encontramos coincidencias, las mostramos en un formato prolijo
    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    print("-" * 60)
    # Formateo de columnas usando f-strings
    print(f"{'Nombre':<15} | {'Población':<12} | {'Superficie (km2)':<15} | {'Continente':<15}")
    print("-" * 60)
    
    for pais in resultados:
        print(f"{pais['nombre']:<15} | {pais['poblacion']:<12} | {pais['superficie']:<15} | {pais['continente']:<15}")
    print("-" * 60)

def filtrar_paises(lista_paises):
    """
    Despliega un submenú para filtrar los países por continente, 
    rango de población o rango de superficie.
    """
    if not lista_paises:
        print("\nEl sistema está vacío. No hay países para filtrar.")
        return

    print("\n--- MENÚ DE FILTRADOS ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    print("4. Volver al menú principal")
    #AQUI TENGO QUE VALIDAR 
    opcion = input("Seleccione una opción de filtrado (1-4): ").strip()
    
    resultados = []

    # --- OPCIÓN 1: FILTRAR POR CONTINENTE ---
    if opcion == "1":
        continente_buscar = input("Ingrese el nombre del continente: ").strip().capitalize()
        for pais in lista_paises:
            if pais["continente"] == continente_buscar:
                resultados.append(pais)
                
    # --- OPCIÓN 2: FILTRAR POR RANGO DE POBLACIÓN ---
    elif opcion == "2":
        print("\nDefina el rango de población:")
        minimo = solicitar_entero_valido("Ingrese el valor MÍNIMO de población: ")
        maximo = solicitar_entero_valido("Ingrese el valor MÁXIMO de población: ")
        
        if minimo > maximo:
            print("Error: El mínimo no puede ser mayor que el máximo.")
            return
            
        for pais in lista_paises:
            if minimo <= pais["poblacion"] <= maximo:
                resultados.append(pais)

    # --- OPCIÓN 3: FILTRAR POR RANGO DE SUPERFICIE ---
    elif opcion == "3":
        print("\nDefina el rango de superficie (km2):")
        minimo = solicitar_entero_valido("Ingrese la superficie MÍNIMA: ")
        maximo = solicitar_entero_valido("Ingrese la superficie MÁXIMA: ")
        
        if minimo > maximo:
            print("Error: El mínimo no puede ser mayor que el máximo.")
            return
            
        for pais in lista_paises:
            if minimo <= pais["superficie"] <= maximo:
                resultados.append(pais)

    # --- OPCIÓN 4: VOLVER ---
    elif opcion == "4":
        return
    else:
        print("Error: Opción de filtrado inválida.")
        return

    # --- MOSTRAR RESULTADOS DEL FILTRO ---
    if not resultados:
        print("\nNo se encontraron países que cumplan con los criterios del filtro.") 
    else:
        print(f"\nSe encontraron {len(resultados)} país(es) que coinciden:")
        mostrar_tabla_paises(resultados)



def obtener_nombre(pais):
    return pais["nombre"].lower()


def obtener_poblacion(pais):
    return pais["poblacion"]


def obtener_superficie(pais):
    return pais["superficie"]


def ordenar_paises(lista_paises):
    """
    Ordena la lista de países por Nombre, Población o Superficie
    utilizando los métodos sort() y reverse().
    """
    if not lista_paises:
        print("\nEl sistema está vacío. No hay países para ordenar.")
        return

    print("\n--- MENÚ DE ORDENAMIENTOS ---")
    print("1. Ordenar por Nombre")
    print("2. Ordenar por Población")
    print("3. Ordenar por Superficie")

    try:
        opcion_criterio = int(input("Seleccione el criterio (1-3): "))
    except ValueError:
        print("Error: Debe ingresar un número.")
        return

    if opcion_criterio == 1:
        criterio = "nombre"
    elif opcion_criterio == 2:
        criterio = "poblacion"
    elif opcion_criterio == 3:
        criterio = "superficie"
    else:
        print("Error: Opción inválida.")
        return

    print("\n¿En qué sentido desea ordenar?")
    print("1. Ascendente (Menor a Mayor / A-Z)")
    print("2. Descendente (Mayor a Menor / Z-A)")

    try:
        opcion_sentido = int(input("Seleccione el sentido (1-2): "))
    except ValueError:
        print("Error: Debe ingresar un número.")
        return

    if opcion_sentido != 1 and opcion_sentido != 2:
        print("Error: Opción inválida.")
        return

    # Crear una copia de la lista para no modificar la original
    lista_ordenada = list(lista_paises)

    # Ordenar según el criterio elegido
    if criterio == "nombre":
        lista_ordenada.sort(key=obtener_nombre)
    elif criterio == "poblacion":
        lista_ordenada.sort(key=obtener_poblacion)
    elif criterio == "superficie":
        lista_ordenada.sort(key=obtener_superficie)

    # Si el usuario eligió descendente, invertir el orden
    if opcion_sentido == 2:
        lista_ordenada.reverse()

    print("\n¡Lista ordenada con éxito!")
    mostrar_tabla_paises(lista_ordenada)
    
def mostrar_tabla_paises(lista):
    """Función auxiliar para mostrar los países en un formato lindo de tabla."""
    print("-" * 65)
    print(f"{'Nombre':<15} | {'Población':<12} | {'Superficie (km2)':<16} | {'Continente':<15}")
    print("-" * 65)
    for pais in lista:
        print(f"{pais['nombre']:<15} | {pais['poblacion']:<12} | {pais['superficie']:<16} | {pais['continente']:<15}")
    print("-" * 65)

