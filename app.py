import streamlit as st
from motor_inferencia_adaptativo import MotorInferenciaAdaptativo

st.set_page_config(page_title="Sistema Disciplinar UFAPE", layout="centered")
st.title("📘 Sistema Especialista — Regime Disciplinar Discente UFAPE")

motor = MotorInferenciaAdaptativo("historico.json")

descricao = st.text_area("Descreva a conduta do discente:")

if st.button("Analisar Conduta"):
    if descricao.strip() == "":
        st.warning("Por favor, insira uma descrição.")
    else:
        resultado = motor.inferir(descricao)
        st.markdown("### Resultado da Análise")
        st.write(f"**🧾 Classificação:** {resultado['classificacao']}")
        st.write(f"**⚖️ Penalidade:** {resultado['penalidade']}")
        st.write(f"**📚 Fundamentação:** {resultado['fundamento']}")
        st.write(f"**📌 Tipo de Regra:** {resultado['tipo_regra']}")

        st.markdown("### Este diagnóstico está correto?")
        col1, col2 = st.columns(2)
        if col1.button("✅ Sim"):
            motor.registrar_feedback(descricao, resultado, True)
            st.success("Feedback positivo registrado!")
        if col2.button("❌ Não"):
            motor.registrar_feedback(descricao, resultado, False)
            st.warning("Feedback negativo registrado.")

if st.checkbox("🔍 Ver sugestões de melhoria nas regras"):
    sugestoes = motor.sugestao_melhorias()
    st.subheader("Palavras frequentes em erros:")
    for palavra, contagem in sugestoes[:10]:
        st.write(f"{palavra}: {contagem}")

if st.checkbox("🚨 Ver histórico de desligamentos"):
    desligamentos = motor.regras_desligamento()
    for d in desligamentos:
        st.write(f"📚 {d['descricao']} — {d['fundamento']}")
