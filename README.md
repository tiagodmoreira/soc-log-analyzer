# 🛡️ SOC Log Analyzer  

Um projeto prático de **cibersegurança**, desenvolvido em Python, que simula como um **SOC (Security Operations Center)** pode detectar tentativas de ataque de força bruta em acessos de login.  

O sistema analisa logs, identifica IPs suspeitos e gera relatórios em **TXT e JSON**.  

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


soc-log-analyzer/
│── data/ # Logs de exemplo
│ └── sample_logs.txt
│── reports/ # Relatórios gerados
│ ├── report.txt
│ └── alerts.json
│── src/ # Código-fonte principal
│ └── log_analyzer.py
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
   git clone https://[github.com/seu-usuario](https://github.com/tiagodmoreira)/soc-log-analyzer.git
   cd soc-log-analyzer








