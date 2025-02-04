import streamlit as st
import requests
import json

# Función para interactuar con la API de Kluster AI
def get_kluster_response(user_input):
    api_url = "https://api.kluster.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['klusterai']['api_key']}",
        "Content-Type": "application/json",
    }
    
    data = {
        "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
        "max_completion_tokens": 2000,
        "temperature": 0.6,
        "top_p": 1,
        "messages": [{"role": "user", "content": user_input}]
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error en la solicitud a la API."

# Función principal para la interfaz Streamlit
def main():
    st.title("Herramientas de Mercadeo para tu Negocio")

    # Menú en la barra lateral
    st.sidebar.title("Herramientas de Mercadeo")
    tools = [
        "Estrategia Digital", "Análisis de Competencia", "Posicionamiento SEO", "Email Marketing",
        "Publicidad en Redes Sociales", "Marketing de Influencers", "Gestión de Contenido", "Análisis de Datos",
        "Branding y Diseño", "Automatización de Marketing", "Gestión de Reputación Online", "Análisis de Sentimientos",
        "Planificación de Campañas", "Optimización de Conversiones", "Estrategias de Precios"
    ]
    
    tool_selection = st.sidebar.radio("Selecciona una herramienta", tools)

    # Descripción del negocio del usuario
    user_input = st.text_area("Describe tu negocio y cómo te gustaría mejorar con esta herramienta:")

    # Obtener respuesta de la API de Kluster
    if user_input:
        st.write(f"Buscando ideas para '{tool_selection}'...")
        response = get_kluster_response(user_input)
        st.write(response)

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
