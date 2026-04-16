from database.setup_db import criar_banco
from automation.pipeline import executar_pipeline, schedule, time

def main():
    print("🚀 Iniciando FlowMetrics...")
    
    # 1. Garante que o banco está criado
    criar_banco()
    
    # 2. Executa o pipeline imediatamente
    executar_pipeline()
    
    # 3. Mantém a automação rodando
    print("⏰ Agendamento ativo — pipeline roda todo dia às 08:00!")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()