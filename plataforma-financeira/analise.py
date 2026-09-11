import mysql.connector


def gerar_relatorio():
    try:
        conexao = mysql.connector.connect(
            host="localhost", user="root", password="12345", database="plataforma_db"
        )
        cursor = conexao.cursor(dictionary=True)

        # Busca todas as transações cadastradas
        query = "SELECT * FROM transacoes;"
        cursor.execute(query)
        resultados = cursor.fetchall()

        print("\n=== RELATÓRIO DE TRANSAÇÕES CADASTRADAS ===")
        for linha in resultados:
            print(linha)

        cursor.close()
        conexao.close()
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")


if __name__ == "__main__":
    gerar_relatorio()
