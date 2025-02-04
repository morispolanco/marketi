import streamlit as st
import requests
import json
import os

def call_kluster_api(prompt):
    api_key = st.secrets["KLUSTER_API_KEY"]
    url = "https://api.kluster.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
        "max_completion_tokens": 2000,
        "temperature": 0.6,
        "top_p": 1,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["choices"][0]["message"]["content"]

st.set_page_config(page_title="Herramientas de Mercadeo", layout="wide")
st.sidebar.title("Menú de Herramientas de Mercadeo")

# Lista de herramientas disponibles
herramientas = {
    "1. Análisis FODA": "Realiza un análisis de fortalezas, oportunidades, debilidades y amenazas.",
    "2. Segmentación de Mercado": "Identifica y describe segmentos de clientes para tu negocio.",
    "3. Buyer Persona": "Crea un perfil detallado de tu cliente ideal.",
    "4. Matriz BCG": "Clasifica productos en estrellas, vacas, incógnitas y perros.",
    "5. Estrategia de Precio": "Obtén recomendaciones para fijación de precios.",
    "6. Estrategia de Producto": "Desarrolla estrategias para mejorar tu producto.",
    "7. Marketing Digital": "Genera estrategias digitales personalizadas.",
    "8. Publicidad en Redes Sociales": "Optimiza tus campañas en Facebook, Instagram, y más.",
    "9. SEO y SEM": "Mejora la visibilidad de tu web con estrategias SEO/SEM.",
    "10. Email Marketing": "Crea campañas de email efectivas.",
    "11. Customer Journey": "Mapea la experiencia del cliente con tu marca.",
    "12. Benchmarking": "Compara tu negocio con la competencia.",
    "13. Estrategia de Branding": "Desarrolla una identidad de marca sólida.",
    "14. Funnel de Ventas": "Diseña un embudo de ventas optimizado.",
    "15. Estrategia de Contenidos": "Planifica contenidos para atraer a tu audiencia.",
}

# Mostrar herramientas en la barra lateral
seleccion = st.sidebar.radio("Selecciona una herramienta", list(herramientas.keys()))
st.sidebar.write("**Descripción:**", herramientas[seleccion])

if st.sidebar.button("Ejecutar Herramienta"):
    with st.spinner("Procesando..."):
        resultado = call_kluster_api(f"Genera un análisis sobre {seleccion}")
        st.subheader(seleccion)
        st.write(resultado)

st.sidebar.markdown("---")
st.sidebar.info("Desarrollado con Kluster AI y Streamlit.")
