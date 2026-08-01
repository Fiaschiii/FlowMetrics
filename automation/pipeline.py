import schedule
import time
from services.analytics_service import buscar_metricas
from services.db_service import salvar_metricas, buscar_relatorio

def executar_pipeline():
    print("\nIniciando pipeline do FlowMetrics...")

    
    dados = buscar_metricas(dias=7)

    
    salvar_metricas(dados)

    
    relatorio = buscar_relatorio()
    print("\nÚltimas métricas salvas:")
    for linha in relatorio[:5]:
        print(linha)

    print("Pipeline concluído!\n")


schedule.every().day.at("08:00").do(executar_pipeline)

if __name__ == "__main__":
    executar_pipeline()  
    while True:
        schedule.run_pending()  
        time.sleep(60)          