import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="FluentAI Tutor", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header, footer, #MainMenu { visibility: hidden; }
        iframe { height: 100vh !important; width: 100% !important; border: none; }
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

api_key = st.secrets.get("GROQ_API_KEY", "")
html_code = html_code.replace("__GROQ_API_KEY__", api_key)

components.html(html_code, height=900, scrolling=False)
