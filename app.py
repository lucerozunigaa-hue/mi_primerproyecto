import streamlit as st
import pandas as pd


df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)
st.header("Base de datos de Yardas vs. Pases")
st.dataframe(df.head(),use_container_width=True)

st.header("Estadisticas Descriptivas")
st.dataframe(df.describe(), use_container_width=True)

# Cambiar el nombre de las columnas89
df.columns = [c.lower().replace('','_') for c in df.columns]
# El diagrama de caja y bigote de los pases
fig, ax = plt.subplots()
ax.set_title("Diagrama de caja y bigote\ndepases")
ax.boxplot(df['pases_completos'])
# st.header("Diagrama de caja y bigote.")
st.pyplot(fig)
# El diagrama de caja y bigote de los pases.
fig, ax = plt.subplots()

ax.set_title("Diagrama de caja y bigote\n de yardas")
ax.boxplot(df['yardas_totales'])
st.pyplot(fig)

