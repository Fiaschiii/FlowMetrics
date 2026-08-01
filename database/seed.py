import mysql.connector
from datetime import date, timedelta
import random

DB_CONFIG = {
    "host": "localhost",
    "user": "miguel",
    "password": "*********",
    "database": "flowmetrics_db"
}

def gerar_dados_ficticios():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    print("Gerando dados fictícios...")

    
    for i in range(30):
        data = date.today() - timedelta(days=i)
        sessoes = random.randint(100, 1000)
        usuarios = random.randint(80, sessoes)
        visualizacoes = random.randint(sessoes, sessoes * 3)
        taxa_rejeicao = round(random.uniform(20.0, 70.0), 2)
        tempo_medio = round(random.uniform(60.0, 300.0), 2)

        cursor.execute("""
            INSERT INTO metricas 
                (data_referencia, sessoes, usuarios, visualizacoes, taxa_rejeicao, tempo_medio_sessao)
            VALUES 
                (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                sessoes = VALUES(sessoes),
                usuarios = VALUES(usuarios),
                visualizacoes = VALUES(visualizacoes),
                taxa_rejeicao = VALUES(taxa_rejeicao),
                tempo_medio_sessao = VALUES(tempo_medio_sessao)
        """, (data, sessoes, usuarios, visualizacoes, taxa_rejeicao, tempo_medio))

    conn.commit()
    cursor.close()
    conn.close()
    print("30 dias de dados fictícios gerados com sucesso!")

if __name__ == "__main__":
    gerar_dados_ficticios()