# 🛡️ SOC Log Analyzer

O **SOC Log Analyzer** é um projeto prático de **Cibersegurança e Análise de Logs**, desenvolvido em **Python**, que simula o funcionamento de um **Security Operations Center (SOC)** no processo de **detecção e classificação de tentativas de força bruta** em sistemas de autenticação.

A solução **automatiza a leitura e o tratamento de logs**, identifica **IPs suspeitos**, **classifica níveis de severidade** e **gera relatórios e alertas em TXT e JSON**, podendo ser integrada a ferramentas **SIEM** ou usada como base para um **IDS (Intrusion Detection System)**.

---

## 🎯 Objetivo

Demonstrar, de forma simples e visual, como a **automção e a análise de logs** podem apoiar equipes de segurança na **identificação precoce de ataques** e no **fortalecimento da observabilidade** de ambientes críticos.

---

## 🚀 Funcionalidades

* 📂 Leitura e análise automatizada de logs simulados
* 🔍 Detecção de IPs com falhas repetidas de autenticação (Regex)
* 📊 Contagem e agrupamento de tentativas por endereço IP
* ⚠️ Classificação inteligente de severidade: **BAIXO, MÉDIO, ALTO, CRÍTICO**
* 📝 Geração automática de relatórios em **TXT**
* 📁 Exportação de alertas em **JSON** para integração com outras ferramentas
* 📊 Visualização interativa com **Streamlit e Plotly**
* 🛸️ Simulação de integração com **SIEM (Security Information and Event Management)**

---

## 📂 Estrutura do Projeto

```bash
soc-log-analyzer/
│── data/                # Logs de exemplo
│   └── sample_logs.txt
│── reports/             # Relatórios e saídas automáticas
│   ├── report.txt
│   ├── alerts.json
│   └── collector.log    # Log de integração SIEM simulada
│── src/                 # Código-fonte principal
│   ├── log_analyzer.py  # Analisador de logs
│   ├── send_to_siem.py  # Simulador de envio de alertas
│   └── dashboard.py     # Dashboard interativo (Streamlit)
│── .gitignore
│── requirements.txt
│── README.md
```

---

## ⚙️ Tecnologias

* Python 3.13+
* Regex (Expressões Regulares)
* JSON / Manipulação de Arquivos
* Streamlit + Plotly (Visualização de Dados)
* Integração SIEM simulada

---

## ▶️ Como Rodar

1️⃣ **Clone este repositório:**

```bash
git clone https://github.com/tiagodmoreira/soc-log-analyzer.git
cd soc-log-analyzer
```

2️⃣ **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3️⃣ **Execute o analisador de logs:**

```bash
python src/log_analyzer.py
```

4️⃣ **Inicie o dashboard interativo:**

```bash
streamlit run src/dashboard.py
```

---

📈 Projeto desenvolvido para fins educacionais, demonstrando conceitos essenciais de **monitoramento, automação e análise de segurança**.
