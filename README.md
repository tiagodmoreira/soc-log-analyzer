#🛡️ SOC Log Analyzer

O SOC Log Analyzer é um projeto prático de Cibersegurança e Análise de Logs desenvolvido em Python, que simula o funcionamento de um Security Operations Center (SOC) no processo de detecção e classificação de tentativas de força bruta em sistemas de autenticação.
A solução automatiza a leitura e o tratamento de logs, identifica IPs suspeitos, classifica níveis de severidade e gera relatórios e alertas em TXT e JSON, podendo ser integrada a ferramentas SIEM ou usada como base para um IDS (Intrusion Detection System).

🎯 Objetivo: Demonstrar, de forma simples e visual, como a automação e a análise de logs podem apoiar equipes de segurança na identificação precoce de ataques e no fortalecimento da observabilidade de ambientes críticos.

Funcionalidades
📂 Leitura e análise automatizada de logs simulados
🔍 Detecção de IPs com falhas repetidas de autenticação (Regex)
📊 Contagem e agrupamento de tentativas por endereço IP
⚠️ Classificação inteligente de severidade: BAIXO, MÉDIO, ALTO, CRÍTICO
📝 Geração automática de relatórios em TXT
📑 Exportação de alertas em JSON para integração com outras ferramentas

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


```markdown
## Tecnologias

Python 3.13+
Regex (expressões regulares)
JSON / Manipulação de arquivos
Streamlit + Plotly (visualização de dados)
Integração SIEM simulada

---

## ▶️ Como Rodar  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/tiagodmoreira/soc-log-analyzer.git
cd soc-log-analyzer

2. Instalar as dependências
pip install -r requirements.txt

3️. Executar o analisador de logs
python src/log_analyzer.py

4️. Executar o dashboard interativo
streamlit run src/dashboard.py







