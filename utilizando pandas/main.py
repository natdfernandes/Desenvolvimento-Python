import pandas as pd
import sqlite3
from sqlite3 import Error


def inserir_dados():
    conn = sqlite3.connect("Banco.db")
    try:
        # Conectar ao banco
        cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS tabela (
                       coluna1 varchar(50), 
                       coluna2 varchar(50),
                       coluna3 varchar(50)
        )
"""
        )
        # Ler excel
        df = pd.read_excel("Dados.xlsx")

        # Insert cada linha
        for index, row in df.iterrows():
            sql = """INSERT INTO tabela (coluna1, coluna2, coluna3)
             VALUES (?, ?, ?)"""
            cursor.execute(
                sql, (row["ColunaExcel1"], row["ColunaExcel2"], row["ColunaExcel3"])
            )
        conn.commit()
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        conn.rollback()

    finally:
        if conn:
            conn.close()


inserir_dados()
