# Primera App: Dashboard de Envíos Phoenix

Esta es una aplicación simple creada con Streamlit que te ayuda a analizar datos de envíos de una empresa llamada Phoenix Shipping.

## ¿Qué hace esta aplicación?

Imagina que tienes una lista de pedidos en un archivo Excel. Esta aplicación te permite:
1. **Subir el archivo**: Selecciona un archivo Excel desde tu computadora.
2. **Elegir cómo agrupar los datos**: Puedes ver los pedidos agrupados por:
   - País (dónde se envía)
   - Empleado (quién maneja el pedido)
   - Método de envío (cómo se envía)
3. **Ver resultados**: Muestra una tabla con el número de pedidos en cada grupo y un gráfico circular (pastel) que muestra la distribución.

## Cómo usar la aplicación

1. Abre la aplicación (sigue las instrucciones del README principal).
2. Haz clic en "Sube el archivo Excel de pedidos" y selecciona tu archivo.
3. Elige una opción en el menú desplegable para agrupar los datos.
4. Mira la tabla y el gráfico que aparecen abajo.

## Datos necesarios

Tu archivo Excel debe tener al menos estas columnas:
- `ship_country`: El país de destino.
- `employee_id`: El ID del empleado.
- `ship_via`: El método de envío.
- `order_id`: El ID único del pedido.

Si no tienes un archivo así, puedes crear uno de ejemplo en Excel con esas columnas.

## Explicación del código (para principiantes)

El código es como una receta que le dice a la computadora qué hacer:

- **Importar bibliotecas**: Como pedir ingredientes. Streamlit para la web, pandas para datos, matplotlib para gráficos.
- **Configurar la página**: Darle un título y icono.
- **Subir archivo**: Un botón para elegir el archivo.
- **Cargar datos**: Leer el Excel y guardarlo en memoria.
- **Selector**: Un menú para elegir cómo agrupar.
- **Agrupar datos**: Contar pedidos únicos por el criterio elegido.
- **Mostrar tabla**: Una lista organizada.
- **Crear gráfico**: Un pastel que muestra porcentajes.

¡Es fácil! Solo sigue los pasos y explora tus datos.</content>
<parameter name="filePath">c:\Users\Chris\Documents\Cursos_Santander\My Project\Primera_app\README.md