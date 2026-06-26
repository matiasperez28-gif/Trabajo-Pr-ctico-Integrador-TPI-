Sistema de Gestión de Países
Trabajo Práctico Integrador – Programación I
Tecnicatura Universitaria en Programación a Distancia
Universidad Tecnológica Nacional (UTN)
Descripción
Sistema desarrollado en Python para la gestión de información geográfica y demográfica de distintos países.
La aplicación permite almacenar, consultar, modificar y analizar datos de países mediante una interfaz de consola simple e intuitiva.
Los datos se almacenan en memoria utilizando listas y diccionarios, mientras que la persistencia se realiza mediante archivos CSV.

Funcionalidades
Gestión de países
Agregar nuevos países
 Actualizar población y superficie
 Buscar países por nombre
Filtrar países por:
oContinente
oRango de población
oRango de superficie
Ordenar países por:
oNombre
oPoblación
oSuperficie
oAscendente o descendente
Estadísticas
País con mayor población
País con menor población
Promedio de población
Promedio de superficie
Cantidad de países por continente
Persistencia de datos
Lectura automática desde CSV al iniciar
Guardado automático al finalizar

Arquitectura del Proyecto
│
├──main.py
├──funciones_paises.py
├──archivos_csv.py
├──estadisticas.py
├──utilidades.py
├──paises.csv
├──README.md
└──GESTIONDEPAISES.pdf
 
Responsabilidades
main.py
Punto de entrada del sistema.
Carga datos desde CSV
Muestra el menú principal
Gestiona las opciones del usuario
Coordina las llamadas a los demás módulos
Guarda los datos al finalizar

funciones_paises.py
Contiene la lógica principal del sistema.
Funciones:
agregar_pais()
actualizar_pais()
buscar_pais()
filtrar_paises()
ordenar_paises()
mostrar_tabla_paises()

archivos_csv.py
Gestiona la persistencia de datos.
Funciones:
cargar_datos_desde_csv()
guardar_datos_en_csv()
estadisticas.py
Calcula indicadores estadísticos.
Función:
mostrar_estadisticas()

utilidades.py
Funciones auxiliares reutilizables.
Función:
solicitar_entero_valido()

paises.csv
Archivo utilizado para almacenar permanentemente la información.

Flujo General del Sistema
Inicio
  │
  ▼
CargarCSV
  │
  ▼
Mostrarmenú
  │
  ▼
Seleccionaropción
  │
  ▼
Ejecutarfunción
  │
  ▼
Volveralmenú
  │
  └───────────────┐
                  │
                  ▼
                Salir
                  │
                  ▼
             GuardarCSV
                  │
                  ▼
                 Fin
 

Estructura de Datos
Cada país se almacena como un diccionario:
{
    "nombre": "Argentina",
    "poblacion": 47000000,
    "superficie": 2780400,
    "continente": "America"
}
 
Todos los países se almacenan dentro de una lista:
lista_paises = [
    {
        "nombre": "Argentina",
        "poblacion": 47000000,
        "superficie": 2780400,
        "continente": "America"
    }
]
 

Validaciones Implementadas
Datos numéricos
No permite letras
No permite símbolos inválidos
No permite campos vacíos
No permite números negativos
Alta de países
Nombre obligatorio
Continente obligatorio
Prevención de países duplicados
Búsquedas
Control de sistema vacío
Mensajes cuando no existen coincidencias
Filtros
Validación de opciones
Verificación de rangos válidos
Ordenamientos
Validación de criterio
Validación de sentido de ordenamiento
Archivos CSV
Verificación de existencia del archivo
Validación de formato de datos
Manejo de errores de lectura y escritura

Tecnologías Utilizadas
Python 3
Módulo csv
Listas
Diccionarios
Funciones
Estructuras condicionales
Bucles

Conceptos Aplicados
Modularización
Manejo de archivos CSV
Validación de datos
Búsquedas
Filtros
Ordenamientos
Estadísticas básicas
Persistencia de información
Arquitectura modular
Ejecución
1.Clonar el repositorio: git clone https://github.com/matiasperez28-gif/Trabajo-Pr-ctico-Integrador-TPI-.git 
2. Ejecutar:
python main.py
 

Autor
Matias A. Perez Romo
Trabajo Práctico Integrador
Programación I
Tecnicatura Universitaria en Programación a Distancia
Universidad Tecnológica Nacional (UTN)

Documentación
El repositorio incluye el documento completo:
GESTION DE PAISES.pdf

donde se detallan:
Diseño del sistema
Arquitectura modular
Diagramas de flujo
Validaciones
Casos de prueba
Conclusiones

Proyecto desarrollado con fines académicos para la materia Programación I - UTN.
Acceso al video
https://drive.google.com/file/d/1BekEsudiRXz3W5GmgV4jKCbBIyDfNFd4/view?usp=drive_link
https://youtu.be/kaF0s6hQzAU

