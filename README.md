# Proyectos de Streamlit - Cursos Santander

Este repositorio contiene dos aplicaciones web creadas con Streamlit para análisis de datos. Estas aplicaciones te permiten visualizar y explorar datos de manera interactiva sin necesidad de conocimientos avanzados de programación.

## Requisitos Previos

Antes de ejecutar estas aplicaciones, necesitas tener instalado Python en tu computadora. Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Pasos para Instalar Python (si no lo tienes):
1. Ve a [python.org](https://www.python.org/downloads/).
2. Descarga la versión más reciente para Windows.
3. Ejecuta el instalador y sigue las instrucciones. Asegúrate de marcar la opción "Add Python to PATH".

### Verificar Instalación:
Abre una terminal (busca "cmd" o "PowerShell" en el menú de inicio) y escribe:
```
python --version
```
Deberías ver algo como "Python 3.x.x".

### Crear un Entorno Virtual (Recomendado)
Es una buena práctica crear un entorno virtual para cada proyecto. Esto mantiene las bibliotecas separadas y evita conflictos.

Para cada aplicación:
1. Abre una terminal en la carpeta correspondiente (ej. `Primera_app`).
2. Crea el entorno virtual:
   ```
   python -m venv env
   ```
3. Activa el entorno:
   - En Windows (PowerShell): `env\Scripts\activate`
   - En Windows (cmd): `env\Scripts\activate.bat`
4. Verifica que esté activado (verás `(env)` al inicio de la línea de comandos).

## Cómo Ejecutar las Aplicaciones

Cada aplicación tiene su propia carpeta con un archivo `requirements.txt` que lista las bibliotecas necesarias.

### Paso 1: Instalar las Dependencias
Para cada aplicación:
1. Activa el entorno virtual (si lo creaste).
2. Ejecuta:
   ```
   pip install -r requirements.txt
   ```

### Paso 2: Ejecutar la Aplicación
En la misma terminal (con el entorno activado), ejecuta:
```
streamlit run streamlit_app.py
```

Esto abrirá la aplicación en tu navegador web automáticamente.

## Aplicaciones Incluidas

### Primera_app: Dashboard de Envíos Phoenix
- **Ubicación**: `Primera_app/`
- **Descripción**: Una aplicación para subir archivos Excel de pedidos y visualizar estadísticas agrupadas por país, empleado o método de envío.
- **Archivo de datos**: Necesitas un archivo Excel con columnas como `ship_country`, `employee_id`, `ship_via`, `order_id`.

### Segunda_app: Dashboard de Análisis Musical
- **Ubicación**: `Segunda_app/`
- **Descripción**: Una aplicación para analizar datos musicales de la base de datos Chinook, mostrando métricas y gráficos por género y álbum.
- **Archivo de datos**: Requiere el archivo `Chinook-Sample-Data.xlsx` en la carpeta `Segunda_app/`. Si no lo tienes, necesitarás obtenerlo o ajustar el código.

## Notas para Principiantes
- **Streamlit**: Es una biblioteca de Python que convierte scripts en aplicaciones web interactivas.
- **Pandas**: Se usa para manejar datos en tablas (como Excel).
- **Matplotlib/Plotly**: Bibliotecas para crear gráficos.
- Si encuentras errores, asegúrate de que todos los archivos estén en las carpetas correctas y que las dependencias estén instaladas.
- Para detener la aplicación, presiona Ctrl+C en la terminal.

¡Disfruta explorando los datos!</content>
