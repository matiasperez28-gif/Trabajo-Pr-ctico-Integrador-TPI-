def mostrar_estadisticas(lista_paises):
    """
    Calcula y muestra los indicadores estadísticos solicitados:
    máximos, mínimos, promedios y conteos por continente.
    """
    print("\n--- ESTADÍSTICAS DEL SYSTEMA ---")
    
    if not lista_paises:
        print("El sistema está vacío. No hay datos para calcular estadísticas.")
        return

    # --- 1. INICIALIZACIÓN DE VARIABLES ---
    pais_mayor_pob = lista_paises[0]
    pais_menor_pob = lista_paises[0]
    
    suma_poblacion = 0
    suma_superficie = 0
    
    # Diccionario para contar países por continente
    conteo_continentes = {}

    # --- 2. RECORRIDO DE LA LISTA (UN SOLO BUCLE PARA OPTIMIZAR) ---
    for pais in lista_paises:
        pob_actual = pais["poblacion"]
        sup_actual = pais["superficie"]
        cont_actual = pais["continente"]
        
        # Acumuladores para los promedios
        suma_poblacion += pob_actual
        suma_superficie += sup_actual
        
        # Buscar Mayor Población
        if pob_actual > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = pais
            
        # Buscar Menor Población
        if pob_actual < pais_menor_pob["poblacion"]:
            pais_menor_pob = pais
            
        # Conteo por Continente (Diccionario de frecuencias)
        if cont_actual in conteo_continentes:
            conteo_continentes[cont_actual] += 1
        else:
            conteo_continentes[cont_actual] = 1

    # --- 3. CÁLCULO DE PROMEDIOS ---
    total_paises = len(lista_paises)
    promedio_pob = suma_poblacion / total_paises
    promedio_sup = suma_superficie / total_paises

    # --- 4. MOSTRAR RESULTADOS ---
    print(f"Total de países registrados: {total_paises}")
    print("-" * 50)
    
    # Mayor y menor población
    print(f"País con MAYOR población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,} hab.)")
    print(f"País con MENOR población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,} hab.)")
    print("-" * 50)
    
    # Promedios (formateados con 2 decimales)
    print(f"Promedio de población general: {promedio_pob:,.2f} habitantes")
    print(f"Promedio de superficie general: {promedio_sup:,.2f} km²")
    print("-" * 50)
    
    # Cantidad por continente
    print("Cantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f" -> {continente}: {cantidad}")
    print("-" * 50)