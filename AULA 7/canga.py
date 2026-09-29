import streamlit as st
from collections import Counter
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Atividade 2 - Frequência de Palavras", page_icon="📊", layout="centered")

st.title("📊 Atividade 2: Frequência de Palavras")
st.subheader("Análise de frequência em avaliações de clientes")

# Entrada do usuário
texto_padrao = "O produto é excelente, muito bom mesmo. A entrega foi rápida e o produto chegou perfeito!"
texto_usuario = st.text_area("Digite ou cole a avaliação do cliente aqui:", value=texto_padrao, height=120)

if st.button("Calcular Frequência", type="primary"):
    if texto_usuario.strip():
        # Tokenização simples e padronização para minúsculas
        palavras = texto_usuario.lower().split()
        
        # Contagem de frequência
        frequencia = Counter(palavras)
        
        # Criação de DataFrame para exibição amigável
        df_frequencia = pd.DataFrame(frequencia.items(), columns=["Palavra", "Frequência"]).sort_values(
            by="Frequência", ascending=False
        ).reset_index(drop=True)

        st.success(f"Total de palavras analisadas: **{len(palavras)}** | Palavras únicas: **{len(frequencia)}**")

        # Exibição dos resultados
        col1, col2 = st.columns([1, 1])

        with col1:
            st.write("### 📋 Tabela de Frequência")
            st.dataframe(df_frequencia, use_container_width=True)

        with col2:
            st.write("### 🔝 Top 5 Palavras Mais Repetidas")
            for palavra, freq in frequencia.most_common(5):
                st.metric(label=f"Palavra: '{palavra}'", value=f"{freq}x")

    else:
        st.warning("Por favor, digite algum texto para analisar.")