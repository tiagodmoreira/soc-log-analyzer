import json
from datetime import datetime

def send_alerts_to_siem(file_path="reports/alerts.json", output="reports/collector.log"):
    with open(file_path, "r", encoding="utf-8") as f:
        alerts = json.load(f)

    with open(output, "a", encoding="utf-8") as log:
        log.write(f"\n=== Envio simulado para SIEM em {datetime.now()} ===\n")
        for alert in alerts:
            log.write(json.dumps(alert, ensure_ascii=False) + "\n")

    print(f"[✅] {len(alerts)} alertas enviados para o SIEM simulado ({output}).")

if __name__ == "__main__":
    send_alerts_to_siem()
