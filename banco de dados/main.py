import sqlite3

# Conecta a um arquivo de banco de dados (cria se não existir)

conn = sqlite3.connect("exemple.db")
cursor = conn.cursor()

# Cria uma tabela 'clientes' se ela não existir
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ALUNOS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE)
    
"""
)
# Salva as alterações
conn.commit()
# Inserindo um registro
cursor.execute("INSERT INTO ALUNOS(nome, email) VALUES (?,?)", ("ola", "ola@gmail.com"))
conn.commit()

# Inserindo múltiplos registros de uma vez
dados = [("maria Souza", "maria@gmail.com"), ("Carlos Lima", "carlos@gmail.com")]

cursor.executemany("INSERT INTO ALUNOS (nome, email) VALUES (?, ?)", dados)
conn.commit()

# Selecionar todos os registros
cursor.execute("SELECT * FROM ALUNOS")
registros = cursor.fetchall()  # Retorna uma lista de tuplas

for linha in registros:
    print(linha)  # Ex: (1, ' João Silva', 'Joao@gmail.com)

# Filtrar com WHERE
cursor.execute("SELECT nome FROM ALUNOS WHERE email = ?", ("maria@gmail.com"))
print(cursor.fetchone())
