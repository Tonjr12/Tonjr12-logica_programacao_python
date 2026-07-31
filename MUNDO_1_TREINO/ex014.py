vendas = [150.0, 45.0, 300.0, 80.0]
for i, valor in enumerate(vendas, start=1):
    if i % 2 != 0:
        print(f"{i}ª Transação: R$ {valor:.2f}")