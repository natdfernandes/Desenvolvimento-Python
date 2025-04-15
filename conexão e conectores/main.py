import sqlite3

# Conecta e cria tabela

with sqlite3.connect("crud.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco REAL
        )
    """
    )

    # Insert
    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Teclado", 99.90)
    )
    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("MONITOR", 599.90)
    )
    # Filtrar com WHERE
    cursor.execute("SELECT nome FROM produtos WHERE nome = ?", ("COISA DE COMPUTADOR",))
    print(cursor.fetchone())  # Retorna a primeira linha: ('Maria Souza',)

    # Update
    cursor.execute(" UPDATE produtos SET preco =? WHERE nome = ? ", (109.90, "Teclado"))

    # Delete
    cursor.execute("DELETE FROM produtos WHERE id = 1")
    cursor.close
