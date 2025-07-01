import streamlit as st

def sidebar():    
    with st.sidebar.expander("**Tipos de Penalidades**"):
        st.markdown("""
        - ⚠️ **Advertência**  - Infrações leves (Art. 216, I)
        - ⚠️ **Suspensão** - Infrações graves ou reincidência (Art. 216, II)
        - ⚠️ **Desligamento** - Infrações muito graves (Art. 216, III)
        - ⚠️ **Penalidades alternativas**  - Complementares (Art. 217)
        """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("2025 © UFAPE")