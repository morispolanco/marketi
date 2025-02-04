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
        "model": "klusterai/Meta-Llama-3.1-405B-Instruct-Turbo",
        "max_completion_tokens": 2000,
        "temperature": 0.6,
        "top_p": 1,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        try:
            response_json = response.json()
            return response_json.get("choices", [{}])[0].get("message", {}).get("content", "Error: No se recibió contenido válido.")
        except json.JSONDecodeError:
            return "Error: La respuesta de la API no es un JSON válido."
    else:
        return f"Error en la API: {response.status_code} - {response.text}"

st.set_page_config(page_title="Herramientas de Mercadeo", layout="wide")
st.sidebar.title("Menú de Herramientas de Mercadeo")

# Sección para que el usuario describa su negocio
st.sidebar.subheader("Describe tu negocio")
business_description = st.sidebar.text_area("Ingresa una breve descripción de tu negocio")

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
    "16. Influencer Marketing": "Aprovecha el poder de los influencers en tu estrategia.",
    "17. Growth Hacking": "Implementa técnicas creativas para acelerar el crecimiento.",
    "18. Marketing Automation": "Automatiza tus procesos de mercadeo para mayor eficiencia.",
    "19. Experiencia del Cliente": "Mejora la experiencia del usuario con tu marca.",
    "20. Neuromarketing": "Aplica principios de psicología en tu estrategia de ventas.",
    "21. Storytelling": "Aprende a contar historias que conecten con tu audiencia.",
    "22. Análisis de Competencia": "Obtén información valiosa sobre tus competidores.",
    "23. Retención de Clientes": "Crea estrategias para fidelizar a tus clientes.",
    "24. Campañas de Remarketing": "Convierte visitantes en clientes con estrategias de remarketing.",
    "25. Marketing de Afiliación": "Explora oportunidades de afiliación para potenciar tus ventas."
}

# Mostrar herramientas en la barra lateral
seleccion = st.sidebar.radio("Selecciona una herramienta", list(herramientas.keys()))
st.sidebar.write("**Descripción:**", herramientas[seleccion])

if st.sidebar.button("Ejecutar Herramienta"):
    with st.spinner("Procesando..."):
        prompt = f"Genera un análisis sobre {seleccion}. Mi negocio es: {business_description}" if business_description else f"Genera un análisis sobre {seleccion}"
        resultado = call_kluster_api(prompt)
        st.subheader(seleccion)
        st.write(resultado)

st.sidebar.markdown("---")
st.sidebar.info("Desarrollado con Kluster AI y Streamlit.")
