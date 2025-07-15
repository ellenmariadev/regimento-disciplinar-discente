import streamlit as st
from system.knowledge_base import TIPOS_CONDUTA, MAPEAMENTO_CONDUTAS, AGRAVANTES

def get_user_input():
    """Coleta as entradas do usuário através da interface Streamlit"""
    
    conduta_selecionada = st.selectbox(
        "Selecione a conduta disciplinar:",
        TIPOS_CONDUTA
    )
    
    tipo_conduta = MAPEAMENTO_CONDUTAS[conduta_selecionada]["tipo"]
    
    st.info(f"**Descrição:** {MAPEAMENTO_CONDUTAS[conduta_selecionada]['descricao_detalhada']}")
    st.markdown(f"**Artigo base:** {MAPEAMENTO_CONDUTAS[conduta_selecionada]['artigo_base']}")
    
    st.subheader("Circunstâncias Agravantes")
    
    reincidente = False
    reincidente_grave = False
    
    if tipo_conduta == "agressao":
        reincidencia_texto = "Reincidente em agressão física/moral"
        reincidencia_help = "Art. 219 §5º - A reincidência em agressão acarreta a pena de desligamento"
        if st.checkbox(reincidencia_texto, help=reincidencia_help):
            reincidente_grave = True
    else:
        reincidencia_texto = "Reincidente nesta infração"
        if tipo_conduta in ["improbidade_academica", "informacao_falsa", "inutilizacao_documentos", 
                           "retirada_sem_permissao", "dano_patrimonio", "perturbacao"]:
            reincidencia_help = "Art. 219 §3º - A reincidência nas faltas I a VI importa em suspensão de 3 a 15 dias"
        else:  
            reincidencia_help = "Reincidência em ilícito penal pode agravar a penalidade"
        
        if st.checkbox(reincidencia_texto, help=reincidencia_help):
            reincidente = True
    
    agravantes_selecionados = []
    agravantes_possiveis = MAPEAMENTO_CONDUTAS[conduta_selecionada]['agravantes_possiveis']
    
    if "violencia_ou_ameaca_grave" in agravantes_possiveis:
        if st.checkbox("Violência ou grave ameaça", 
                     help="Art. 221, I - Cometimento de infração mediante violência ou grave ameaça, com emprego de arma ou substância perigosa"):
            agravantes_selecionados.append("violencia_ou_ameaca_grave")
    
    return {
        'conduta': conduta_selecionada,
        'agravantes': agravantes_selecionados,
        'reincidente': reincidente,
        'reincidente_grave': reincidente_grave
    }