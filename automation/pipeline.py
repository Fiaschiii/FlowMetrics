import schedule
import time
from services.analytics_service import buscar_metricas
from services.db_service import salvar_metricas, buscar_relatorio

def executar_pipeline():
    print("\n🔄 Iniciando pipeline do FlowMetrics...")

    # 1. Busca os dados no Google Analytics
    dados = buscar_metricas(dias=7)

    # 2. Salva os dados no MySQL
    salvar_metricas(dados)

    # 3. Busca e exibe o relatório
    relatorio = buscar_relatorio()
    print("\n📊 Últimas métricas salvas:")
    for linha in relatorio[:5]:
        print(linha)

    print("✅ Pipeline concluído!\n")

# Agenda execução automática todo dia às 08:00
schedule.every().day.at("08:00").do(executar_pipeline)

if __name__ == "__main__":
    executar_pipeline()  # Executa imediatamente na primeira vez
    while True:
        schedule.run_pending()  # Fica verificando se está na hora de rodar
        time.sleep(60)          # Verifica a cada 60 segundos