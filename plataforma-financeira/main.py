from ingestion.gerador_transacoes import gerar_transacao


def main():
    print("=== Plataforma de Análise Financeira e Risco ===")
    print("Status: Sistema inicializado com sucesso.\n")

    print("--- Simulando Ingestão de Transações ---")
    for i in range(1, 6):
        transacao = gerar_transacao()
        print(f"Transação {i}: {transacao}")


if __name__ == "__main__":
    main()