import psycopg2
from psycopg2 import OperationalError


class Database:

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                database="escola",
                user="postgres",
                password="2025",
                host="localhost",
                port="5432",
            )
            print("Conexão bem sucedida!")
        except OperationalError as e:
            print(f"Erro ao conectar: {e}")
