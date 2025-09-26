import re
from collections import Counter
from datetime import datetime
import json

def classify_severity(count):
    """Classifica a severidade com base no número de falhas."""
    if count >= 10:
        return "CRÍTICO"
    elif count >= 5:
        return "ALTO"
    elif count >= 3:
        return "MÉDIO"
    else:
        return "BAIXO"

def analyze_logs(file_path, threshold=3, report_path="reports/report.txt"):
    with open(file_path, "r") as file:
        logs = file.readlines()

    # Regex para capturar IPs
    ip_pattern = re.compile(r'failed login from (\d+\.\d+\.\d+\.\d+)',re.IGNORECASE)
    ips = []

    for log in logs:
        match = ip_pattern.search(log)
        if match:
            ips.append(match.group(1)) 
    
    counter = Counter(ips)

    # Abre (ou cria) o relatório
    with open(report_path, "w") as report:
        report.write("=== Relatório de Análise de Logs ===\n")
        report.write(f"Gerado em: {datetime.now()}\n\n")

        print("\n Análise de logs de Segurança:")
        for ip, count in counter.items():
            severity = classify_severity(count)

            if count >= threshold:
                alert_msg = f"[{severity}] ALERTA: {ip} teve {count} falhas de login!"
                print(alert_msg)
                report.write(alert_msg + "\n")
            else:
                ok_msg = f"[{severity}] {ip} teve {count} falhas (dentro do limite)."
                print(ok_msg)
                report.write(ok_msg + "\n")

    # Salvar resultados em JSON
    results = []
    for ip, count in counter.items():
        severity = classify_severity(count)
        results.append({
            "ip": ip,
            "falhas": count,
            "severidade": severity,
            "alerta": count >= threshold
        })

    with open("reports/alerts.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4, ensure_ascii=False)
    print("\n Resultados exportados para 'reports/alerts.json'")

if __name__ == "__main__":
    analyze_logs("data/sample_logs.txt") 

