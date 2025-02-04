import streamlit as st
import requests
import json

# Recupera la API Key desde los secretos de Streamlit
api_key = st.secrets["KLUSTER_API_KEY"]

# Configura la URL de la API de Kluster.ai
url = "https://api.kluster.ai/v1/chat/completions"

# Define las 15 herramientas de marketing
tools = [
    "Análisis de mercado",
    "Segmentación de audiencia",
    "Estrategia de contenido",
    "SEO (Optimización de motores de búsqueda)",
    "Publicidad en redes sociales",
    "Email marketing",
    "Optimización de tasa de conversión",
    "Análisis de la competencia",
    "Campañas PPC (pago por clic)",
    "Generación de leads",
    "Automatización de marketing",
    "Marketing de influencia",
    "Branding",
    "Investigación de palabras clave",
    "Estrategias de fidelización"
]

# Función para hacer la llamada a la API
def get_kluster_response(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
        "max_completion_tokens": 2000,
        "temperature": 0.6,
        "top_p": 1,
        "messages": [{"role": "system", "content": "Eres un asistente de marketing profesional."},
                     {"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Interfaz de usuario
st.title("Herramientas de Mercadeo")

# Barra lateral con las opciones
selected_tool = st.sidebar.selectbox("Selecciona una herramienta", tools)

# Explicación general
st.sidebar.write("""
Este panel de herramientas de marketing te permitirá acceder a varias funcionalidades para mejorar tu estrategia de marketing.
""")

# Generar el prompt basado en la herramienta seleccionada
prompt = f"Explica cómo se puede aplicar la herramienta de marketing: {selected_tool}"

# Mostrar el resultado de la API
if selected_tool:
    st.write(f"Aplicando la herramienta: **{selected_tool}**")
    result = get_kluster_response(prompt)
    st.write(result['choices'][0]['message']['content'])

