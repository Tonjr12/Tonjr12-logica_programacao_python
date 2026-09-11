import mysql.connector


def conectar():
    """Cria e retorna a conexão com o banco MySQL local."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",  # Coloque a sua senha do MySQL aqui se houver
        database="plataforma_db",
    )


def salvar_transacao(transacao):
    """Insere uma transação gerada na tabela transacoes do MySQL."""
    conexao = conectar()
    cursor = conexao.cursor()

    query = """
        INSERT INTO transacoes (transacao_id, cliente_id, valor, tipo, data_hora)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (
        transacao["transacao_id"],
        transacao["cliente_id"],
        transacao["valor"],
        transacao["tipo"],
        transacao["data_hora"],
    )

    cursor.execute(query, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
