# 🌍 Sistema de Gestión de Países

**Trabajo Práctico Integrador – Programación I**  
**Tecnicatura Universitaria en Programación a Distancia**  
**Universidad Tecnológica Nacional (UTN)**

---

## 📖 Descripción

Sistema desarrollado en **Python** para administrar información geográfica y demográfica de distintos países.

La aplicación permite agregar, consultar, actualizar, ordenar, filtrar y obtener estadísticas sobre los países almacenados, utilizando una interfaz de consola.

Los datos se mantienen en memoria mediante listas de diccionarios y se almacenan de forma permanente en un archivo CSV.

---

# ✨ Funcionalidades

## Gestión de países

- Agregar países.
- Actualizar población.
- Actualizar superficie.
- Buscar países por nombre.
- Mostrar todos los países.
- Filtrar por continente.
- Filtrar por rango de población.
- Filtrar por rango de superficie.
- Ordenar por:
  - Nombre
  - Población
  - Superficie
- Orden ascendente o descendente.

---

## 📊 Estadísticas

El sistema permite obtener:

- País con mayor población.
- País con menor población.
- Promedio de población.
- Promedio de superficie.
- Cantidad de países por continente.

---

## 💾 Persistencia de datos

La información se almacena automáticamente en un archivo CSV.

Al iniciar el programa:

- Se leen los datos desde **paises.csv**.

Al finalizar:

- Se guardan automáticamente los cambios realizados.

---

# 📂 Estructura del proyecto

```
Proyecto
│
├── main.py
├── funciones_paises.py
├── archivos_csv.py
├── estadisticas.py
├── utilidades.py
├── paises.csv
├── README.md
└── GESTION_DE_PAISES.pdf
```

---

# 📄 Descripción de los módulos

## main.py

Controla todo el programa.

- Muestra el menú principal.
- Carga los datos.
- Llama a las funciones correspondientes.
- Guarda la información al finalizar.

---

## funciones_paises.py

Contiene las funciones principales del sistema.

- agregar_pais()
- actualizar_pais()
- buscar_pais()
- filtrar_paises()
- ordenar_paises()
- mostrar_tabla_paises()

---

## archivos_csv.py

Gestiona la lectura y escritura del archivo CSV.

Funciones:

- cargar_datos_desde_csv()
- guardar_datos_en_csv()

---

## estadisticas.py

Calcula estadísticas sobre los países.

Función principal:

- mostrar_estadisticas()

---

## utilidades.py

Contiene funciones auxiliares.

- solicitar_entero_valido()

---

# 🗂 Estructura de los datos

Cada país se almacena como un diccionario.

```python
{
    "nombre": "Argentina",
    "poblacion": 47000000,
    "superficie": 2780400,
    "continente": "América"
}
```

Todos los países se almacenan dentro de una lista.

```python
lista_paises = [
    {
        "nombre": "Argentina",
        "poblacion": 47000000,
        "superficie": 2780400,
        "continente": "América"
    }
]
```

---

# ✔ Validaciones implementadas

## Datos numéricos

- No admite letras.
- No admite símbolos.
- No admite valores vacíos.
- No admite números negativos.

## Alta de países

- Nombre obligatorio.
- Continente obligatorio.
- Evita países duplicados.

## Búsquedas

- Verifica que existan datos.
- Informa cuando no encuentra coincidencias.

## Filtros

- Valida opciones ingresadas.
- Verifica rangos correctos.

## Ordenamientos

- Valida el criterio elegido.
- Valida el tipo de orden.

## Archivos CSV

- Comprueba la existencia del archivo.
- Maneja errores de lectura.
- Maneja errores de escritura.

---

# 🛠 Tecnologías utilizadas

- Python 3
- Módulo csv
- Listas
- Diccionarios
- Funciones
- Condicionales
- Bucles
- Bubble Sort

---

# 📚 Conceptos aplicados

- Modularización.
- Manejo de archivos CSV.
- Persistencia de datos.
- Validación de entradas.
- Búsquedas.
- Filtros.
- Ordenamientos.
- Estadísticas.
- Arquitectura modular.

---

# ▶ Ejecución

1. Clonar el repositorio.

```bash
git clone https://github.com/matiasperez28-gif/Trabajo-Pr-ctico-Integrador-TPI-.git
```

2. Ingresar al proyecto.

```bash
cd Trabajo-Pr-ctico-Integrador-TPI-
```

3. Ejecutar el programa.

```bash
python main.py
```

---

# 👨‍💻 Autor

**Matías A. Pérez Romo**

Trabajo Práctico Integrador

Programación I

Tecnicatura Universitaria en Programación a Distancia

Universidad Tecnológica Nacional (UTN)

---

# 📄 Documentación

El proyecto incluye el documento:

**GESTION_DE_PAISES.pdf**

En él se desarrollan:

- Introducción.
- Objetivos.
- Arquitectura.
- Diagramas de flujo.
- Explicación del código.
- Validaciones.
- Casos de prueba.
- Conclusiones.

---

## 📌 Licencia

Proyecto desarrollado exclusivamente con fines académicos para la materia **Programación I** de la **Universidad Tecnológica Nacional (UTN)**.
---

# 🎥 Video demostrativo

Se puede ver el funcionamiento completo del sistema en los siguientes enlaces:

- 📺 **YouTube:** https://youtu.be/kaF0s6hQzAU
- 📁 **Google Drive:** https://drive.google.com/file/d/1BekEsudiRXz3W5GmgV4jKCbBIyDfNFd4/view?usp=drive_link

En el video se muestra:

- Ejecución del programa.
- Gestión de países.
- Búsquedas y filtros.
- Ordenamientos.
- Estadísticas.
- Persistencia de datos mediante archivos CSV.
