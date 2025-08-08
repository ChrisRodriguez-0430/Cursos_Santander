import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phoenix Shipping Dashboard", page_icon="📦", layout="wide")

st.title("📦 Phoenix Shipping Data Dashboard")

# Subir archivo Excel
uploaded_file = st.file_uploader("📤 Sube el archivo Excel de pedidos", type=["xlsx"])

if uploaded_file:
    # Cargar datos
    @st.cache_data
    def load_data(file):
        return pd.read_excel(file)

    df = load_data(uploaded_file)

    st.success("✅ Archivo cargado correctamente")

    # Selector de agrupación
    option = st.selectbox(
        "Selecciona el criterio para agrupar",
        ("País", "Empleado", "Método de envío")
    )

    # Mapeo de opción a columna
    column_map = {
        "País": "ship_country",
        "Empleado": "employee_id",
        "Método de envío": "ship_via"
    }
    group_col = column_map[option]

    # Agrupar datos
    grouped_data = (
        df.groupby(group_col)["order_id"]
        .nunique()
        .reset_index()
        .rename(columns={group_col: option, "order_id": "Número de Pedidos"})
    )

    # Mostrar tabla
    st.subheader(f"📋 Pedidos agrupados por {option}")
    st.dataframe(grouped_data)

    # Gráfica circular
    st.subheader(f"📈 Distribución de pedidos por {option}")
    fig, ax = plt.subplots()
    ax.pie(
        grouped_data["Número de Pedidos"],
        labels=grouped_data[option],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)

else:
    st.info("👆 Sube un archivo Excel para comenzar")
