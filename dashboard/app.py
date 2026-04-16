# dashboard/app.py
import streamlit as st
import pandas as pd
import mysql.connector
import subprocess
import sys
import os

# Configuração da página
st.set_page_config(
    page_title="FlowMetrics",
    page_icon="📊",
    layout="wide"
)

# Conexão com o banco
DB_CONFIG = {
    "host": "localhost",
    "user": "miguel",
    "password": "fiaschi0987",
    "database": "flowmetrics_db"
}

def carregar_dados():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        df = pd.read_sql("SELECT * FROM metricas ORDER BY data_referencia DESC", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Erro ao conectar ao banco: {e}")
        return None

def executar_pipeline():
    try:
        subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True
        )
        st.success("✅ Pipeline executado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao executar pipeline: {e}")

# Header
st.title("📊 FlowMetrics")
st.subheader("Análise automatizada de dados do Google Analytics")
st.divider()

# Botão para rodar o pipeline manualmente
col1, col2 = st.columns([1, 3])
with col1:
    if st.button("▶️ Executar Pipeline", type="primary"):
        with st.spinner("Executando pipeline..."):
            executar_pipeline()

st.divider()

# Carrega os dados
df = carregar_dados()

if df is not None and not df.empty:

    # Métricas resumidas
    st.subheader("📈 Resumo Geral")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total de Sessões", f"{df['sessoes'].sum():,}")
    m2.metric("Total de Usuários", f"{df['usuarios'].sum():,}")
    m3.metric("Total de Visualizações", f"{df['visualizacoes'].sum():,}")
    m4.metric("Média Taxa de Rejeição", f"{df['taxa_rejeicao'].mean():.2f}%")

    st.divider()

    # Gráficos
    st.subheader("📊 Evolução das Métricas")
    tab1, tab2, tab3 = st.tabs(["Sessões", "Usuários", "Visualizações"])

    with tab1:
        st.line_chart(df.set_index("data_referencia")["sessoes"])
    with tab2:
        st.line_chart(df.set_index("data_referencia")["usuarios"])
    with tab3:
        st.line_chart(df.set_index("data_referencia")["visualizacoes"])

    st.divider()

    # Tabela completa
    st.subheader("📋 Histórico Completo")
    st.dataframe(df, use_container_width=True)

else:
    st.warning("⚠️ Nenhum dado encontrado! Clique em 'Executar Pipeline' para buscar os dados.")