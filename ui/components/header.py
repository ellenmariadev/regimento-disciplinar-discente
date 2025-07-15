import streamlit as st

def render_header():
    st.title("Regime Disciplinar Discente da UFAPE")
    st.markdown("""
    Este sistema especialista analisa condutas disciplinares com base no Regimento Geral da Universidade Federal do Agreste de Pernambuco (UFAPE) e fornece recomendações sobre as penalidades aplicáveis, baseadas nas regras e artigos do regimento.
    """)