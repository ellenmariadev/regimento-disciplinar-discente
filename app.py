import streamlit as st
from ui.components.header import render_header
from ui.components.results import render_results
from ui.components.forms import get_user_input
from system.engine import analisar_conduta
from ui.components.sidebar import sidebar

st.set_page_config(
    page_title="Sistema Especialista - Regime Disciplinar UFAPE",
    page_icon="🏛️",
    layout="wide"
)

render_header()

with st.form("analise_conduta_form"):
    st.subheader("Formulário de Análise de Conduta Disciplinar")
    
    dados = get_user_input()
    
    submit_button = st.form_submit_button("Analisar Conduta")

if submit_button:
    resultado = analisar_conduta(
        dados['conduta'], 
        dados['agravantes'], 
        dados['reincidente'],
        dados['reincidente_grave'],
    )
    
    render_results(resultado)

sidebar()