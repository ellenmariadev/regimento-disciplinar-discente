import streamlit as st
from system.knowledge_base import ARTIGOS_REGIMENTO

def render_results(resultado):
    st.header("Resultado da Análise")
    
    st.subheader("Penalidades")
    for penalidade in resultado['penalidades']:
        if penalidade['gravidade'] <= 2:
            st.warning(f"**{penalidade['nome']}**")
        if penalidade['gravidade'] > 2:
            st.error(f"**{penalidade['nome']}**")        
        st.markdown(f"""
        - **Artigo:** {penalidade['artigo']}
        - **Descrição:** {penalidade['descricao']}
        """)
    
    st.subheader("Detalhes")
    for explicacao in resultado['explicacao']:
        st.markdown(f"- {explicacao}")
    
    st.subheader("Artigos")
    artigos_unicos = list(set(resultado['artigos']))
    for artigo in artigos_unicos:
        if artigo in ARTIGOS_REGIMENTO:
            st.markdown(f"""
            **{artigo}:**
            {ARTIGOS_REGIMENTO[artigo]}
            """)
    
    with st.expander("Detalhes do Raciocínio do Sistema"):
        for item in resultado['trace']:
            if item['type'] == 'fact_declared':
                st.markdown(f"**Passo {item['step']}:** Fato declarado: {item['fact']} (fonte: {item['source']})")
            elif item['type'] == 'rule_applied':
                st.markdown(f"**Passo {item['step']}:** Regra aplicada: {item['rule']}")
                st.markdown(f"- {item['explanation']}")