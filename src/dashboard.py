import streamlit as st
import json
import pandas as pd
import plotly.express as px

# ==============================
# ⚙️ CONFIGURAÇÕES DA PÁGINA
# ==============================
st.set_page_config(
    page_title="SOC Dashboard",
    layout="wide"
)

st.markdown("""
    <style>
        /* Fundo escuro e estilo SOC */
        .stApp {
            background-color: #0f172a;
            color: #e2e8f0;
        }
        .stMetric {
            background-color: #1e293b;
            border-radius: 10px;
            padding: 15px;
        }
        h1 {
            color: #93c5fd;
        }
        h2, h3 {
            color: #e2e8f0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("SOC Log Analyzer Dashboard")
st.write("Visualização interativa e estilizada dos alertas gerados pelo analisador de logs.")

# ==============================
# 📂 CARREGAR DADOS
# ==============================
try:
    with open("reports/alerts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
except FileNotFoundError:
    st.error("❌ Arquivo alerts.json não encontrado! Execute o analisador primeiro.")
    st.stop()

# ==============================
# 📊 KPIs DE RESUMO
# ==============================
total_ips = len(df)
total_falhas = df["falhas"].sum()
total_alertas = df[df["alerta"] == True].shape[0]
criticos = df[df["severidade"] == "CRÍTICO"].shape[0]
percent_alertas = (total_alertas / total_ips) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("IPs Analisados", total_ips)
col2.metric("Alertas", total_alertas)
col3.metric("Críticos", criticos)
col4.metric("% de Alertas", f"{percent_alertas:.1f}%")

# ==============================
# 🧭 TOP 5 IPs SUSPEITOS
# ==============================
st.subheader("Top 5 IPs com mais falhas")
top_ips = df.sort_values(by="falhas", ascending=False).head(5)

fig1 = px.bar(
    top_ips,
    x="ip",
    y="falhas",
    color="severidade",
    title="Top 5 IPs com mais falhas",
    color_discrete_map={
        "CRÍTICO": "#dc2626",
        "ALTO": "#f97316",
        "MÉDIO": "#eab308",
        "BAIXO": "#22c55e"
    }
)
st.plotly_chart(fig1, use_container_width=True)

# ==============================
# ⚠️ DISTRIBUIÇÃO DE SEVERIDADES
# ==============================
st.subheader("Distribuição por Severidade")

fig2 = px.histogram(
    df,
    x="severidade",
    color="severidade",
    color_discrete_map={
        "CRÍTICO": "#dc2626",
        "ALTO": "#f97316",
        "MÉDIO": "#eab308",
        "BAIXO": "#22c55e"
    },
    title="Distribuição de Severidades"
)
st.plotly_chart(fig2, use_container_width=True)


# 🧾 TABELA COMPLETA DE ALERTAS
# ==============================
st.subheader("Tabela Completa de Alertas")
st.dataframe(df)