import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos desde Excel
@st.cache_data
def load_data():
    xls = pd.ExcelFile("Chinook-Sample-Data.xlsx")
    data = xls.parse("Data")
    albums = xls.parse("Album")
    genres = xls.parse("Genre")
    media_types = xls.parse("MediaType")
    return data, albums, genres, media_types

# Obtener los datos
data, albums, genres, media_types = load_data()

# Unir con tabla de álbum para obtener el AlbumId y ArtistId
df = data.merge(albums, left_on="Album", right_on="Title", how="left")

# Interfaz
st.set_page_config(page_title="Análisis Musical IA - Santander", layout="wide")
st.title("🎵 Dashboard de Análisis Musical")
st.markdown("**Curso de Inteligencia Artificial - Santander**")

# Filtros en sidebar
st.sidebar.header("🎚️ Filtros")
album_filter = st.sidebar.multiselect("Álbum", options=df["Album"].unique(), default=df["Album"].unique())
genre_filter = st.sidebar.multiselect("Género", options=df["Genre"].unique(), default=df["Genre"].unique())
media_filter = st.sidebar.multiselect("Tipo de Medio", options=df["MediatType"].unique(), default=df["MediatType"].unique())

# Aplicar filtros
filtered_df = df[
    (df["Album"].isin(album_filter)) &
    (df["Genre"].isin(genre_filter)) &
    (df["MediatType"].isin(media_filter))
]

# Métricas generales
st.subheader("📈 Métricas Generales")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Pistas", len(filtered_df))
col2.metric("Álbumes Únicos", filtered_df["Album"].nunique())
col3.metric("Géneros Distintos", filtered_df["Genre"].nunique())

# Gráfico de barras por género
st.subheader("🎼 Distribución por Género")
genre_chart = filtered_df["Genre"].value_counts().reset_index()
genre_chart.columns = ["Género", "Cantidad"]
fig1 = px.bar(genre_chart, x="Género", y="Cantidad", color="Género", title="Pistas por Género")
st.plotly_chart(fig1, use_container_width=True)

# Gráfico de pastel por álbum
st.subheader("💿 Álbumes más Frecuentes")
album_chart = filtered_df["Album"].value_counts().reset_index()
album_chart.columns = ["Álbum", "Cantidad"]
fig2 = px.pie(album_chart, names="Álbum", values="Cantidad", title="Distribución de Pistas por Álbum")
st.plotly_chart(fig2, use_container_width=True)

# Tabla de datos filtrados
st.subheader("🧾 Vista Tabular de los Datos Filtrados")
st.dataframe(filtered_df)

# Exportar CSV
st.download_button(
    "📥 Descargar Datos Filtrados",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="datos_filtrados_chinook.csv",
    mime="text/csv"
)
