class Aluno:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, matricula, curso, nota):
        with self.db.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO alunos(nome, matricula, curso, nota) VALUES (%s, %s, %s, %s) RETURNING id",
                (nome, matricula, curso, nota),
            )
            self.db.conn.commit()
            return cursor.fetchone()[0]

    def ler_todos(self):
        with self.db.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM alunos ORDER BY id")
            return cursor.fetchall()

    def atualizar(self, id, nome, matricula, curso, nota):
        with self.db.conn.cursor() as cursor:
            cursor.execute(
                """UPDATE alunos
                SET nome=%s, curso=%s, nota=%s
                WHERE id=%s""",
                (nome, matricula, curso, nota, id),
            )
            self.db.conn.commit()

    def deletar(self, id):
        with self.db.conn.cursor() as cursor:
            cursor.execute("DELETE FROM alunos WHERE id=%s", (id,))
            self.db.conn.commit()
