import streamlit as st
import json
import pandas as pd

# Configurações da página
st.set_page_config(page_title="SOC Dashboard", page_icon="🛡️", layout="centered")

st.title("🛡️ SOC Log Analyzer Dashboard")
st.write("Visualização interativa dos alertas gerados pelo analisador de logs.")

# Carrega os alertas do arquivo JSON
try:
    with open("reports/alerts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
except FileNotFoundError:
    st.error("Arquivo alerts.json não encontrado! Execute o analisador primeiro.")
    st.stop()

# Exibe as métricas principais
st.metric("Total de alertas", len(df))
st.metric("IPs únicos", df['ip'].nunique())

# Top 5 IPs suspeitos
st.subheader("Top 5 IPs com mais falhas")
top_ips = df['ip'].value_counts().head(5)
st.bar_chart(top_ips)

# Distribuição de severidade
st.subheader("Distribuição por Severidade")
severity_counts = df['severidade'].value_counts()
st.bar_chart(severity_counts)

# Tabela de alertas completa
st.subheader("Tabela de Alertas")
st.dataframe(df)