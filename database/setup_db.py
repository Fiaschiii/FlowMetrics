import mysql.connector

def criar_banco():
    conn = mysql.connector.connect(
        host="localhost",
        user="miguel",
        password="fiaschi0987"
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS flowmetrics_db")
    cursor.execute("USE flowmetrics_db")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metricas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data_referencia DATE NOT NULL UNIQUE,
            sessoes INT,
            usuarios INT,
            visualizacoes INT,
            taxa_rejeicao FLOAT,
            tempo_medio_sessao FLOAT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Banco flowmetrics_db criado com sucesso!")

if __name__ == "__main__":
    criar_banco()