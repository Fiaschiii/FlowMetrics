import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "miguel",
    "password": "fiaschi0987",
    "database": "flowmetrics_db"
}

def salvar_metricas(dados: list):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    sql = """
        INSERT INTO metricas 
            (data_referencia, sessoes, usuarios, visualizacoes, taxa_rejeicao, tempo_medio_sessao)
        VALUES 
            (%(data_referencia)s, %(sessoes)s, %(usuarios)s, %(visualizacoes)s, 
             %(taxa_rejeicao)s, %(tempo_medio_sessao)s)
        ON DUPLICATE KEY UPDATE
            sessoes = VALUES(sessoes),
            usuarios = VALUES(usuarios),
            visualizacoes = VALUES(visualizacoes)
    """

    cursor.executemany(sql, dados)
    conn.commit()
    print(f"{cursor.rowcount} registros salvos no MySQL!")

    cursor.close()
    conn.close()

def buscar_relatorio():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT data_referencia, sessoes, usuarios, visualizacoes,
               ROUND(taxa_rejeicao, 2) AS taxa_rejeicao,
               ROUND(tempo_medio_sessao, 2) AS tempo_medio_sessao
        FROM metricas
        ORDER BY data_referencia DESC
        LIMIT 30
    """)

    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultado