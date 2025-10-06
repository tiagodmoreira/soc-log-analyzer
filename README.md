# 🛡️ SOC Log Analyzer  

Um projeto prático de **Cibersegurança** que demonstra como um **SOC (Security Operations Center)** detecta e classifica **tentativas de força bruta** em logs de autenticação.  
Desenvolvido em **Python**, este sistema analisa logs, identifica IPs suspeitos e gera relatórios automáticos em **TXT** e **JSON**.  

🔒 Este projeto pode ser usado como base para sistemas de **detecção de intrusão (IDS)**, análise de **logs SSH** ou integração com **ferramentas SIEM**.

---

## 🚀 Funcionalidades  
- 📂 Leitura de arquivos de log simulados  
- 🔍 Extração de IPs que falharam login (Regex)  
- 📊 Contagem de tentativas de login por IP  
- ⚠️ Classificação de severidade: **BAIXO, MÉDIO, ALTO, CRÍTICO**  
- 📝 Geração de relatórios em **TXT**  
- 📑 Exportação de alertas em **JSON** (para integração com outras ferramentas)  

---

## 📂 Estrutura do Projeto  

```bash
soc-log-analyzer/
│── data/              # Logs de exemplo
│   └── sample_logs.txt
│── reports/           # Relatórios gerados automaticamente
│   ├── report.txt
│   └── alerts.json
│── src/               # Código-fonte principal
│   └── log_analyzer.py
│── .gitignore
│── requirements.txt
│── README.md

## ⚙️ Tecnologias  
- Python 3.13+  
- Regex  
- JSON  
- Manipulação de arquivos  

---

## ▶️ Como Rodar  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/tiagodmoreira/soc-log-analyzer.git
cd soc-log-analyzer









