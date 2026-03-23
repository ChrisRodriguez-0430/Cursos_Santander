# Segunda App: Dashboard de Análisis Musical

Esta aplicación es un dashboard interactivo para explorar datos musicales de la base de datos Chinook, creada con Streamlit.

## ¿Qué hace esta aplicación?

Analiza una colección de pistas musicales y te muestra:
1. **Métricas generales**: Número total de pistas, álbumes únicos y géneros distintos.
2. **Gráficos**:
   - Un gráfico de barras mostrando cuántas pistas hay por género.
   - Un gráfico circular (pastel) mostrando la distribución por álbum.
3. **Filtros**: Puedes filtrar los datos por álbum, género y tipo de medio.
4. **Tabla de datos**: Una vista detallada de los datos filtrados.
5. **Descargar datos**: Un botón para guardar los datos filtrados como archivo CSV.

## Cómo usar la aplicación

1. Asegúrate de que el archivo `Chinook-Sample-Data.xlsx` esté en la carpeta `Segunda_app/`.
2. Abre la aplicación (sigue el README principal).
3. Usa los filtros en el panel lateral izquierdo para seleccionar qué datos ver.
4. Explora las métricas, gráficos y tabla.
5. Si quieres guardar los datos, haz clic en "Descargar Datos Filtrados".

## Datos necesarios

La aplicación carga automáticamente el archivo `Chinook-Sample-Data.xlsx`, que contiene hojas como:
- Data: Información de pistas.
- Album: Datos de álbumes.
- Genre: Géneros musicales.
- MediaType: Tipos de medio (CD, MP3, etc.).

Si no tienes este archivo, puedes buscar "Chinook Sample Database" en línea o crear uno similar.

## Nota sobre dependencias

El código usa Plotly para gráficos, pero el `requirements.txt` incluye Matplotlib. Si hay errores, instala Plotly con:
```
pip install plotly
```

## Explicación del código (para principiantes)

Paso a paso, el código hace lo siguiente:

- **Importar bibliotecas**: Streamlit para la app web, pandas para datos, plotly para gráficos bonitos.
- **Cargar datos**: Leer el Excel y combinar las hojas para tener toda la información junta.
- **Configurar página**: Título y diseño ancho.
- **Filtros**: Menús en el lado para elegir qué mostrar.
- **Aplicar filtros**: Solo mostrar los datos que coinciden con tus selecciones.
- **Mostrar métricas**: Números importantes en cajas.
- **Crear gráficos**: Barras para géneros, pastel para álbumes.
- **Mostrar tabla**: Una lista de los datos.
- **Botón de descarga**: Para guardar como CSV.

Es como un explorador de música: eliges qué ver y la app te lo muestra de forma visual.</content>
<parameter name="filePath">c:\Users\Chris\Documents\Cursos_Santander\My Project\Segunda_app\README.md